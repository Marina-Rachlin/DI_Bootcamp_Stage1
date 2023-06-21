// Array of planets in the solar system
const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

// Get the listPlanets section
const listPlanetsSection = document.querySelector(".listPlanets");

// Loop through each planet and create a div for it
planets.forEach((planet) => {
  // Create a div for the planet
  const planetDiv = document.createElement("div");
  planetDiv.classList.add("planet", planet.toLowerCase());

  // Set a different background color for each planet
  planetDiv.style.backgroundColor = getRandomColor();

  // Append the planet div to the listPlanets section
  listPlanetsSection.appendChild(planetDiv);

  // Check if the planet has moons and create them
  const moons = getMoonsForPlanet(planet);
  if (moons.length > 0) {
    moons.forEach((moon) => {
      const moonDiv = document.createElement("div");
      moonDiv.classList.add("moon");
      moonDiv.style.backgroundColor = getRandomColor();
      planetDiv.appendChild(moonDiv);
    });
  }
});

// Helper function to generate a random color
function getRandomColor() {
  const letters = "0123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

// Helper function to get the moons for a planet
function getMoonsForPlanet(planet) {
  // Define the moons for each planet (can be an array of objects if required)
  const moonsByPlanet = {
    Mercury: [],
    Venus: [],
    Earth: ["Moon"],
    Mars: ["Phobos", "Deimos"],
    Jupiter: ["Io", "Europa", "Ganymede", "Callisto"],
    Saturn: ["Titan", "Enceladus", "Mimas"],
    Uranus: ["Miranda", "Ariel", "Umbriel", "Titania", "Oberon"],
    Neptune: ["Triton"]
  };

  return moonsByPlanet[planet] || [];
}
