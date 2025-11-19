let taches=document.querySelectorAll(".sup");
taches.forEach(link =>{
link.addEventListener("click" ,function(event){
    const c= confirm("vous voulez vraiment le supprimer");
    if(c==false){
        event.preventDefault();
    }
})})

// Filtre de recherche en direct
let search = document.querySelector("#search");
let taches_li = document.querySelectorAll("#taches li");

search.addEventListener("input", function(){
    const ser = search.value.toLowerCase();

    taches_li.forEach(item => {
        const text = item.innerText.toLowerCase();
        if (text.includes(ser)) {
            item.style.display = "";
        } else {
            item.style.display = "none";
        }
    });
});



