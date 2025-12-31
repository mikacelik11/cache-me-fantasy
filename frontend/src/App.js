import React, { useState, useEffect } from 'react';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import { getCurrentUser } from './services/api';
import './App.css';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [showRegister, setShowRegister] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if user is already logged in
    const token = localStorage.getItem('token');
    if (token) {
      getCurrentUser()
        .then(() => setIsAuthenticated(true))
        .catch(() => {
          localStorage.removeItem('token');
          setIsAuthenticated(false);
        })
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  const handleLogin = () => {
    setIsAuthenticated(true);
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    setIsAuthenticated(false);
  };

  if (loading) {
    return (
      <div style={{ 
        display: 'flex', 
        justifyContent: 'center', 
        alignItems: 'center', 
        height: '100vh' 
      }}>
        <h2>Loading...</h2>
      </div>
    );
  }

  if (!isAuthenticated) {
    return showRegister ? (
      <Register switchToLogin={() => setShowRegister(false)} />
    ) : (
      <Login 
        onLogin={handleLogin} 
        switchToRegister={() => setShowRegister(true)} 
      />
    );
  }

  return <Dashboard onLogout={handleLogout} />;
}

export default App;