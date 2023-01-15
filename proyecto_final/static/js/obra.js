$("#agregar_obra").on("click", function() {

    $("#add_obra").modal("show");
  
  });

  $("#cancel").on("click", function() {

    $("#add_obra").modal("toggle");
    $('#nombre').val('')
    $('#genero').val('')
    $('#duracion').val('')
    $('#autor').val('')  
  
  });

  var boton_save=document.getElementById('bt_save');
  var lista=document.getElementById('tabla');
  var data=[];
  var cont=0;
  boton_save.addEventListener("click", save);
  function save(){
    var nombre=document.getElementById('nombre').value;
    var genero=document.getElementById('genero').value;
    var duracion=document.getElementById('duracion').value;
    var autor=document.getElementById('autor').value;
    //agregar elementos al arreglo data
    data.push(
        {
         "id":cont,
         "nombre":nombre,
         "genero":genero,
         "duracion":duracion,
         "autor":autor,
        }
    );
    var id_row='row'+cont;
    var fila='<tr id='+id_row+'><td>'+nombre+'</td><td>'+genero+'</td><td>'+duracion+'</td><td>'+autor+'</td><td><a href="#" class="btn btn-danger" onclick="eliminar('+cont+')";>Eliminar</a></td></tr>';
    //agregar a la tabla
    $("#tabla").append(fila);
    $('#nombre').val('')
    $('#genero').val('')
    $('#duracion').val('')
    $('#autor').val('')
    cont++;
    $("#add_obra").modal("toggle");
    


  }
  function eliminar(row){
    $("#dlt_obra").modal("show");

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
  cancelButton = document.getElementById('#cancel');
  cancelButton.onclick = function(){
    if(cancelButton.onclick){
     return function(){
      $("#dlt_obra").modal("hide");
    } 
  }
  }
  
  }
  }
 
  