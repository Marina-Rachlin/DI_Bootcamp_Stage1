// const url = `https://v6.exchangerate-api.com/v6/3618cca6f16b652284a155fe/latest/USD`;

const fromSelect = document.getElementById("from");
const toSelect = document.getElementById("to");
const switchButton = document.getElementById("switch"); 

document.getElementById("input").addEventListener("keyup", handleClick);

fromSelect.addEventListener("change", handleClick);
toSelect.addEventListener("change", handleClick);
switchButton.addEventListener("click", switchCurrencies);

fetchCurrencies(); 


function switchCurrencies() {
    [fromSelect.value, toSelect.value] = [toSelect.value, fromSelect.value]; 
    handleClick(); 
}

function fetchCurrencies() {
  const url = `https://v6.exchangerate-api.com/v6/3618cca6f16b652284a155fe/codes`;
  fetch(url)
    .then((res) => res.json()) 
    .then((res) => populateDropDown(res.supported_codes)) 
    .catch((error) => console.error(error));
}

function populateDropDown(codes) { // takes code and ...
    console.log("rates:", codes);
    const entries = Object.entries(codes); // ... create entries ... 
    // console.log('entries:', entries);
  
    for (const entry of entries)
    { // ... disctruct to loop 
      const [code, name] = entry[1]; // for each entries we have code and name. We use [1] index, coz we have code, name bu index 1. index 0 is number
      const option = document.createElement("option"); // create 2 opt
      option.innerText = name; // for each opt create name and ... 
      option.value = code; // ... code
      fromSelect.appendChild(option); // add to page and each populate by API
  
      const option2 = document.createElement("option");
      option2.innerText = name;
      option2.value = code;
      toSelect.appendChild(option2);
    }
  }

async function handleClick() {
  const currency1 = fromSelect.value; 
  const currency2 = toSelect.value;
  const input = document.getElementById("input");
  const summary = document.getElementById("summary");

  const url = `https://v6.exchangerate-api.com/v6/3618cca6f16b652284a155fe/pair/${currency1}/${currency2}`;

  try
  {
    const res = await fetch(url); 
    const resJson = await res.json(); 
    const rate = resJson.conversion_rate; 
    const amount = Number(input.value); 
    const total = amount * rate; 
    summary.innerText = `${amount} ${currency1} = ${total} ${currency2}`; 
  }
  catch (error)
  {
    console.error(error);
  }
}




















