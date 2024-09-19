document.addEventListener("DOMContentLoaded",()=>{
let cart = document.getElementsByClassName("card_cart")
let cart_value = document.getElementById("cart_value")
let del = document.getElementsByClassName("del")
Array.from(cart).forEach(item => {
    item.addEventListener("click", () => {
        let id = item.querySelector('p').dataset.id;
        console.log(id);
        fetch(`/v1/addCart/${id}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: id })
        })
        .then(response => response.json())
        .then(data => {

            number = data['number']
            item.classList.add("muted");
            item.disabled = true;
            
            cart_value.innerHTML=number
            
        })
        .catch((error) => {
            console.error('Error:', error);
        });
       
    });
});
Array.from(del).forEach(item => {
    item.addEventListener("click", () => {
        let id = item.dataset.id;
        console.log(id);
        fetch(`/v1/deleteCart/${id}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: id })
        })
        .then(response => response.json())
        .then(data => {
            
            window.location.href= "/v1/cart"
            
        })
        .catch((error) => {
            console.error('Error:', error);
        });
       
    });
});

});//end of domcontentloaded