import React from "react";

function Card(props){
    const [count,setCount] = React.useState(0);
    function increase(){
        setCount(count +1)
    }
    return(
        <div className="languages">
            <div className="language">
                <p className="voteCount">{count}</p>
                <h3 className="languageName">{props.lang}</h3>
                <button onClick={increase}>Click Here</button>
            </div>
        </div>
    );
}

export default Card;
