import React from "react";

class ErrorBoundary extends React.Component {
  constructor() {
    super();
    this.state = {
      hasErr: false
    };
  }

  componentDidCatch(err, errInfo) {
    this.setState({ hasErr:true, err: err, errInfo: errInfo });
    //write err and errInfo to a log file and send to a support team
  }

  render() {
    if (this.state.hasErr) {
        return (
        <>
           Something went wrong, we are fixing the problem
            <details style={{ whiteSpace: 'pre-wrap' }}>
                {this.state.err && this.state.err.toString()};
                <br />
                {this.state.errInfo.componentStack};
            </details>
        </>
        )
    }
    
    return this.props.children;
  }
}

export default ErrorBoundary;