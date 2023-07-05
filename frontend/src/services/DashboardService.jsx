import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DashboardService = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/userdashboard/all/') // Update the URL to match your Django API endpoint
      .then(response => {
        setUsers(response.data.users);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>User List</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.username}</li>
        ))}
      </ul>
    </div>
  );
};

export default DashboardService;
