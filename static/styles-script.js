var path   = "css";
var style   = document.createElement( 'link' );
style.rel   = 'stylesheet';
style.type  = 'text/css';
style.href  = './static/styles.css';
document.getElementsByTagName( 'head' )[0].appendChild( style );