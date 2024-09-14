document.addEventListener('DOMContentLoaded', function() {
  const searchIcon = document.querySelector('#search');
  const inputsearch = document.querySelector('#input_search');
  
    searchIcon.addEventListener('click', function() {
        inputsearch.focus()
    })

});