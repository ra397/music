// credit: https://www.w3schools.com/howto/howto_js_filter_lists.asp

function search() {
    const search = document.getElementById('search')
    let cur_search = search.value.toUpperCase()
    let ul = document.getElementById('myUl')
    li = ul.getElementsByTagName('li')

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        p = li[i].getElementsByTagName("p")[0];
        console.log(p)
        txtValue = p.textContent || p.innerText;
        if (txtValue.toUpperCase().indexOf(cur_search) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}