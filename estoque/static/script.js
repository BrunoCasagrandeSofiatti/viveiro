
// Faz a requisição dos dados na API.
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
				var tds = `<span style="width: 140px;">	
							<a href="/adm/contratos/367d2353-b6a6-4bda-b3b0-1391fcfe2b61/editar" class="m-portlet__nav-link btn m-btn m-btn--hover-accent m-btn--icon m-btn--icon-only m-btn--pill" data-toggle="tooltip" title="" data-original-title="Editar">
								<i class="fa fa-edit fa-sm" style="color: #00c5dc;"></i>
							</a> 
							
							<a href="#" onclick="confirmar_exclusao('/adm/contratos/367d2353-b6a6-4bda-b3b0-1391fcfe2b61/excluir', 'Tem certeza que deseja excluir o contrato: 0 - UnimedDigital Teste ?');" class="m-portlet__nav-link btn m-btn m-btn--hover-danger m-btn--icon m-btn--icon-only m-btn--pill" data-toggle="tooltip" title="" data-original-title="Excluir">
								<i class="fa fa-trash-alt fa-sm" style="color: #f4516c;"></i>
							</a>   
	
							<!-- <a href="#" onclick="libera_permisao_contrato_usuario('/adm/contratos/367d2353-b6a6-4bda-b3b0-1391fcfe2b61/adicionar_usuarioContrato');" class="m-portlet__nav-link btn m-btn m-btn--hover-success m-btn--icon m-btn--icon-only m-btn--pill" data-toggle="tooltip" title="" data-original-title="Liberar contrato no meu login">
								<i class="fa fa-play fa-sm" style="color: #34bfa3;"></i>
							</a> -->

							<script>
								$(document).ready(function(){
									$('[data-toggle="tooltip"]').tooltip();   
								});
							</script>
					      </span>`			
				var t_row = []
				for(var index in cols){    
					if (index != 'acoes'){
						//tds += `<td class="data-values"> ` + `${ cols[ index ] }</td>`     
						t_row.push(cols[ index ])
					}else{
						t_row.push(tds)
					}            					
				}
				t.row.add(t_row).draw(false);
				//tbody += `<tr>${tds}</tr>`
			}                
			//$(`#body_table_stations_off`).html(tbody);
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


