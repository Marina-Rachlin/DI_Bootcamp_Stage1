function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}
// Prediction: The value of 'a' will be 3 inside the funcOne function.
// Explanation: 'a' is initially assigned the value 5. The if statement condition is true (5 > 1), so the value of 'a' is updated to 3. The alert will display "inside the funcOne function 3".



// #1.2
// If the variable is declared with 'const' instead of 'let', it will cause an error because 'const' variables cannot be reassigned. The code inside the if statement would result in an error.


//#2
let a = 0;
function funcTwo() {
    a = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

// #2.1 - if we will run:
funcThree()
funcTwo()
funcThree()

// Prediction: The value of 'a' will be 0, 5, 5 respectively.
// Explanation: Initially, 'a' is assigned the value 0. When funcThree is called, it will display "inside the funcThree function 0". Then, funcTwo is called and it updates the value of 'a' to 5. When funcThree is called again, it will display "inside the funcThree function 5" because the value of 'a' has been modified.

// #2.2 What will happen if the variable is declared with const instead of let ?
// If the variable is declared with 'const' instead of 'let', it will cause an error because 'const' variables cannot be reassigned. The assignment a = 5 in funcTwo would result in an error.



//#3
function funcFour() {
    window.a = "hello";
}


function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

// if we will run:
funcFour()
funcFive()

//Prediction: The value of 'a' will be "hello" inside the funcFive function.
// Explanation: In funcFour, the global object's property 'a' is set to the string "hello". In funcFive, when accessing 'a', it refers to the global object's property, and thus it will display "inside the funcFive function hello".




//#4
let a = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}


// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
    a = 3;
    }
    alert(inside the funcOne function ${a});
    }
    // Prediction: The value of 'a' will be 3 inside the funcOne function.
    // Explanation: 'a' is initially assigned the value 5. The if statement condition is true (5 > 1), so the value of 'a' is updated to 3. The alert will display "inside the funcOne function 3".
    
    // #1.1
    // If the variable is declared with 'const' instead of 'let', it will cause an error because 'const' variables cannot be reassigned. 
    
    //#2
    let a = 0;
    function funcTwo() {
    a = 5;
    }
    
    function funcThree() {
    alert(inside the funcThree function ${a});
    }
    // Prediction: The value of 'a' will be 0, 5, 5 respectively.
    // Explanation: Initially, 'a' is assigned the value 0. When funcThree is called, it will display "inside the funcThree function 0". Then, funcTwo is called and it updates the value of 'a' to 5. When funcThree is called again, it will display "inside the funcThree function 5" because the value of 'a' has been modified.
    
    // #2.2
    // If the variable is declared with 'const' instead of 'let', it will cause an error because 'const' variables cannot be reassigned. The assignment a = 5 in funcTwo would result in an error.
    
    //#3
    function funcFour() {
    window.a = "hello";
    }
    
    function funcFive() {
    alert(inside the funcFive function ${a});
    }
    // Prediction: The value of 'a' will be "hello" inside the funcFive function.
    // Explanation: In funcFour, the global object's property 'a' is set to the string "hello". In funcFive, when accessing 'a', it refers to the global object's property, and thus it will display "inside the funcFive function hello".
    
    //#4
    let a = 1;
    function funcSix() {
        let a = "test";
        alert(inside the funcSix function ${a});
    }

    // if we will run funcSix()

    // Prediction: The value of 'a' will be "test" inside the funcSix function.
    // Explanation: Inside funcSix, a new local variable 'a' is declared and assigned the value "test". This variable 'a' shadows the outer variable 'a' with a different value. Therefore, the alert will display "inside the funcSix function test".

    // If the variable is declared with 'const' instead of 'let', it will not cause any change in functionality, because variable 'a' inside funcSix is a separate variable with a different scope, and 'const' will only affect the variable within its own scope.



//#5
let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);

// Prediction: The value of 'a' will be 5, 2 respectively.
// Explanation: Inside the if block, a new block-scoped variable 'a' is declared and assigned the value 5. It only exists within the if block. The alert inside the if block will display "in the if block 5". Outside of the if block, 'a' refers to the outer variable declared at the top with a value of 2.

//If the variable is declared with const instead of let the behavior will remain the same. The 'const' declaration will create a block-scoped constant variable 'a' inside the if block, and it will not affect the outer variable 'a'. 



// 🌟 Exercise 2 : Ternary Operator
// Instructions
// Using the code below:

// function winBattle(){
//     return true;
// }
// Transform the winBattle() function to an arrow function.
// Create a variable called experiencePoints.
// Assign to this variable, a ternary operator. If winBattle() is true, the experiencePoints variable should be equal to 10, else the variable should be equal to 1.
// Console.log the experiencePoints variable.

const winBattle = () => true;
const experiencePoints = winBattle() ? 10 : 1;
console.log(experiencePoints);



// 🌟 Exercise 3 : Is It A String ?
// Instructions
// Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not. The function should return true or false
// Check out the example below to see the expected output
// Example:

// console.log(isString('hello')); 
// //true
// console.log(isString([1, 2, 4, 0]));
// //false

const isString = (value) => {
    return typeof value === 'string';
  };
  

// 🌟 Exercise 4 : Find The Sum
// Instructions
// Create a one line function (ie. an arrow function) that receives two numbers as parameters and returns the sum.

const sum = (num1, num2) => num1 + num2;


// 🌟 Exercise 5 : Kg And Grams
// Instructions
// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)

// First, use function declaration and invoke it.
// Then, use function expression and invoke it.
// Write in a one line comment, the difference between function declaration and function expression.
// Finally, use a one line arrow function and invoke it.

//function declaration 
function convertToGramsFromKg(weightInKg) {
    return weightInKg * 1000;
  }
  
  
//function expression
const convertToGramsFromKg = function(weightInKg) {
    return weightInKg * 1000;
  };
  
  
//Difference between function declaration and function expression:
//Function declaration: The function is declared using the function keyword. It can be invoked before its declaration in the code.
//Function expression: The function is assigned to a variable using the assignment operator (=). It needs to be defined before it can be invoked.
  
//arrow_function:
const convertToGramsFromKg = weightInKg => weightInKg * 1000;


// 🌟 Exercise 6 : Fortune Teller
// Instructions
// Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
// The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."


