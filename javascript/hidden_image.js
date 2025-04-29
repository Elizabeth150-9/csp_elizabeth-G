function view(){
    const img = document.getElementById("food_color");    
    img.src = "https://handletheheat.com/wp-content/uploads/2013/04/red-velvet-cake-recipe-SQUARE.jpg";
    document.getElementById("img_src").innerHTML="handelttheheat";
}
function resetimage(){
    const img = document.getElementById("food_color");    
    img.src = "https://chefmaster.com/cdn/shop/files/NaturalRedLiqua-GelLiquidFoodColoring7oz.png?v=1699265942";
    document.getElementById("img_src").innerHTML="chefmaster";
}