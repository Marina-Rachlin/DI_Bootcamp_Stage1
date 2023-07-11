const express = require('express');
const app = express();
const path = require('path');
const port = 3000;

const user = {firstname: 'John',lastname: 'Doe'};

app.use('/', express.static(__dirname + '/../public'));

app.get('/users', (req, res) => {
    res.json(user);
  });
  
  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}/`);
  });


app.get('/:id', (req, res) => {
    const id = req.params.id;
    console.log({ id });
    res.json({ id });
  });

app.get('/', (req, res) => {
  
})  
 
  
  
  
  
  
  
