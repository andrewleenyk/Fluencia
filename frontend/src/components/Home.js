import React, { useEffect, useState } from 'react';
import axios from 'axios';
import authService from '../services/AuthService';
import DashboardService from '../services/DashboardService';
import FlashCards from './FlashCards/FlashCards';

const Home = () => {
  const [data, setData] = useState({ terms: []});

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/cards/');
      setData(response.data);
      console.log(data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleLogout = () => {
    console.log("Home.js:: logged out, but need to refresh page to see change")
    authService.logout();
  };

  return (
    <div>
      <button onClick={handleLogout}>Logout</button>
      <h1>Data from Django Backend:</h1>
      <h2>Terms:</h2>
      {data.terms.map((term) => (
        <div key={term.id}>
          <p>Word: {term.word}</p>
          <p>Definition: {term.definition}</p>
        </div>
      ))}
      <h2>Other Users:</h2>
      <DashboardService />
      <FlashCards />
    </div>
  );
};

export default Home;
