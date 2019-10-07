/* Esse script serve para adicionar dia, semana, ano e hora em uma pagina html 

 -Copyright -> FaBiUsKcomp
 
 */


let $lineWeek = document.getElementById('week');
let $lineYear = document.getElementById('year');
let $lineHour = document.getElementById('hour');

let getWeekDay = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"];
let getMonthSig = ["Jan","Fev", "Mar","Abr", "Mai","Jun", "Jul", "Ago","Set","Out","Nov","Dez"];

function hourAuto() {

    info = new Date();

    let y = info.getFullYear();
    let d = info.getDate();
    let w = (info.getDay()).toString(); //Retorna o dia da semana em int
    let m = (info.getMonth()).toString(); //Retorna o mes do Ano em int
    let h = info.getHours();
    let min = info.getMinutes();

    let week = getWeekDay[w];
    let month = getMonthSig[m];

    if(min < 10){ min = "0"+min; }
    if(d < 10){ d = "0"+d; }
    if(h < 10){ h = "0"+h; }

    $lineWeek.textContent = week + ", " + d + " " + month;
    $lineYear.textContent = y;
    $lineHour.textContent = h + ":" + min;
}

console.log(getWeekDay.length);

setInterval(hourAuto, 1000);

//  Conferir ------------------> https://ntp.br/