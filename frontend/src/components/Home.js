import React, { useEffect, useState } from 'react';
import axios from 'axios';

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

  return (
    <div>
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
