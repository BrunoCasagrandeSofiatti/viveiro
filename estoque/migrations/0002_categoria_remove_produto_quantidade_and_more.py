# Generated by Django 4.1.1 on 2022-09-25 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='produto',
            name='quantidade',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='valor',
        ),
        migrations.AddField(
            model_name='produto',
            name='data_cadastro',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='estoque.fornecedor'),
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='estoque.categoria'),
        ),
    ]
