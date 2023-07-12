const getAllProducts = async() => {
    try{
       const res = await fetch('/api/products');
       const data = await data.json();
    }
    catch (err){
        console.log(err);
    }
}

const render = (arr) => {
    const html = arr.map(item => {
        return <div style="display:inline-block">
            <h2>${item.name}</h2>
            <h4>${item.name}</h4>
        </div>
        })
}