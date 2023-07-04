import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import AuthService from './services/AuthService';
import Home from './components/Home';
import Login from './components/Login';
import Register from './components/Register';

const PrivateRoute = ({ children }) => {
  const user = AuthService.getCurrentUser();
  return user ? children : <Navigate to="/login" replace={true} />;
};

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/home" element={ AuthService.getCurrentUser() ? <Home /> : <Navigate to="/login" replace={true} />} />
        <Route path="*" element={<Navigate to="/login" replace={true} />} />
      </Routes>
    </Router>
  );
};

export default App;
