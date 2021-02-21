// author = 'danish-wani'


function filterBy(){
    document.getElementById('filterBy-form').submit()
}

var elements = document.getElementsByClassName("pagination-link");

var category = document.getElementById("category-dropdown").value ;

Array.from(elements).forEach(function(element) {
  element.setAttribute("href", element.getAttribute("href") + "&category="+category);
});
