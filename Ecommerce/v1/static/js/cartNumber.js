document.addEventListener("DOMContentLoaded",()=>{
    let cart_value = document.getElementById("cart_value")
    let subtotal = document.getElementById("subtotal")
    let total = document.getElementById("total")
    let popupTotal = document.getElementById("popupTotal")
    fetch(`/v1/cartNumber`)
    .then(response => response.json())
    .then(data => {
        
        number = data['number']
        subtotalValue = data['subtotal']
        console.log(subtotal)
        cart_value.innerHTML=number
        subtotal.innerHTML=`$${subtotalValue}`
        total.innerHTML=`$${3+parseFloat(subtotalValue)}`
        popupTotal.innerHTML=`$${3+parseFloat(subtotalValue)}`
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    document.getElementById("confirm").addEventListener("click",()=>{
        document.getElementById('confirmPopup').style.display = 'block';
    })

    document.querySelector('.close').onclick = function() {
        document.getElementById('confirmPopup').style.display = 'none';
    };
    
    document.getElementById('confirmPurchase').onclick = function() {
        // Add your purchase confirmation logic here
        fetch("/v1/confirmPurchase")
        .then(response => response.json())
        .then(data=>{
            document.getElementById('confirmPopup').style.display = 'none';
            console.log(data)
            window.location.href="/v1/cart"
        })
        .catch((error)=>{
            console.log("error",error)
        })

    };
    
});
