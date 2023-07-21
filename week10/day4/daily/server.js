import express from 'express';
import * as fs from 'fs';
import path from 'path';
const __dirname = path.resolve();

const app = express();

//for json, forms
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));
app.use(express.json());

//get html pages
app.get('/login', (req, res) => {
  res.sendFile(__dirname + '/public/login.html');
});

app.get('/register', (req, res) => {
  res.sendFile(__dirname + '/public/register.html');
});


app.post('/register', (req, res) => {
  //values from js file when I got value to every input through getElementByID
  const { name, lastName, email, username, password } = req.body;

  // data from JSON file
  const data = fs.readFileSync('users.json');
  const users = JSON.parse(data);

  // Check if the username or password already exist
  const userExists = users.find(user => user.username === username || user.password === password);
  if (userExists) {
    //go to client to work with this error
    return res.send('error1');
  }

  // Add the new user to array
  users.push({ name, lastName, email, username, password });

  // Write user to JSON file
  fs.writeFileSync('users.json', JSON.stringify(users, null, 2));

  res.send('register');
});


//after submit 
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  // Read data from JSON file
  const data = fs.readFileSync('users.json');
  //to JS obj
  const users = JSON.parse(data);

  // Check if the user exists
  const user = users.find(user => user.username === username && user.password === password);
  //if not registered
  if (!user) {
    return res.send('error2');
  }

  res.send('login');
});


app.listen(3000, () => {
  console.log('Server is running on port 3000');
});