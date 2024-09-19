document.addEventListener("DOMContentLoaded", () => {
    let alltab = document.getElementById("alltab");
    let clothestab = document.getElementById("clothestab");
    let electronicstab = document.getElementById("electronicstab");
    let furniturestab = document.getElementById("furniturestab");
    let all = document.getElementById("all");
    let clothes = document.getElementById("clothes");
    let electronics = document.getElementById("electronics");
    let furniture = document.getElementById("furniture");
    alltab.classList.add("active");
    alltab.addEventListener("click", () => {
      alltab.classList.add("active");
      clothestab.classList.remove("active");
      electronicstab.classList.remove("active");
      furniturestab.classList.remove("active");
      all.classList.remove("disabled");
      clothes.classList.add("disabled");
      electronics.classList.add("disabled");
      furniture.classList.add("disabled");
    });
  
    clothestab.addEventListener("click", () => {
      alltab.classList.remove("active");
      clothestab.classList.add("active");
      electronicstab.classList.remove("active");
      furniturestab.classList.remove("active");
      all.classList.add("disabled");
      clothes.classList.remove("disabled");
      electronics.classList.add("disabled");
      furniture.classList.add("disabled");
    });
  
    electronicstab.addEventListener("click", () => {
      alltab.classList.remove("active");
      clothestab.classList.remove("active");
      electronicstab.classList.add("active");
      furniturestab.classList.remove("active");
      all.classList.add("disabled");
      clothes.classList.add("disabled");
      electronics.classList.remove("disabled");
      furniture.classList.add("disabled");
    });
  
    furniturestab.addEventListener("click", () => {
      alltab.classList.remove("active");
      clothestab.classList.remove("active");
      electronicstab.classList.remove("active");
      furniturestab.classList.add("active");
      all.classList.add("disabled");
      clothes.classList.add("disabled");
      electronics.classList.add("disabled");
      furniture.classList.remove("disabled");
    });
  });