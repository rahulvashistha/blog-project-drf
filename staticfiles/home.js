function setStyleSheet(url, classvalue, mode){
  var stylesheet = document.getElementById('stylesheet');
  stylesheet.setAttribute('href', url);
  /*
  if(typeof(Storage)!==undefined){
    console.log(mode)
    window.localStorage.setItem('stylemode', mode)
  }
  else{
    console.log('storage not supported')
  }
  */
  var NavClass = document.getElementById('nav-mode');
  NavClass.setAttribute('class', classvalue);

}

