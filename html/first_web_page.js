function view(){
    const img = document.getElementById("walks");    
    img.src = "https://upload.wikimedia.org/wikipedia/commons/b/b3/Upper_Provo_River_Utah.jpg";
    document.getElementById("img_src").innerHTML="wikimedia";
}

function resetimage(){
    const img = document.getElementById("walks");    
    img.src = "https://swiftmedia.s3.amazonaws.com/mountain.swiftcom.com/images/sites/2/2023/01/17233033/Screenshot-2023-01-21-at-4.44.44-PM-1024x687.png";
    document.getElementById("img_src").innerHTML="swiftmedia";
}

function showHide(){
    let show = document.getElementById("showHide")
    if(show.style.display == "block"){
    show.style.display = "none"
    if(document.getElementById("hover").style.display = "show"){
        document.getElementById("spotify").style.display = "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/ea/e0/66/eae0669b-8c6b-45cc-d1da-32c7dd5ecf50/AppIcon-0-0-1x_U007emarketing-0-7-0-0-85-220.png/1200x630wa.png"
        document.getElementById("shw").style.display = "show"
    }else{
        document.getElementById("hide").style.display = "none"
         show.style.display = "block"
    }
    }
}