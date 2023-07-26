import "./App.css";
import UserFavoriteAnimals from "./UserFavoriteAnimals";
import Exercise from "./Exercise3";

const myelement = <h1>I love JSX!</h1>;
const sum = 5 + 5;

const user = {
  firstName: "Bob",
  lastName: "Dylan",
  favAnimals: ["Horse", "Turtle", "Elephant", "Monkey"],
};



function App() {
  return (
    <div>
      <header>

        <p>Hello world!</p>
        <div>{myelement}</div>
        <div>React is {sum} times better with JSX</div>

        <div>
          <h3>{user.firstName}</h3>
          <h3>{user.lastName}</h3>
        </div>
        <ul>
            {
                //item everytime is object with key: name of attr and value after =
                user.favAnimals.map((item, index) => (
                    <UserFavoriteAnimals favAnimals={item} key={index} />  
                ))  
            }
        </ul>
        
        <Exercise />
       
      </header>
    </div>
  );
}

export default App;