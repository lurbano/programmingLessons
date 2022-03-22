$(".toggle-next").click(function(){
  $(this).next().toggle();
  if ($(this).next().is(":visible")){
    $(this).parent().css("border", "1px solid red");
    let txt = $(this).html().replace("Show", "Hide").replace("▼", "▲");
    $(this).html(txt);
  }
  else {
    $(this).parent().css("border", "1px solid black");
    let txt = $(this).html().replace("Hide", "Show").replace("▲", "▼");
    $(this).html(txt);
  }
})

function getLEDs(nPix=20){
  //add element above
  let targetDiv = document.createElement("div");
  targetDiv.classList.add("ledStrip");
  let scriptElement = document.currentScript;
  let parentElement = scriptElement.parentNode;
  parentElement.insertBefore(targetDiv, scriptElement);

  var leds = []
  for (let i = 0; i < nPix; i++){
    leds.push(document.createElement("div"));
    leds[i].classList.add("led");
    targetDiv.append(leds[i]);
  }
  return leds;
}

function getLedSiblingFromButton(elem){
  let sibling = elem.nextElementSibling;
  while (sibling) {
    if (sibling.matches(".ledStrip")) return sibling;
		sibling = sibling.nextElementSibling
	}
  return undefined; //if not found
}

function animateLEDs( f){
  elem = document.activeElement;
  let targetDiv = getLedSiblingFromButton(document.activeElement);
  targetDiv.innerHTML = '';

  var leds = []
  for (let i = 0; i < nPix; i++){
    leds.push(document.createElement("div"));
    leds[i].classList.add("led");
    targetDiv.append(leds[i]);
  }
  f(leds);

}

function resetLEDs(){
  let targetDiv = getLedSiblingFromButton(document.activeElement);
  targetDiv.innerHTML = '';

  var leds = []
  for (let i = 0; i < nPix; i++){
    leds.push(document.createElement("div"));
    leds[i].classList.add("led");
    targetDiv.append(leds[i]);
  }

  // for (let i=0; i<leds.length; i+=2){
  //   leds[i].style.backgroundColor = 'black';
  // }
}
