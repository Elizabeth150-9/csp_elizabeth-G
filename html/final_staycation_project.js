function view(){
    const img = document.getElementById("snow");    
    img.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQa8GW-TkBiOEKKrJlRkyXwkmaLCg6da27PQg&s";
    document.getElementById("img_src").innerHTML="encrypted-tbno";
}
function resetimage(){
    const img = document.getElementById("snow");
    img.src = "https://scene7.vailresorts.com/is/image/vailresorts/20220302_PC_Markewitz_089?wid=4000&resMode=sharp2&w=4000&h=2666&fit=constrain,1&dpr=on,2.625";
    document.getElementById("img_src").innerHTML="scene7";
}
function showBoth() {
    let content = document.getElementById("stuff");
    content.style.display = content.style.display === "none" ? "block" : "none";
}