// Function to generate a random number between min and max (inclusive)
function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;// we can do it like this : Math.floor(Math.random() * 11)
  }

  // Function to validate the number input
  function getValidNumberInput() {
    while (true) {
      const userInput = Number(prompt("Enter a number between 0 and 10:"));
  
      if (isNaN(userInput)) {
        alert("Sorry, not a number. Try again.");
      } else if (userInput < 0 || userInput > 10) {
        alert("Sorry, it's not a good number. Try again.");
      } else {
        return userInput;
      }
    }
  }
  
  // Function to compare the user's number with the computer's number
  function compareNumbers(userNumber, computerNumber) {
    let counter = 0;
  
    while (counter < 3) {
      if (userNumber === computerNumber) {
        alert("WINNER");
        return; // Stop the game
      }
  
      if (userNumber > computerNumber) {
        alert("Your number is bigger than the computer’s, guess again");
      } else {
        alert("Your number is smaller than the computer’s, guess again");
      }
  
      counter++;
      userNumber = getValidNumberInput();
    }
  
    alert("Out of chances");
  }
   
  // Function to play the guessing game
  function playTheGame() {
    const playGame = confirm("Would you like to play the game?");
  
    if (!playGame) {
      alert("No problem, Goodbye.");
    } else {
      const userNumber = getValidNumberInput();
  
      const computerNumber = getRandomNumber(0, 10);
      compareNumbers(userNumber, computerNumber);
    }
  }
  
  // Call the playTheGame function when the button is clicked
  function handleClick() {
    playTheGame();
  }
  