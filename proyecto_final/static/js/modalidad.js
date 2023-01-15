$("#agregar_modalidad").on("click", function() {

    $("#addmodality").modal("show");

  });

  $("#cancel").on("click", function() {

    $("#addmodality").modal("toggle");
    $('#nombre_modalidad').val('')

  });

  var boton_save=document.getElementById('save');
  var lista=document.getElementById('tabla');
  var data=[];
  var cont=0;
  boton_save.addEventListener("click", save);
  function save(){
    var nombre=document.getElementById('nombre_modalidad').value;
    //agregar elementos al arreglo data
    data.push(
        {
         "id":cont,
         "nombre_modalidad":nombre_modalidad,
        }
    );
    var id_row='row'+cont;
    var fila='<tr id='+id_row+'><td>'+nombre_modalidad+'</td><td><a href="#" class="btn btn-danger" id="dlt_modality" onclick="eliminar('+cont+')";>Eliminar</a></td></tr>';
    //agregar a la tabla
    $("#tabla").append(fila);
    $('#nombre_modalidad').val('')
    cont++;
    $("#addmodality").modal("toggle");



  }
  function eliminar(row){
    $("#dlt_modality").modal("show");

    deleteButton = document.getElementById('#btn_delete');
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
  cancelButton = document.getElementById('#cancel');
  cancelButton.onclick = function(){
    if(cancelButton.onclick){
     return function(){
      $("#dlt_modality").modal("hide");
    }
  }
  }

  }
  }
