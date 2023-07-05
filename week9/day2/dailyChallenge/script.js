// Instructions
// 1rst Daily Challenge

// Create two functions. Each function should return a promise.

// The first function called makeAllCaps(), takes an array of words as an argument
// If all the words in the array are strings, resolve the promise. The value of the resolved promise is the array of words uppercased.
// else, reject the promise with a reason.

function makeAllCaps(arr) {
    const newPromise = new Promise((resolve, reject) => {
        if (arr.every(word => typeof word === 'string')) {
            const newArr = arr.map(element => element.toUpperCase());
            resolve(newArr);
        } else {
            reject ("Not all words are string");
        }
    })
    return newPromise;
}

// The second function called sortWords(), takes an array of words uppercased as an argument
// If the array length is bigger than 4, resolve the promise. The value of the resolved promise is the array of words sorted in alphabetical order.
// else, reject the promise with a reason.


function sortWords(arr) {
    const newPromise = new Promise((resolve, reject) => {
        if (arr.length > 4) {
            const newArr = arr.sort();
            resolve(newArr);
        } else {
            reject ("Not a good array");
        }
    })
    return newPromise;
}

//in this example, the catch method is executed
makeAllCaps([1, "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, you should see in the console, 
// the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
      .catch(error => console.log(error))

//2 dailychallenge

const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`;
  
  function toJs() {
    return new Promise((resolve, reject) => {
      const morseObj = JSON.parse(morse);
      if (Object.keys(morseObj).length === 0) {
        reject(new Error('Morse JavaScript object is empty.'));
      } else {
        resolve(morseObj);
      }
    });
  }
  
  function toMorse(morseJS) {
    return new Promise((resolve, reject) => {
      const userWord = prompt('Enter a word or sentence:');
      const morseTranslation = [];
  
      for (let i = 0; i < userWord.length; i++) {
        const char = userWord[i].toLowerCase();
        if (morseJS[char] === undefined) {
          reject(new Error(`Character "${userWord[i]}" doesn't exist in the Morse JavaScript object.`));
          return;
        }
        morseTranslation.push(morseJS[char]);
      }
  
      resolve(morseTranslation);
    });
  }
  
  function joinWords(morseTranslation) {
    const result = morseTranslation.join(' ');
    document.getElementById('morse-output').textContent = result;
  }
  
  toJs()
    .then(toMorse)
    .then(joinWords)
    .catch((error) => {
      console.error(error);
    });
  