// App.js
import React from 'react';
import Car from './Car';
import Events from './Events';
import Phone from './Phone';
import Color from './Color';

function App() {
  const carinfo = {name: "Ford", model: "Mustang"};
  return (
    <div>
      <Car  
      model = {carinfo.model}/>
      <Events />
      <Phone /> 
      <Color/>
    </div>
  );
}

export default App;
