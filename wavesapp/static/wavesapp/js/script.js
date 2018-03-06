
var currntUrl = window.location.href;
var i = 0;
var images = [];
var time = 2000;

    console.log(currntUrl);
  var targetUrl = "http://127.0.0.1:8000/signup/";
    if (currntUrl===targetUrl) {
      var btnLink = document.getElementsByClassName('navbarbrand');
      btnLink.style.visibility = "hidden";
      console.log("in condition");
    }
images[0] = "{{ image.image.url }}";
function changeImg() {
  document.slide.source = images[i];
  if (i < images.length - 1){
    i++;
  }else{
    i = 0;
  }
  setTimeout("changeImg()",time);
}
window.onload = changeImg;
