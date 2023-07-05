// Exercise 1 : Giphy API
// Create a program to retrieve the data from the API URL provided above.
// Use the fetch() method to make a GET request to the Giphy API and Console.log the Javascript Object that you receive.
// Make sure to check the status of the Response and to catch any occuring errors.


async function getGifs() {
    try {
        const gifsPromise = await fetch('https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My')
        if (gifsPromise.ok) {
            
            const gifsData = await gifsPromise.json();
            console.log(gifsData);
        } else {
            throw new Error ("Issues with Fetch");
        }    
    } catch(err) {
        console.log("IN THE CATCH", err);
    }
}

getGifs()




//2 
// Read carefully the documention to understand all the possible queries that the URL accept.
// Use the Fetch API to retrieve 10 gifs about the “sun”. The starting position of the results should be 2.
// Make sure to check the status of the Response and to catch any occuring errors.
// Console.log the Javascript Object that you receive.


async function getGifsSun(word) {
    
    try {
        const gifsSunPromise = await fetch(`https://api.giphy.com/v1/gifs/search?q=${word}&limit=10&offset=2&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`)
        if (gifsSunPromise.ok) {
            
            const gifsData = await gifsSunPromise.json();
            console.log('10 gifs with sun, starting from position 2:', gifsData); 
        } else {
            throw new Error ("Issues with Fetch");
        }    
    } catch(err) {
        console.log("IN THE CATCH", err);
    }
}

getGifsSun('sun')

//3
// Improve the program below :

// fetch("https://www.swapi.tech/api/starships/9/")
//     .then(response => response.json())
//     .then(objectStarWars => console.log(objectStarWars.result));
// Create an async function, that will await for the above GET request.
// The program shouldn’t contain any then() method.
// Make sure to check the status of the Response and to catch any occuring errors.

async function starWars() {
    try {
        const response = await fetch(`https://www.swapi.tech/api/starships/9/`)
        if (response.ok) {
            
            const starData = await response.json();
            console.log(starData.result); 
        } else {
            throw new Error ("Issues with Fetch");
        }    
    } catch(err) {
        console.log("IN THE CATCH", err);
    }
}

starWars()


//Exercise 4: Analyze
// Instructions
// Analyse the code provided below - what will be the outcome?

function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved'); 
        }, 2000);
    });
}

async function asyncCall() {
    console.log('calling'); //2 immidiately after calling func
    let result = await resolveAfter2Seconds(); //wait when finished
    console.log(result); //3 - console.log('resolved')
}

asyncCall(); //1
