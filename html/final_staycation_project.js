function resetimage(){
    let img = document.getElementById("snow");
    img.onmouseover = () => img.src = "https://scene7.vailresorts.com/is/image/vailresorts/20220302_PC_Markewitz_089?wid=4000&resMode=sharp2&w=4000&h=2666&fit=constrain,1&dpr=on,2.625";
    img.onmouseout = () => img.src = "https://upload.wikimedia.org/wikipedia/commons/8/84/Ski_Famille_-_Family_Ski_Holidays.jpg";
    }
    function showButton(){
    const content = document.getElementById("button");
    if (content.style.display === "none") {
        content.style.display = "block";
    }else{
        content.style.display = "none";
        }
    }