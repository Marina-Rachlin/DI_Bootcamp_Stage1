let newDiv = document.getElementById('content');
let finder = document.getElementById('submit');
finder.addEventListener('click', submita);

let loading = document.getElementById('loading');
let icon = document.getElementById('icon');
let homeworld;

let contDiw = document.getElementById('content');

async function submita(event)
{
    event.preventDefault();
    showLoading()
    let id = Math.floor(Math.random()*100)
    
    try
    {
        let r = await fetch(`https://www.swapi.tech/api/people/${id}`)
        if(!r.status == '200'){
            throw new Error('not found')
        }
        const json = await r.json();
        hideLoading();
        let homeworldname = 'not valid'
        console.log(json.result.properties.homeworld);
        if (json.result.properties.homeworld)
        {
            let r2 = await fetch(json.result.properties.homeworld)
            let resFromR2 = await r2.json()
            homeworldname = resFromR2.result.properties.name;
        }
        swResult({...json.result.properties,homeworld:homeworldname})
    }
    catch(e)

    {
        hideLoading();
        contDiw.innerHTML = '';
        let erMessage = document.createElement('p');
        erMessage.textContent = "Oh No! That person isn't available.";
        erMessage.setAttribute('style', 'color: yellow');
        contDiw.appendChild(erMessage);
        console.log(`${e} "Oh No! That person isnt available.`);
    }
}

function showLoading() {
    icon.classList.add('fa-solid', 'fa-spinner', 'fa-spin-pulse')
}

function hideLoading() {
    icon.classList.remove('fa-solid', 'fa-spinner', 'fa-spin-pulse')
}

function swResult(properties) {
    console.log(properties);
    
    contDiw.innerHTML = '';
    const labels = {
       name: 'Name: ',
       height: 'Height: ',
       gender: 'Gender: ',
       birth_year: 'Birth Year: ',
       homeworld: 'Homeworld: '
     };

    for(item in properties)
    {
        if (labels[item])
        {
            let dataDiv = document.createElement('p');
            dataDiv.textContent = labels[item] + properties[item];
            dataDiv.setAttribute('style', 'color: yellow')
            contDiw.appendChild(dataDiv);
        }
    }
}