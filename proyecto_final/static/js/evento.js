$("#agregar_evento").on("click", function() {

    $("#addevent").modal("show");

  });


  $("#cancel").on("click", function() {

    $("#add_artist").modal("toggle");
    $('#nombre').val('')
    $('#apellidos').val('')
    $('#ci').val('')
    $('#grupo').val('')
    $('#sexo').val('')

  });

  var boton_save=document.getElementById('save');
  var lista=document.getElementById('tabla');
  var data=[];
  var cont=0;
  boton_save.addEventListener("click", save);
  function save(){
    var nombre=document.getElementById('nombre').value;
    var apellidos=document.getElementById('apellidos').value;
    var ci=document.getElementById('ci').value;
    var grupo=document.getElementById('grupo').value;
    var sexo=document.getElementById('sexo').value;
    //agregar elementos al arreglo data
    data.push(
        {
         "id":cont,
         "nombre":nombre,
         "apellidos":apellidos,
         "ci":ci,
         "grupo":grupo,
         "sexo":sexo,
        }
    );
    var id_row='row'+cont;
    var fila='<tr id='+id_row+'><td>'+nombre+'</td><td>'+apellidos+'</td><td>'+ci+'</td><td>'+grupo+'</td><td>'+sexo+'</td><td><a href="#" class="btn btn-danger" onclick="eliminar('+cont+')";>Eliminar</a></td></tr>';
    //agregar a la tabla
    $("#tabla").append(fila);
    $('#nombre').val('')
    $('#apellidos').val('')
    $('#ci').val('')
    $('#grupo').val('')
    $('#sexo').val('')
    cont++;
    $("#add_artist").modal("toggle");



  }
  function eliminar(row){
    $("#dlt_artist").modal("show");

    deleteButton = document.getElementById('#btn-delete');
  deleteButton.onclick = function(){

  if(deleteButton.onclick){
    return function(){
      $("#row"+row).remove();
    var i=0;
    var pos=0;
    for (x of data){
        if(x.id==row){
            pos=i;
        }
        i++;
    }
    data.splice(pos,1);
    }
  }else
  cancelButton = document.getElementById('#dlt_cancel');
  cancelButton.onclick = function(){
    if(cancelButton.onclick){
     return function(){
      $("#dlt_obra").modal("hide");
    }
  }
  }

  }
  }