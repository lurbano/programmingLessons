function lightSequence(leds, {
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
    }, (startTime + i*dt)*1000);
  }
  let endTime = startTime + n *dt + pauseAfter;
  return(endTime);
}

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
