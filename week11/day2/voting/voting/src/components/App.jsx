import React from "react";
import Card from "./Card";

const languages = ['Php','Python','JavaSript','Java'];
const createCard = languages.map(language =>  <Card lang = {language}/>)

function App(){
    return(
        <div>
             <h1>Vote Your Language!</h1>
            {createCard}
        </div>
    );
}

export default App;
