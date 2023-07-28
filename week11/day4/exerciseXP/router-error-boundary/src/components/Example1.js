import React, { Component } from 'react';
import data from '../data.json';

class Example1 extends Component {
    constructor() {
        super();
    }
    
    render() { 
        
        return ( 
            <div>
                {data.SocialMedias.map((item, index) => (
                    <ul key={index}>
                        <li>{item}</li>
                    </ul>
                ))}
            </div>
         );
    }
}
 
export default Example1;