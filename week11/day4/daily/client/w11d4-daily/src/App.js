import './App.css';
import React, {Component} from 'react';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      header: null,
      inputValue: '',
      responseMessage: '',
    }
  }

  componentDidMount() {
    const getText = async () => {
      try {
          const res = await fetch(`http://localhost:3030/api/hello`);
          const data = await res.json();
          //console.log(data);
          this.setState({header: data});
      } catch (error) {
          console.log(error);
      }
    }
    getText();
  }

  //post to my server
  handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch('http://localhost:3030/api/world', {
        method: 'POST',
        headers: {
          "Content-Type": "application/json",
        },
        //key can be whatever
        body: JSON.stringify({ post: this.state.inputValue }),
      });

      if (res.ok) {
        // Get the response message from the server
        const responseMessage = await res.text();
        //in browser console log
        console.log('Data posted successfully');
        // Reset the input after submit and set the response message from server
        this.setState({ inputValue: "", responseMessage });
      } else {
        console.error("Response not 200");
      }
    } catch (error) {
      console.error('Failed to post data');
    }
  }

  handleInput = (e) => {
    this.setState({inputValue: e.target.value})
  }
  
  render() { 

    const {inputValue, responseMessage} = this.state;

    return ( 
      <div className="App">
        <header>
          <h1>{this.state.header}</h1>
          <h2>Post to Server:</h2>
          <form onSubmit={this.handleSubmit}>
              <input type="text" onChange={this.handleInput} value={inputValue}/>
              <button>Submit</button>
          </form>
          <p>{responseMessage}</p>
        </header>
      </div>
    );
  }
}
 
export default App;