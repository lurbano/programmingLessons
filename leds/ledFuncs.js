function lightSequence(leds, {
                        startLight=0,
                        n=20,
                        color="red",
                        dt=0.1,
                        startTime=0,
                        step=1,
                        pauseAfter=0.25
                      } = {}) {

  for (let i=startLight; i<n; i+=step){
    setTimeout( function() {
      leds[i].style.backgroundColor = color;
    }, (startTime + (i-startLight)*dt)*1000);
  }
  let endTime = startTime + (n-startLight) *dt + pauseAfter;
  return(endTime);
}

// function lastLights(leds, {
//                         n=20,
//                         color="red",
//                         dt=0.1,
//                         startTime=0,
//                         step=1,
//                         pauseAfter=0.25
//                       } = {}) {
//
//   let
//   let args = arguments[1];
//   args['startLight'] = 20-n;
//   console.log(args);
//   let endTime = lightSequence(leds, args)
//   return(endTime);
// }

function lightBackwards(leds, {
                        n=20,
                        color="red",
                        dt=0.1,
                        startTime=0,
                        step=1,
                        pauseAfter=0.25
                      } = {}) {

  for (let i=0; i<n; i+=step){
    setTimeout( function() {
      leds[i].style.backgroundColor = color;
    }, (startTime + (n-1-i)*dt)*1000);
  }
  let endTime = startTime + n *dt + pauseAfter;
  return(endTime);
}

function clearLeds(leds, {
                            startTime=0,
                            n = 20,
                            pauseAfter=0.25
                          } = {}) {
  setTimeout( function() {
    for (let i=0; i<n; i++){
      leds[i].style.backgroundColor = "black";
    }
  }, startTime*1000);
  let endTime = startTime + pauseAfter;

  return (endTime);
}

function complementaryColors(color=[255,0,0], maxVal= 10){
  let scaleFactor = 255/maxVal;
  let r = color[0] * scaleFactor;
  let g = color[1] * scaleFactor;
  let b = color[2] * scaleFactor;
  let rc = (maxVal - color[0]) * scaleFactor;
  let gc = (maxVal - color[1]) * scaleFactor;
  let bc = (maxVal - color[2]) * scaleFactor;
  return [`rgb(${r}, ${g}, ${b})`, `rgb(${rc}, ${gc}, ${bc})`]
}
