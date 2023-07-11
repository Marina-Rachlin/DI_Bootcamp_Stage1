fetch('/users')
  .then(response => response.json())
  .then(data => {
    document.getElementById('output').innerHTML = `<p>${JSON.stringify(data)}</p>`;
  })
  .catch(error => {
    console.log('Error:', error);
  });

  function showAlert() {
    alert('Button Clicked!');
  }

