function resetimage(){
    const img = document.getElementById("walks");    
    img.src = "https://swiftmedia.s3.amazonaws.com/mountain.swiftcom.com/images/sites/2/2023/01/17233033/Screenshot-2023-01-21-at-4.44.44-PM-1024x687.png";
    document.getElementById("img_src").innerHTML="swiftmedia";
}
function view(){
    const img = document.getElementById("walks");    
    img.src = "https://upload.wikimedia.org/wikipedia/commons/b/b3/Upper_Provo_River_Utah.jpg";
    document.getElementById("img_src").innerHTML="wikimedia";
}
function showBoth(){
    let content = document.getElementById("stuff");
    content.style.display = content.style.display === "none" ? "block" : "none";
}