import ErrorBoundary from "./ErrorBoundary";
import React, { Component } from "react";
import "./App.css";

class BuggyCounter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 0,
    };
  }

  handleClick = () => {
    this.setState((previous) => {
      //console.log(previous.counter);
      return { counter: previous.counter + 1 };
    });
  };

  render() {
    if (this.state.counter >= 5) {
      throw new Error("I crashed....");
    }

    return (
      <>
        <h1 onClick={this.handleClick}>{this.state.counter}</h1>
      </>
    );
  }
}

function App() {
  return (
    <div>
        <b>
          Click on the numbers to increase the counters. The counter is
          programmed to throw error when it reaches 5. This simulates a
          JavaScript error in a component.
        </b>
        <hr />
        
        <p>
        These two counters are inside the same error boundary. If one crashes, the error boundary will replace both of them.  
        </p>
        <ErrorBoundary> 
            <BuggyCounter />
            <BuggyCounter />
        </ErrorBoundary> 

        <p>These two counters are each inside of their own error boundary. So if one crashes, the other is not affected.</p>
        <ErrorBoundary>
            <BuggyCounter />
        </ErrorBoundary>
        <ErrorBoundary>
            <BuggyCounter />
        </ErrorBoundary>
        <hr />

        <p>This counter is not inside of boundary. So if crashes, all other components are deleted.</p>
        <BuggyCounter />
        
    </div>
  );
}

export default App;