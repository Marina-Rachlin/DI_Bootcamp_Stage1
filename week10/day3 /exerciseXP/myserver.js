const express = require('express');
const fs = require('fs');


const app = express();
const port = 3000;

app.listen(port, () => {
    console.log('The server is running on port', port);
})


fs.readFile('info.txt', 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
  
    console.log(data);
  });

  
