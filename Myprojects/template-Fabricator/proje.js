/**
 * 
let menuover=document.querySelectorAll(".header-nav-buton ul  li a");
let overmenu=document.querySelector(".overmenu");

for (let i=0; i<menuover.length; i++ ){
  menuover[i].addEventListener('mouseover',function(){
    overmenu=document.querySelector(".overmenu");

    overmenu.className += ' overd'
  
  })
  
}

console.log(menuover);
 */




function ac(){
    document.getElementById("burger-menu").style.width="300px"
} 
function kapat(){
    document.getElementById("burger-menu").style.width="0"
}






/**///////////////////*/



///////////////////////





window.onscroll = function() {myFunction()};
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 150) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
}
/* logo */


let logintag=document.querySelector("#login");
console.log(logintag);

let loginbuton = document.querySelector(".header-info-container-icon span");


loginbuton.addEventListener("click",loginac);

function loginac(){
  logintag.style.display = "block";
  
  
  

}
function lgbaqla(){
  logintag.style.display = "none";
 
}