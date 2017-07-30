/**
 * @Author: Will Scott <willscottuk>
 * @Date:   30/07/2017 10:20
 * @Project: Ambassadr Home Automation
 * @Last modified by:   willscottuk
 * @Last modified time: 30/07/2017 10:21
 */



$('document').ready(function(){
  setInterval("imgSwap()",120000);
});  

function imgSwap(){
  $('body').css("background-image", "url('https://home.ambassadr.io/local/london_live.jpg?rand=" + Math.random() + "')").fadeIn(slow);
}
