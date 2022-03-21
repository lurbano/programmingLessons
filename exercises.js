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

function getLEDs(){
  //add element above
  let targetDiv = document.createElement("div");
  let scriptElement = document.currentScript;
  let parentElement = scriptElement.parentNode;
  parentElement.insertBefore(targetDiv, scriptElement);

  var leds = []
  for (let i = 0; i <= 20; i++){
    leds.push(document.createElement("SPAN"));
    leds[i].classList.add("led");
    targetDiv.append(leds[i]);
  }
  return leds;
}
