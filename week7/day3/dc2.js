// Instructions
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *

// Using One Loop:
const rowsOneLoop = 6;
let patternOneLoop = '';

for (let i = 1; i <= rowsOneLoop; i++) {
  patternOneLoop += '* ';
  console.log(patternOneLoop);
}



// Using Two Nested For Loops:
const rowsNested = 6;

for (let i = 1; i <= rowsNested; i++) {
  let patternNested = '';
  for (let j = 1; j <= i; j++) {
    patternNested += '* ';
  }
  console.log(patternNested);
}


