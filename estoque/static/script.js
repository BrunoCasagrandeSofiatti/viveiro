

// ########################### Faz a requisição dos dados na API PARA PREENCHER A TABELA PRODUTOS ###########################
function get_produtos_cadastrados(){

	const endpoint = `/listarprodutos/`
	var t = $('#table-stations-off').DataTable();
	
	// limpar  tabela
	t.clear();
	var estacao = 10;
	var objeto = {
		'station_id': estacao,
	};
	$.ajax({
		url: endpoint,
		type:'get',
		headers: { 'Content-Type': 'application/json' },
		data: objeto,
		success: function(data) {
			console.log()
			//var tbody = '';
			var rows_datetime = Object.keys(data)
			for (var index in rows_datetime){
				var row = rows_datetime[ index ]                        
				var cols = data[ row ]                        						
				var t_row = []
				for(var index in cols){   
					 
					if (index != 'id'){
						t_row.push(cols[ index ]);
					}else{
						var id_prod = cols[ index ]
						var tds = `<span style="width: 140px;">	
							<a href="#" class="m-portlet__nav-link btn m-btn m-btn--hover-accent m-btn--icon m-btn--icon-only m-btn--pill" data-toggle="tooltip" title="" data-original-title="Editar">
								<i class="fa fa-edit fa-sm" style="color: #00c5dc;"></i>
							</a> `+
							
							`<a href="#" onclick="delete_prod(${id_prod})" class="m-portlet__nav-link btn m-btn m-btn--hover-danger m-btn--icon m-btn--icon-only m-btn--pill" data-toggle="tooltip" title="" data-original-title="Excluir">` +
								`<i class="fa fa-trash-alt fa-sm" style="color: #f4516c;"></i>
							</a>   

							<script>
								$(document).ready(function(){
									$('[data-toggle="tooltip"]').tooltip();   
								});
							</script>
					      </span>`
						  
						t_row.push(tds);      					
					}								     
					
				}
				t.row.add(t_row).draw(false);
			}                
		},
		error: function(error){
			console.error(error)
		},
		complete: function(data){
			t.draw()
		},
		cache: false
	});
};  


// ########################### Faz a requisição dos dados na API PARA PREENCHER A TABELA CATEGORIAS ###########################
function get_categorias_cadastradas(){

	const endpoint = `/listarcategorias/`
	var t = $('#table-stations-off').DataTable();
	
	// limpar  tabela
	t.clear();
	var estacao = 10;
	var objeto = {
		'station_id': estacao,
	};
	$.ajax({
		url: endpoint,
		type:'get',
		headers: { 'Content-Type': 'application/json' },
		data: objeto,
		success: function(data) {
			console.log()
			//var tbody = '';
			var rows_datetime = Object.keys(data)
			for (var index in rows_datetime){
				var row = rows_datetime[ index ]                        
				var cols = data[ row ]                        						
				var t_row = []
				for(var index in cols){   
					 
					if (index != 'id'){
						t_row.push(cols[ index ]);
					}else{
						var id_prod = cols[ index ]
						var tds = `<span style="width: 140px;">	
							<a href="#" class="m-portlet__nav-link btn m-btn m-btn--hover-accent m-btn--icon m-btn--icon-only m-btn--pill" data-toggle="tooltip" title="" data-original-title="Editar">
								<i class="fa fa-edit fa-sm" style="color: #00c5dc;"></i>
							</a> `+
							
							`<a href="#" onclick="delete_prod(${id_prod})" class="m-portlet__nav-link btn m-btn m-btn--hover-danger m-btn--icon m-btn--icon-only m-btn--pill" data-toggle="tooltip" title="" data-original-title="Excluir">` +
								`<i class="fa fa-trash-alt fa-sm" style="color: #f4516c;"></i>
							</a>   

							<script>
								$(document).ready(function(){
									$('[data-toggle="tooltip"]').tooltip();   
								});
							</script>
					      </span>`
						  
						t_row.push(tds);      					
					}								     
					
				}
				t.row.add(t_row).draw(false);
			}                
		},
		error: function(error){
			console.error(error)
		},
		complete: function(data){
			t.draw()
		},
		cache: false
	});
};  

// ########################### JANELA DE ALERTA OK, FALHA ###########################
function mostraDialogo(mensagem, tipo, tempo){
	// se houver outro alert desse sendo exibido, cancela essa requisição
	if($("#message").is(":visible")){
	  return false;
	}
	// se não setar o tempo, o padrão é 3 segundos
	if(!tempo){
	  var tempo = 4000;
	}
	// se não setar o tipo, o padrão é alert-info
	if(!tipo){
	  var tipo = "info";
	}
  
	// monta o css da mensagem para que fique flutuando na frente de todos elementos da página
	var cssMessage = "display: block; position: fixed; top: 0; left: 20%; right: 20%; width: 60%; padding-top: 10px; z-index: 9999";
	var cssInner = "margin: 0 auto; box-shadow: 1px 1px 5px black;";
  
	// monta o html da mensagem com Bootstrap
	var dialogo = "";
	dialogo += '<div id="message" style="'+cssMessage+'">';
	dialogo += '    <div class="alert alert-'+tipo+' alert-dismissable" style="'+cssInner+'">';
	dialogo += '    <a href="#" class="close" data-dismiss="alert" aria-label="close">×</a>';
	dialogo +=          mensagem;
	dialogo += '    </div>';
	dialogo += '</div>';
  
	// adiciona ao body a mensagem com o efeito de fade
	$("body").append(dialogo);
	$("#message").hide();
	$("#message").fadeIn(200);
  
	// contador de tempo para a mensagem sumir
	setTimeout(function() {
	  $('#message').fadeOut(400, function(){
		$(this).remove();
	  });
	}, tempo); // milliseconds
  };
