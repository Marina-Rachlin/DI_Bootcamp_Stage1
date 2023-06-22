// Exercise 1
// Part I

const people = ["Greg", "Mary", "Devon", "James"];

// Remove "Greg" from the people array
people.shift();

// Replace "James" with "Jason"
const index = people.indexOf("James");
people[index] = "Jason";

// Add your name to the end of the people array
people.push("Yourname");

// Print Mary's index
console.log(people.indexOf("Mary"));

// Make a copy of the people array without "Mary" or your name
const copy = people.slice(1, 3);

// Print the index of "Foo"
console.log(people.indexOf("Foo"));
// It returns -1 because "Foo" is not present in the people array

// Get the last element of the array
const last = people[people.length - 1];

// Part 2
const people = ["Mary", "Devon", "Jason", "Yourname"];

// Iterate through the people array and console.log each person
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
}

// Iterate through the people array and exit the loop after console.log "Devon"
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
  if (people[i] === "Devon") {
    break;
  }
}

// Exercise 2 : Your Favorite Colors
// Instructions
// Create an array called colors where the value is a list of your five favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

const colors = ["blue", "red", "green", "yellow", "purple"];
const suffixes = ["st", "nd", "rd", "th", "th"];

for (let i = 0; i < colors.length; i++) {
  let choiceSuffix;

  if (i + 1 === 1) {
    choiceSuffix = suffixes[0];
  } else if (i + 1 === 2) {
    choiceSuffix = suffixes[1];
  } else if (i + 1 === 3) {
    choiceSuffix = suffixes[2];
  } else {
    choiceSuffix = suffixes[3];
  }

  console.log(`My ${i + 1}${choiceSuffix} choice is ${colors[i]}`);
}

// 🌟 Exercise 3 : Repeat The Question
// Instructions
// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?

let number = Number(prompt("Enter a number:"));

while (typeof number === "number" && number < 10) {
  number = Number(prompt("Enter a new number:"));
}

console.log("Number is greater than or equal to 10. Exiting the loop.");


// Exercise 4 : Building Management
// Review About Objects
// Copy and paste the above object to your Javascript file.

// Console.log the number of floors in the building.

// Console.log how many apartments are on the floors 1 and 3.

// Console.log the name of the second tenant and the number of rooms he has in his apartment.

// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

// Console.log the number of floors in the building.
console.log("Number of floors in the building:", building.numberOfFloors);

// Console.log how many apartments are on floors 1 and 3.
console.log("Number of apartments on the first floor:", building.numberOfAptByFloor.firstFloor);
console.log("Number of apartments on the third floor:", building.numberOfAptByFloor.thirdFloor);

// Console.log the name of the second tenant and the number of rooms he has in his apartment.
const secondTenant = building.nameOfTenants[1];
const roomsForSecondTenant = building.numberOfRoomsAndRent[secondTenant][0];
console.log("Second tenant:", secondTenant);
console.log("Number of rooms in second tenant's apartment:", roomsForSecondTenant);

// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, then increase Dan’s rent to 1200.
const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];

if (sarahRent + davidRent > danRent) {
    console.log("Sarah's and David's rent is greater than Dan's rent. Increasing Dan's rent...");
    building.numberOfRoomsAndRent.dan[1] = 1200;
}

console.log(building);

// 🌟 Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

const family = {
    father: "John",
    mother: "Jane",
    son: "Sam",
    daughter: "Emily"
};

// Print the keys of the object
console.log("Keys of the family object:");
for (let key in family) {
    console.log(key);
}

// Print the values of the object
console.log("\nValues of the family object:");
for (let key in family) {
    console.log(family[key]);
}


// Exercise 6 : Rudolf
// Instructions
// const details = {
//   my: 'name',
//   is: 'Rudolf',
//   the: 'raindeer'
// }
// Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
};

let sentence = "";

for (let key in details) {
    sentence += details[key] + " ";
}

console.log(sentence.trim());


// Exercise 7 : Secret Group
// Instructions
// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let secretSocietyName = "";

for (let i = 0; i < names.length; i++) {
    secretSocietyName += names[i][0];
}

secretSocietyName = secretSocietyName.split('').sort().join('');

console.log("Secret Society Name:", secretSocietyName);







