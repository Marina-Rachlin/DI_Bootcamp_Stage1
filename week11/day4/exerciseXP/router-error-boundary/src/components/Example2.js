import React, { Component } from 'react';
import data from '../data.json'; 

class Example2 extends Component {
  render() {
    return (
      <div>
        {data.Skills.map((item, index) => (
          <ul key={index}>
            <li>
              {item.Area}
              <ul>
                {item.SkillSet.map((skill, skillIndex) => (
                  <li key={skillIndex}>
                    {skill.Name}
                  </li>
                ))}
              </ul>
            </li>
          </ul>
        ))}
      </div>
    );
  }
}

export default Example2;
