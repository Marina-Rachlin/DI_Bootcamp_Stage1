import React from "react";
import data from '../data.json'; 

class Example3 extends React.Component{
  render(){
    return(
        <div>
                {data.Experiences.map((item, index) => (
                    <div key={index}>
                        <div><img src={item.logo}/></div>
                        <a href={item.url}><b>{item.companyName}</b></a>
                        
                        {
                            item.roles.map((role, index) => (
                                <div key={index}>
                                    <h3>{role.title}</h3>
                                    <p>{role.startDate} {role.location}</p>
                                    <p>{role.description}</p>
                                </div>
                                
                            ))
                        }
                    </div>
                ))}
            </div>
    )
  }
}

export default Example3;