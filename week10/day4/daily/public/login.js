// Login form submission
const loginForm = document.getElementById('loginForm');
loginForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Send login request
  const response = await fetch('/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ username, password })
  });

  const result = await response.text();
  const msg = document.querySelector('#loginMessage');
  if (result === 'login') {
    msg.textContent = `Hey ${username} welcome back again!`
  } else if (result === 'error2') {
    msg.textContent = 'Username or password is not registered!';
  }
});