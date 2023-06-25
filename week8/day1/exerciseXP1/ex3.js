// 🌟 Exercise 3 : Transform The Sentence

var allBoldItems;

function getBoldItems() {
    allBoldItems = document.querySelectorAll('p strong');
    console.log(allBoldItems);
}

function highlight() {
    for (var i = 0; i < allBoldItems.length; i++) {
        allBoldItems[i].classList.add('blue');
    }
}

function returnItemsToDefault() {
    for (var i = 0; i < allBoldItems.length; i++) {
        allBoldItems[i].classList.remove('blue');
    }
}