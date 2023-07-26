import React from 'react';
import Garage from './Garage';

function Car(props) {
  const [color, setColor] = React.useState('silver');

  return (
    <div>
      <h1>This car is {props.model}.</h1>
      <h3>This car is {color} {props.model}.</h3>
      <Garage size='small'/>
    </div>
  );
}

  export default Car;