import React, { useState, useEffect } from 'react';

const Example1 = () => {
  const [socialMedias, setSocialMedias] = useState([]);

  useEffect(() => {
    // Fetch the data from data.json
    fetch('./data.json') // Replace with the correct path to data.json if needed
      .then(response => response.json())
      .then(data => setSocialMedias(data.SocialMedias))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h2>Social Media Links:</h2>
      <ul>
        {socialMedias.map((link, index) => (
          <li key={index}>
            <a href={link} target="_blank" rel="noopener noreferrer">{link}</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Example1;


