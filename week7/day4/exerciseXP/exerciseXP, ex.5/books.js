// Create an array of book objects
const allBooks = [
    {
      title: "Tale of Love and Darkness",
      author: "Amos Oz",
      image: "https://upload.wikimedia.org/wikipedia/en/thumb/f/f4/A_Tale_of_Love_and_Darkness_%28book_cover%29.jpg/220px-A_Tale_of_Love_and_Darkness_%28book_cover%29.jpg",
      alreadyRead: true
    },
    {
      title: "The Master and Margarita",
      author: "Michael Bulgakov",
      image: "https://m.media-amazon.com/images/I/91BHmR8HASL._AC_UF1000,1000_QL80_.jpg",
      alreadyRead: true
    }
  ];
  
  // Get the listBooks section
  const listBooksSection = document.querySelector(".listBooks");
  
  // Loop through each book in the array and render it in a div
  allBooks.forEach((book) => {
    // Create a div for each book
    const bookDiv = document.createElement("div");
    bookDiv.classList.add("book");
  
    // Create an image element and set its source and width
    const bookImage = document.createElement("img");
    bookImage.src = book.image;
    bookImage.width = "100";
  
    // Create a paragraph element for the book details
    const bookDetails = document.createElement("p");
    bookDetails.textContent = book.title + " written by " + book.author;
  
    // Add the image and details to the book div
    bookDiv.appendChild(bookImage);
    bookDiv.appendChild(bookDetails);
  
    // If the book is already read, add the "read" class to the book div
    if (book.alreadyRead) {
      bookDiv.classList.add("read");
    }
  
    // Add the book div to the listBooks section
    listBooksSection.appendChild(bookDiv);
  });
  