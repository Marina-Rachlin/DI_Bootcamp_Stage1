import React from "react";

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      err: null,
      errInfo: null
    };
  }

  componentDidCatch(err, errInfo) {
    
    this.setState({ 
        err: err,
        errInfo: errInfo 
    });
  }

  render() {
    if (this.state.err) {
        return (
        <>
            <h1>Something went wrong.</h1>
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