from django.db import models


# Cadastro Cliente
class Cliente(models.Model):

    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    ESTADO_CIVIL_CHOICES = (
        ('S', 'Solteiro'),
        ('C', 'Casado'),
        ('D', 'Divorciado'),
        ('V', 'Viúvo'),
    )

    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado civil')
    celular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')

    def __str__(self):
        return self.nome

# Cadastro Fornecedor
class Fornecedor(models.Model):
    nome_fantasia = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18, help_text='XX.XXX.XXX/0001-XX')
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    celular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')

    def __str__(self):
        return self.nome_fantasia


class Categoria(models.Model):
    descricao = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.descricao

class Produto(models.Model):
    descricao = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, blank=False)
    #valor = models.DecimalField(max_digits=8, decimal_places=2)
    data_cadastro = models.DateField(null=True, blank=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.descricao


class Estoque(models.Model):
    id_produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField(verbose_name="Quantidade", blank=False, null=False)
    estoque_minimo = models.IntegerField()

    def __str__(self):
        return self.id_produto_descricao
          