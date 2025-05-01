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
function see(){
    img.src = "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/ea/e0/66/eae0669b-8c6b-45cc-d1da-32c7dd5ecf50/AppIcon-0-0-1x_U007emarketing-0-7-0-0-85-220.png/1200x630wa.png"
    if(document.getElementById("button").style.display === "see"){
        document.getElementById("button").style.display = "none"
    }else{
        document.getElementById("button").style.display = "see"
    } 
}