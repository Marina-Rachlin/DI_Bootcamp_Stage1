// 🌟 Exercise 1 : Change The Article

       // Retrieve h1 and console.log it
       var h1 = document.querySelector('h1');
       console.log(h1);

       // Remove the last paragraph
       var paragraphs = document.querySelectorAll('p');
       var lastParagraph = paragraphs[paragraphs.length - 1];
       lastParagraph.parentNode.removeChild(lastParagraph);

       // Change background color of h2 when clicked
       var h2 = document.querySelector('#color-change');
       h2.addEventListener('click', function() {
           h2.style.backgroundColor = 'red';
       });

       // Hide h3 when clicked
       var h3 = document.querySelector('#hide-heading');
       h3.addEventListener('click', function() {
           h3.style.display = 'none';
       });

       // Make text of all paragraphs bold when button is clicked
       var boldButton = document.querySelector('#bold-button');
       boldButton.addEventListener('click', function() {
           paragraphs.forEach(function(paragraph) {
               paragraph.style.fontWeight = 'bold';
           });
       });

       // Bonus: Random font size on h1 hover
       h1.addEventListener('mouseover', function() {
           var randomSize = Math.floor(Math.random() * 101); // Random number between 0 and 100
           h1.style.fontSize = randomSize + 'px';
       });

       // Bonus: Fade out 2nd paragraph on hover
       var secondParagraph = document.querySelectorAll('p')[1];
       secondParagraph.id = "fade-paragraph";
       secondParagraph.addEventListener('mouseover', function() {
           secondParagraph.classList.add('fade-out');
           console.log(secondParagraph.className)
       });
       secondParagraph.addEventListener('mouseout', function() {
           secondParagraph.classList.remove('fade-out');
       });



