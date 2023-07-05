import React, { useEffect, useState } from 'react';
import axios from 'axios';
import authService from '../services/AuthService';


const CardService = () => {
  const [data, setData] = useState({ terms: [], verbs: [] });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/cards/');
      setData(response.data);
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
      <h2>Verbs:</h2>
      {data.verbs.map((verb) => (
        <div key={verb.id}>
          <p>Word: {verb.word}</p>
          <p>Definition: {verb.definition}</p>
          <p>Conjugations: {JSON.stringify(verb.conjugations)}</p>
        </div>
      ))}
    </div>
  );
};

export default CardService;
