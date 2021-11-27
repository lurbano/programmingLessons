// a class to deal with cylinders
class cylinder{

  constructor(r, h) {
    this.r = r;
    this.h = h;
  }

  // method for calculating the volume of the cylinder
  volume(){
    let v = Math.PI * this.r**2 * this.h;
    return v;
  }

}

// Function to calculate the volume of a cylinder
function volCylinder(){
  // Get input from webpage
  let r = document.getElementById("r").value;
  let h = document.getElementById("h").value;
  let u = document.getElementById("units").value;

  // do CALCULATIONS USING THE CYLINDER CLASS
  let c = new cylinder(r, h);
  let vol = c.volume()

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
