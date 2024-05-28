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

    // Obtener el valor del select gtff
    var inde = document.getElementById("gtff");
    var selectedOption = inde.options[inde.selectedIndex];
    var gtf = parseFloat(selectedOption.getAttribute('data-gtf')) || 0;

    

    // Calcular y actualizar el valor de TMU COSTURA
    var respu = mts * gtf;
    document.getElementById("resultmu").value = respu.toFixed(2); // Mostrar el resultado 
    
}

// Asegúrate de que esta función esté definida y se llame cuando cambie el tipo de máquina
document.getElementById('tipo_maquina').addEventListener('change', actRPM);
document.getElementById('nparadas').addEventListener('input', arranque_parada);
document.getElementById('gtff').addEventListener('change', arranque_parada);

document.getElementById('ppp').addEventListener('input', MTS);
document.getElementById('rpm').addEventListener('input', MTS);