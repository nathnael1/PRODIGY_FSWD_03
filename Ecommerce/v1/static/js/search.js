let searchicon = document.getElementById("searchicon");
searchicon.addEventListener("click", () => {
    let search = document.getElementById("input_search").value;
    let searchInput = document.getElementById("searchInput");
    searchInput.value = search;
    console.log(search, searchInput.value); // Debugging line to check values
    let searchForm = document.getElementById("searchForm");
    searchForm.submit();
});