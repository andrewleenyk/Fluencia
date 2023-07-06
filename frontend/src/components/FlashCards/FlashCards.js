import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './FlashCards.css'

const FlashCards = () => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [terms, setTerms] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/cards/');
      setTerms(response.data.terms);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleCardClick = () => {
    setIsFlipped(!isFlipped);
  };

  return (
    <div>
      <h1>Flashcards</h1>
      <div className={`card ${isFlipped ? 'flipped' : ''}`} onClick={handleCardClick}>
        <div className="card-content">
          <div className="front-face">
            <h3>{terms[currentIndex]?.word}</h3>
          </div>
          <div className="back-face">
            <p>{terms[currentIndex]?.definition}</p>
          </div>
        </div>
      </div>
      <button className="button" onClick={() => setCurrentIndex((currentIndex + 1) % terms.length)}>Next Card</button>
    </div>
  );  
};

export default FlashCards;
