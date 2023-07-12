const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: false }));
app.use(express.json());


//Defining the routes:

app.get('/aboutMe/:hobby', (req, res) => {
  const { hobby } = req.params;// equivalent of const hobby = req.params.hobby, but using js object destructuring
  if (typeof hobby !== 'string') {
    res.status(404).send('Invalid hobby parameter');
  } else {
    res.send(`One of my hobbies is ${hobby}`);
  }
});
  
app.get('/pic', (req, res) => {
  res.send('<div><img src="https://media.nomadicmatt.com/2022/iscancunsafe.jpeg" alt="cancun"></div>');
});

app.get('/form', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/form.html'));
});

app.post('/formData', (req, res) => {
  const { email, message } = req.body;
  res.send(`${email} sent you a message: "${message}"`);
});

//Start the server:

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}/`);
});








