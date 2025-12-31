import React, { useState } from 'react';
import { login } from '../services/api';
import './Auth.css';

function Login({ onLogin, switchToRegister }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    try {
      const response = await login(username, password);
      localStorage.setItem('token', response.data.access_token);
      onLogin();
    } catch (err) {
      setError('Invalid username or password');
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-box">
        <h1>Cache Me Fantasy 🏀</h1>
        <h2>Login</h2>
        
        {error && <div className="error-message">{error}</div>}
        
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit">Login</button>
        </form>
        
        <p className="switch-auth">
          Don't have an account?{' '}
          <span onClick={switchToRegister}>Register</span>
        </p>
      </div>
    </div>
  );
}

export default Login;
