import React from 'react';
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import ErrorBoundary from './ErrorBoundary';
import Example1 from './components/Example1';
import Example2 from './components/Example2';
import Example3 from './components/Example3';
import PostList from './components/PostList';


const HomeScreen = () => <h3>Home</h3>;

const ProfileScreen = () => <h3>Profile Screen</h3>;

const ShopScreen = () => {
  throw new Error("Error during render");
};

const getFromUrl = async() => {
  const data = {
      key1: 'myusername',
      email: 'mymail@gmail.com',
      name: 'Isaac',
      lastname: 'Doe',
      age: 27

  }

  try {
      const res = await fetch('https://webhook.site/38c1cf14-a3c8-4721-b617-7e596355c05a', {
          method: 'POST',
          mode: "no-cors", // disable CORS
          headers: {
              'Content-Type': 'application-json'
          },
          body: JSON.stringify(data)
      });
      console.log(res);
  } catch (error) {
      console.log(error);
  }

}

const App = () => (
  <BrowserRouter>
    <div className="container">
      <nav className="nav nav-pills">
        <NavLink exact className="nav-link" activeClassName="active" to="/">
          Home
        </NavLink>
        <NavLink className="nav-link" activeClassName="active" to="/profile">
          Profile
        </NavLink>
        <NavLink className="nav-link" activeClassName="active" to="/shop">
          Shop
        </NavLink>
      </nav>

      <Routes>
      <Route
          path="/"
          element={
            <ErrorBoundary>
              <HomeScreen />
            </ErrorBoundary>
          }
        />
        <Route
          path="/profile"
          element={
            <ErrorBoundary>
              <ProfileScreen />
            </ErrorBoundary>
          }
        />
        <Route
          path="/shop"
          element={
            <ErrorBoundary>
              <ShopScreen />
            </ErrorBoundary>
          }
        />
      </Routes>

      <Example1 />
      <Example2 />
      <Example3 />
      <br/> <br />
      <PostList />

      <button onClick={getFromUrl}>post the data</button>

    
        
    </div>
  </BrowserRouter>
);

export default App;
