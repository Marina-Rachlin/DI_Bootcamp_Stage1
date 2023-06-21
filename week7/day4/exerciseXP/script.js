// 🌟 Exercise 1 : Find The Numbers Divisible By 23
// Instructions
// Create a function call displayNumbersDivisible() that takes no parameter.

// In the function, loop through numbers 0 to 500.

// Console.log all the numbers divisible by 23.

// At the end, console.log the sum of all numbers that are divisible by 23.

// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 
// 368 391 414 437 460 483
// Sum : 5313


function displayNumbersDivisible(){
    let sum = 0;
    for (let i = 0; i <= 500; i++){
        if(i%23==0){
            console.log(i);
            sum += i;
        }
    }
    console.log("Sum:", sum);
}

displayNumbersDivisible();

// Bonus: Add a parameter divisor to the function.

// displayNumbersDivisible(divisor)

// Example:
// displayNumbersDivisible(3) : Console.log all the numbers divisible by 3, 
// and their sum
// displayNumbersDivisible(45) : Console.log all the numbers divisible by 45, 
// and their sum

function displayNumbersDivisible(divisor){
    let sum = 0;
    for ( let i = 0; i<= 500; i++){
        if(i%divisor==0){
            console.log(i);
            sum += i;
        }
    }
    console.log(sum)
}

displayNumbersDivisible(25);

// 🌟 Exercise 2 : Shopping List
// Instructions
// Add the stock and prices objects to your js file.
// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.

// Create a function called myBill() that takes no parameters.

// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.

// Call the myBill() function.

// Bonus: If the item is in stock, decrease the item’s stock by 1


const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

const shoppingList = ["banana", "orange", "apple"];
function myBill(){
    let total = 0;
    for (let i = 0; i<=shoppingList.length; i++){
        const item = shoppingList[i]
        if (item in stock && stock[item] > 0) {
            total += prices[item];
            stock[item] -= 1; // Decrease the item's stock by 1
          }
        }
      
        return total;
      }

const totalPrice = myBill();
console.log("Total Price:", totalPrice);
console.log("Updated Stock:");

for (const item in stock) {
  console.log(item + ": " + stock[item]);
}


// Exercise 3 : What’s In My Wallet ?
// Instructions
// Note: Read the illustration (point 4), while reading the instructions

// Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
// an item price
// and an array representing the amount of change in your pocket.

// In the function, determine whether or not you can afford the item.
// If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
// If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false

// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// A quarters is 0.25
// A dimes is 0.10
// A nickel is 0.05
// A penny is 0.01


// 4. To illustrate:

// After you created the function, invoke it like this:

// changeEnough(4.25, [25, 20, 5, 0])
// The value 4.25 represents the item’s price
// The array [25, 20, 5, 0] represents 25 quarters, 20 dimes, 5 nickels and 0 pennies.
// The function should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)


// Examples

// changeEnough(14.11, [2,100,0,0]) => returns false
// changeEnough(0.75, [0,0,20,5]) => returns true

function changeEnough(itemPrice, amountOfChange) {
    const quartersValue = 0.25;
    const dimesValue = 0.10;
    const nickelsValue = 0.05;
    const penniesValue = 0.01;
  
    const totalChange = amountOfChange[0] * quartersValue +
                        amountOfChange[1] * dimesValue +
                        amountOfChange[2] * nickelsValue +
                        amountOfChange[3] * penniesValue;
  
    return totalChange >= itemPrice;
  }
  
  console.log(changeEnough(4.25, [25, 20, 5, 0])); // true
  console.log(changeEnough(14.11, [2, 100, 0, 0])); // false
  console.log(changeEnough(0.75, [0, 0, 20, 5])); // true


//   🌟 Exercise 4 : Vacations Costs
//   Instructions
//   Let’s create functions that calculate your vacation’s costs:
  
//   Define a function called hotelCost().
//   It should ask the user for the number of nights they would like to stay in the hotel.
//   If the user doesn’t answer or if the answer is not a number, ask again.
//   The hotel costs $140 per night. The function should return the total price of the hotel.
  
//   Define a function called planeRideCost().
//   It should ask the user for their destination.
//   If the user doesn’t answer or if the answer is not a string, ask again.
//   The function should return a different price depending on the location.
//   “London”: 183$
//   “Paris” : 220$
//   All other destination : 300$
  
//   Define a function called rentalCarCost().
//   It should ask the user for the number of days they would like to rent the car.
//   If the user doesn’t answer or if the answer is not a number, ask again.
//   Calculate the cost to rent the car. The car costs $40 everyday.
//   If the user rents a car for more than 10 days, they get a 5% discount.
//   The function should return the total price of the car rental.
  
//   Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
//   Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
//   Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().
  
//   Call the function totalVacationCost()
  
//   Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.
  

// Function to calculate hotel cost
function hotelCost() {
    let numberOfNights;
    do {
      numberOfNights = parseInt(prompt("Enter the number of nights you would like to stay in the hotel:"));
    } while (isNaN(numberOfNights));
  
    const hotelPricePerNight = 140;
    return numberOfNights * hotelPricePerNight;
  }
  
  // Function to calculate plane ride cost
  function planeRideCost() {
    let destination;
    do {
      destination = prompt("Enter your destination:");
    } while (!destination || typeof destination !== "string");
  
    switch (destination.toLowerCase()) {
      case "london":
        return 183;
      case "paris":
        return 220;
      default:
        return 300;
    }
  }
  
  // Function to calculate rental car cost
  function rentalCarCost() {
    let numberOfDays;
    do {
      numberOfDays = parseInt(prompt("Enter the number of days you would like to rent the car:"));
    } while (isNaN(numberOfDays));
  
    const carPricePerDay = 40;
    let totalCarRentalCost = numberOfDays * carPricePerDay;
  
    if (numberOfDays > 10) {
      const discountPercentage = 5;
      const discountAmount = (totalCarRentalCost * discountPercentage) / 100;
      totalCarRentalCost -= discountAmount;
    }
  
    return totalCarRentalCost;
  }
  
  // Function to calculate total vacation cost
  function totalVacationCost() {
    const hotelCost = hotelCost();
    const planeRideCost = planeRideCost();
    const rentalCarCost = rentalCarCost();
    const totalCost = hotelCost + planeRideCost + rentalCarCost;
  
    console.log("The hotel cost: $" + hotelCost);
    console.log("The plane tickets cost: $" + planeRideCost);
    console.log("The car rental cost: $" + rentalCarCost);
    console.log("Total vacation cost: $" + totalCost);
  }
  
  // Call the totalVacationCost function
  totalVacationCost();


//   🌟 Exercise 5 : Users
// Instructions
// Create a new structured HTML file and a new Javascript file

// <div id="container">Users:</div>
// <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
// </ul>
// <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
// </ul>


// Add the code above, to your HTML file

// Using Javascript:
// Retrieve the div and console.log it
// Change the name “Pete” to “Richard”.
// Delete the second <li> of the second <ul>.
// Change the name of the first <li> of each <ul> to your name. (Hint : use a loop)

// Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

// Using Javascript:
// Add a “light blue” background color and some padding to the <div>.
// Do not display the <li> that contains the text node “Dan”. (the last <li> of the first <ul>)
// Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
// Change the font size of the whole body.

// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).🌟 Exercise 6 : Change The Navbar


// Instructions
// Create a new structured HTML file and a new Javascript file

// <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>


// Add the code above, to your HTML file

// Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (<li>).
// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.

// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).
