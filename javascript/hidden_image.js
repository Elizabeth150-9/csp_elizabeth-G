function view(){
    const img = document.getElementById("cake");    
    img.src = "https://upload.wikimedia.org/wikipedia/commons/b/b3/Upper_Provo_River_Utah.jpg";
    document.getElementById("img_src").innerHTML="wikimedia";
}
function view(){
    if(document.getElementById("button").style.display === "block"){
        document.getElementById("cake").style.display = "none"
    }else{
        document.getElementById("button").style.display = "block"
    } 
}