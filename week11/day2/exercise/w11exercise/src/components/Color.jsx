import { useEffect, useState } from "react";

const Color = () => {
    const [favoriteColor, setFavoriteColor] = useState('red');

    useEffect(() => {
        alert('UseEffect is reached');
    },[]);

   const changeColor = () => setFavoriteColor('blue');

    return 
    <>
    <h1> My Favorite Color is {favoriteColor}</h1>
    <button onClick={changeColor}>Change Color</button>
    </>
}

export default Color;