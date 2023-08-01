import React, { useEffect, useState } from 'react';
import axios from 'axios';

const AITutorService = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // api request from openai for suggestion of mneumonic from a given term
    // use prompt specified in prompts
    // return two things, the mneuemnic itself and the explanation
  }, []);

};

export default AITutorService;
