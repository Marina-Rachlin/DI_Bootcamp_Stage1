const http = require('http');

const user = {
    firstname: 'John',
    lastname: 'Doe'
}

const server = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'application/json');
    res.json(user);
  });
  
  server.listen(8080, 'localhost', () => {
    console.log('Server is running on port 8080');
  });