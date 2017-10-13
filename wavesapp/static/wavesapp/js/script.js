
var currntUrl = window.location.href;

    console.log(currntUrl);
  var targetUrl = "http://127.0.0.1:8000/signup/";
    if (currntUrl===targetUrl) {
      var btnLink = document.getElementsByClassName('navbarbrand');
      btnLink.style.visibility = "hidden";
      console.log("in condition");
    }
