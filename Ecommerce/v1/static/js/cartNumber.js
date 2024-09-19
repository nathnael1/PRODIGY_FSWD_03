document.addEventListener("DOMContentLoaded",()=>{
    let cart_value = document.getElementById("cart_value")
    let subtotal = document.getElementById("subtotal")
    let total = document.getElementById("total")
    fetch(`/v1/cartNumber`)
    .then(response => response.json())
    .then(data => {
        
        number = data['number']
        subtotalValue = data['subtotal']
        console.log(subtotal)
        cart_value.innerHTML=number
        subtotal.innerHTML=`$${subtotalValue}`
        total.innerHTML=`$${3+parseFloat(subtotalValue)}`
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    
});
