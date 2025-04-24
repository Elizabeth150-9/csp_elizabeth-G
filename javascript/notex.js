// JavaScript - JS

function show(){
    document.getElementById("patric").style.display = "block"
}

function hello(){
    let name = prompt("What is your name?", "Koro Sensei")
    document.getElementById("title").innerHTML = "Hello" + name + "!"
        
}
        
function enter(){
    document.getElementById("btn").style.color = "white"
    document.getElementById("btn").style.backgroundColor = "green"
}
function down(){
    document.getElementById("btn").style.backgroundColor = "red"
}
function out(){
    document.getElementById("btn").style.backgroundColor = "black"
    document.getElementById("btn").style.backgroundColor = "lightgrey"
}
let images = ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/1200px-Cat_November_2010-1a.jpg", "https://media.tenor.com/-_bYOZ_6NZcAAAAM/shrek.gif"]
let counter = 0

function change(){
    if(counter < images.length){
        document.getElementById("image").src = images
        [counter]
        counter += 1
    }else{
        counter = 0
        document.getElementById("image").src = images
        [counter]
    }

}

function popup(){
    window.prompt("Don't click this. Really!")
}
    