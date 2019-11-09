/* Coded By FaBiUsKcomp - 2019 
  modificado por jpandolpho - 2019
   Script usado para abrir modais da tela de Participantes
*/

// Recebendo o Modal
var modalUser = document.getElementById("myModalUser");
var modalScore = document.getElementById("myModalScore");

// Botoes para abrir os modais
var btnUser = document.getElementById("btn-user");
var btnScore = document.getElementById("btn-score");


//var body = document.getElementById("body");

// Botoes para fechar os modais
var spanUser = document.getElementsByClassName("close")[0];
var spanScore = document.getElementsByClassName("close")[1];

// Quando o usuário clicar no botao "Adicionar Usuario"
btnUser.onclick = function() {
  modalUser.style.display = "block";
  //body.className += "blur-effect";
}
btnScore.onclick = function() {
  modalScore.style.display = "block";
  //body.className += "blur-effect";
}

// Quando o usuário clicar no botao Fechar do modal "Adicionar Usuario"
spanUser.onclick = function() {
  modalUser.style.display = "none";
  //body.className -= "blur-effect";
}
spanScore.onclick = function() {
  modalScore.style.display = "none";
  //body.className -= "blur-effect";
}

// Quando o usuário clicar em qualquer lugar fora dos modal, serão fechado
window.onclick = function(event) {
  if (event.target == modalUser) {
    modalUser.style.display = "none";
    //body.className -= "blur-effect";
  }
  if (event.target == modalScore) {
    modalScore.style.display = "none";
    //body.className -= "blur-effect";
  }
}