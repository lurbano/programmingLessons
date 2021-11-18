// Function to calculate the volume of a cylinder
function volCylinder(){
  // Get input from webpage
  let r = document.getElementById("r").value;
  let h = document.getElementById("h").value;
  let u = document.getElementById("units").value;

  // do calculations
  let vol = Math.PI * r**2 * h;

  // output to webage
  let vOut = document.getElementById("volume");
  vUnits = " " + u + "<sup>3</sup>";
  vOut.innerHTML = vol + vUnits;

}

// call function/s when page loads
volCylinder();

//   add event listeners to run function whenever a change
// is made to one of the inputs
rInput = document.getElementById("r");
rInput.addEventListener("change", volCylinder);

hInput = document.getElementById("h");
hInput.addEventListener("change", volCylinder);

uInput = document.getElementById("units");
uInput.addEventListener("input", volCylinder);
