import React from 'react';

const Phone = () => {
    const [brand, setBrand] = React.useState("Samsung");
    const [model, setModel] = React.useState("Galaxy S20");
    const [color, setColor] = React.useState("black");
    const [year, setYear] = React.useState(2020);

    const changeColor = () => setColor('blue');
    
    return (
        <div>
          <h2>My phone is a {brand}</h2> 
          <p>It is a {color} {model} from {year}</p>
          <button onClick={changeColor}>Change color</button>
        </div>
    )
}

export default Phone;