const pagos = [];
const nombres = [];
const lista = document.getElementById("lista");
const usuario = document.getElementById("nombre");
const pago = document.getElementById("monto");
const resultado = document.getElementById("total")

function repartir(){
    agregarGastos();
    ultimo();
    mostrarIndividual();
}

function agregarGastos(){
    nombres.push(usuario.value);
    pagos.push(pago.value);
}

function ultimo(){
    const li = document.createElement("li");
    const text = document.createTextNode(`${usuario.value} Gastó: $${pago.value}`);
    li.classList.add("list-group-item");
    li.appendChild(text);
    lista.appendChild(li);
}

function suma(){
    let suma=0;
    for(let pago of pagos){
        suma+=parseInt(pago);
    }
    return suma;
}

function mostrarIndividual(){
    const total = suma(pagos);
    const promedio = total/nombres.length;
    resultado.innerText = `Total: $${total}. A cada uno le tocaria pagar: $${promedio}`
    

}