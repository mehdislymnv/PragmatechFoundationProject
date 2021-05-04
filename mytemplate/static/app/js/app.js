
var modal = document.getElementById("myModal");
console.log(modal);

var btn = document.getElementById("myBtn");
console.log(myBtn);


var span = document.getElementsByClassName("close")[0];
console.log(span);

btn.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
