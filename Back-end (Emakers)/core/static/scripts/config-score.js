/* Esse script serve para configurar os pontos da tela participantes 

 -Copyright -> FaBiUsKcomp
 
 */

var $select = document.getElementById('id_score_specification');
var $fiel = document.getElementById('id_equivalent_score');
var signal = "-";
$fiel.addEventListener('submit', function(evt){
  evt.preventDefault();
  $fiel.value = "-" + $fiel.value;
  console.log($fiel.value)
});

