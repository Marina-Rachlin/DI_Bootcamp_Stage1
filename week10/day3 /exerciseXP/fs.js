const fs = require('fs');


fs.writeFile('file.txt', 'Lets drink tee!', (err) => {
    console.log(err);
    return;
})
console.log('Lets drink tee!');

fs.appendFile('file.txt', '\nOr coffe!', (err) => {
    console.log(err);
    return;
})
console.log('or coffe');

fs.unlink('file.txt', (err) => {
    console.log(err);
})
console.log('The file deleted');