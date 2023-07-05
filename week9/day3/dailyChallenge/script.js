const form = document.getElementById('myForm');
form.addEventListener("submit", getValuesForm)

function getValuesForm(event) {
    event.preventDefault();
    const valueWord = event.target.category.value.toLowerCase();
    console.log(valueWord);
    getGif(valueWord);
}

async function getGif (word) {
    console.log("start fetching a gif ...");
    try { 
        const response = await fetch(`https://api.giphy.com/v1/gifs/random?tag=${word}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`)
        if(response.ok) {
            const datagif = await response.json();
            displayGif(datagif, word);
        } else {
            throw new Error ("issues with fetch")
        }
    }catch(error) {
        if (error.message === "Cannot Find a Gif") {
            getWord()
        } else {
            console.log("ERROR", error)
        }
    }
}

const divElem = document.getElementById("container");

function displayGif(datagif) {
    if (datagif["data"].length === 0) {
      console.log("Cannot Find a Gif");
      throw new Error("Cannot Find a Gif");
    } else {

      const gifContainer = document.createElement("div");
      const image = document.createElement("img");
      const urlGif = datagif["data"]["images"]["original"]["url"];
      image.src = urlGif;

      const delBtn = document.createElement("button");
      const text = document.createTextNode("Delete This Gif");
      delBtn.append(text);

      delBtn.addEventListener("click", function () {
        divElem.removeChild(gifContainer);
      });

      gifContainer.appendChild(delBtn);
      gifContainer.appendChild(image);
      divElem.appendChild(gifContainer);
    }
}

const deleteAllBtn = document.getElementById('deleteAll');

deleteAllBtn.addEventListener("click", function () {
    while (divElem.firstChild) {
      divElem.removeChild(divElem.firstChild);
    }
});
  