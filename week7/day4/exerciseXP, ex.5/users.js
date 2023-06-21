// Retrieve the div and console.log it
const containerDiv = document.getElementById("container");
console.log(containerDiv);

// Change the name "Pete" to "Richard"
const listItems = document.querySelectorAll("ul.list li");
listItems[1].textContent = "Richard";

// Delete the second <li> of the second <ul>
const secondUl = document.querySelectorAll("ul.list")[1];
secondUl.removeChild(secondUl.children[1]);

// Change the name of the first <li> of each <ul> to your name
const firstUl = document.querySelectorAll("ul.list")[0];
firstUl.children[0].textContent = "Marina";
const secondUlFirstLi = document.querySelectorAll("ul.list")[1].children[0];
secondUlFirstLi.textContent = "Marina";

// Add class "student_list" to both <ul>'s
const ulElements = document.querySelectorAll("ul.list");
ulElements.forEach((ul) => ul.classList.add("student_list"));

// Add classes "university" and "attendance" to the first <ul>
ulElements[0].classList.add("university", "attendance");

// Add background color and padding to the <div>
containerDiv.style.backgroundColor = "lightblue";
containerDiv.style.padding = "10px";

// Do not display the <li> that contains the text node "Dan"
const danLi = firstUl.querySelector("li:last-child");
danLi.style.display = "none";

// Add a border to the <li> that contains the text node "Richard"
const richardLi = secondUlFirstLi;
richardLi.style.border = "1px solid black";

// Change the font size of the whole body
document.body.style.fontSize = "18px";

// Bonus: Check if the background color of the div is "lightblue" and alert the users
if (containerDiv.style.backgroundColor === "lightblue") {
  const users = document.querySelectorAll("ul.list li");
  const usersArray = Array.from(users).map((user) => user.textContent);
  const alertMessage = "Hello " + usersArray.join(" and ");
  alert(alertMessage);
}
