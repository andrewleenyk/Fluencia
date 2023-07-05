import React from 'react';
import { Link } from 'react-router-dom';
import './WelcomePage.css';

const WelcomePage = () => {
  return (
    <div className="container">
      <h1 className="heading">Welcome to Fluent, a language learning app!</h1>
      <div className="links-container">
        <Link to="/login" className="link">Login</Link>
        <Link to="/register" className="link">Register</Link>
      </div>
    </div>
  );
};

export default WelcomePage;
