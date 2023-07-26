import React from 'react';

const Events = () => {
    const [isToggleOn, setIsToggleOn] = React.useState('true');
    const handleClick = (e) => alert('I am clicked');
    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
          alert('Enter key pressed! Input value: ' + event.target.value);
        }
      };

    const toggleState = () => setIsToggleOn(!isToggleOn);

    return(
        <>
        <button onClick={handleClick}>Click me</button>
        <input onKeyDown={handleKeyDown} type='text' placeholder='Press the ENTER key!'></input><br/>
        <button onClick={toggleState}>{isToggleOn?'ON':'OFF'}</button>
        </>
    );
}

export default Events;