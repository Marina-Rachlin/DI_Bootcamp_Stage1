const http = require('http');

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/html');
  
  res.write('<h1>This is my first response</h1>');
  res.write('<h2>This is my second response</h2>');
  res.end('<p>This is the third line of HTML.</p>');
});

server.listen(3000, 'localhost', () => {
  console.log('Server is running on port 3000');
});