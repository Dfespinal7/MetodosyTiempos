function actRPM(){
    var tipoMaquina=document.getElementById('tipo_maquina');
    var selectedOption = tipoMaquina.options[tipoMaquina.selectedIndex];
    var rpm = selectedOption.getAttribute('data-rpm');
    var ppp=selectedOption.getAttribute('data-ppp');
    document.getElementById('rpm').value = rpm;
    
    
        document.getElementById('rpm').value = rpm;
        console.log(rpm);
        var div = parseFloat(rpm) / 1000;
        document.getElementById("fhsf").value = div; 
    
        MTS();
    
}
function actcodOp(){
    var codigo=document.getElementById("operacion")
    var seleccion=codigo.options[codigo.selectedIndex]
    var cod=seleccion.getAttribute('data-cod')
    codigo_op.value=cod
}
function MTS(){
    var ppp = parseInt(document.getElementById('ppp').value)||0
    var rpm = parseInt(document.getElementById('rpm').value)||0
    var consta = parseFloat(document.getElementById('consta').value)||1

    var div=rpm*consta
   
   var multi=ppp/div
   document.getElementById('resulmt').value = multi.toFixed(2);
   arranque_parada();
}

function arranque_parada(){
    var valor1=parseInt(document.getElementById("nparadas").value)||0
    var valor2=valor1*17
    document.getElementById("parada_arranque").value=valor2

    var mts = parseFloat(document.getElementById("resulmt").value) || 0;

    
    var inde = document.getElementById("gtff");
    var selectedOption = inde.options[inde.selectedIndex];
    var gtf = parseFloat(selectedOption.getAttribute('data-gtf')) || 0;
    var los=parseFloat(document.getElementById("dista").value)||0
    var hsf=parseFloat(document.getElementById("fhsf").value)||0
    var parada=document.getElementById("parad")
    var seleccion=parada.options[parada.selectedIndex]
    var p=parseFloat(seleccion.getAttribute("data-parada"))||0

    

    
    var respu = (mts * gtf * los *hsf)+valor2+p
    document.getElementById("resultmu").value = respu.toFixed(2); 
    
}

// Asegúrate de que esta función esté definida y se llame cuando cambie el tipo de máquina
document.getElementById('tipo_maquina').addEventListener('change', actRPM);
document.getElementById('nparadas').addEventListener('input', arranque_parada);
document.getElementById('gtff').addEventListener('change', arranque_parada);

document.getElementById('ppp').addEventListener('input', MTS);
document.getElementById('rpm').addEventListener('input', MTS);
document.getElementById('parad').addEventListener('change', arranque_parada);



function agregarFila() {
    const tabla = document.getElementById('movimientosBody');
    const nuevafila = document.createElement('tr');
    
    nuevafila.innerHTML = `
        <td><input type="text" name="numero[]" class="short-input"></td>
        <td><input type="text" name="codigo[]" class="short-input"></td>
        <td><input type="text" name="movimiento[]" class="short-input"></td>
        <td><input type="text" name="frecuencia[]" class="short-input"></td>
        <td><input type="text" name="distancia[]" class="short-input"></td>
        <td><input type="number" name="tmu[]" class="short-input"></td>
        <td><input type="text" name="total_tmu[]" class="short-input"></td>
        <td><input type="text" name="tiempo_sam[]" class="short-input"></td>
        <td><button type="button" class="btn btn-danger" onclick="eliminarFila(this)">Eliminar</button></td>
    `;
    
    tabla.appendChild(nuevafila);
}
function eliminarFila(button) {
    const fila = button.parentNode.parentNode;
    fila.parentNode.removeChild(fila);
}