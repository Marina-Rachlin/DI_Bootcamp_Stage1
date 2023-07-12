const fs = require('fs');

fs.readFile('RightLeft.txt', 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
  
    const stepsToRight = (data.match(/>/g) || []).length;
    const stepsToLeft = (data.match(/</g) || []).length;
    const finalPosition = stepsToRight - stepsToLeft;
    const stepsToMinusOne = data.indexOf('<', 0) + 1;
  
    console.log('Steps to the right:', stepsToRight);
    console.log('Steps to the left:', stepsToLeft);
    console.log('Final position:', finalPosition);
    console.log('Steps to -1:', stepsToMinusOne);
  });


