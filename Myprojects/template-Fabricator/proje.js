
        
function ac(){
    document.getElementById("burger-menu").style.width="300px"
}
function kapat(){
    document.getElementById("burger-menu").style.width="0"
}


function ac(){
    document.getElementById("burger-menu").style.width="300px"
}
function kapat(){
    document.getElementById("burger-menu").style.width="0"
}
/**///////////////////*/ 
window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}
/* 
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.display = "block";
    document.getElementById("navbar").style.top = "0px"; 
}
    
else 
{
    document.getElementById("navbar").style.top = "0";
   
    
    
}
prevScrollpos = currentScrollPos;
}
*/