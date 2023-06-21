// Change the value of the id attribute from navBar to socialNetworkNavigation
const navBar = document.getElementById("navBar");
navBar.setAttribute("id", "socialNetworkNavigation");

// Create a new <li> tag and append it to the <ul>
const newListItem = document.createElement("li");
const logoutText = document.createTextNode("Logout");
newListItem.appendChild(logoutText);

const ulElement = document.querySelector("#socialNetworkNavigation ul");
ulElement.appendChild(newListItem);

// Retrieve the first and last <li> elements and display their text
const firstLi = ulElement.firstElementChild;
const lastLi = ulElement.lastElementChild;

console.log("First link: " + firstLi.textContent);
console.log("Last link: " + lastLi.textContent);
