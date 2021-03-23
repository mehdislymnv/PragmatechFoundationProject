
        
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
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "100px";} 
else {
    document.getElementById("navbar").style.top = "0";
}
prevScrollpos = currentScrollPos;
}
