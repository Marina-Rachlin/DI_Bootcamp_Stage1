function singSong() {
    let numBottles = Number(prompt("Enter the number of bottles to start with:"));
  
    if (isNaN(numBottles) || numBottles < 0) {
      alert("Invalid input. Please enter a positive number.");
      return;
    }
  
    let counter = 1; // Counter for the number of bottles to drop
  
    while (numBottles > 0) {
      console.log(numBottles + " bottles of beer on the wall");
      console.log(numBottles + " bottles of beer");
  
      let bottlesToDrop = Math.min(numBottles, counter); // Number of bottles to drop in this iteration
  
      console.log("Take " + bottlesToDrop + " down, pass " + (bottlesToDrop === 1 ? "it" : "them") + " around");
  
      numBottles -= bottlesToDrop; // Update the number of bottles left
  
      if (numBottles === 0) {
        console.log("No more bottles of beer on the wall\n");
      } else if (numBottles === 1) {
        console.log(numBottles + " bottle of beer on the wall\n");
      } else {
        console.log(numBottles + " bottles of beer on the wall\n");
      }
  
      counter++; // Increase the counter for the next iteration
    }
  }
  