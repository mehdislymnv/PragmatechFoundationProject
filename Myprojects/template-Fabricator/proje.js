
        
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



window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 150) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
}