import React, { useState } from 'react';
import { register } from '../services/api';
import './Auth.css';

function Register({ switchToLogin }) {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    try {
      await register({ email, username, password });
      setSuccess(true);
      setTimeout(() => switchToLogin(), 2000);
    } catch (err) {
      setError(err.response?.data?.detail || 'Registration failed');
    }
  };

  if (success) {
    return (
      <div className="auth-container">
        <div className="auth-box">
          <h2>Success! 🎉</h2>
          <p>Redirecting to login...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="auth-container">
      <div className="auth-box">
        <h1>Cache Me Fantasy 🏀</h1>
        <h2>Register</h2>
        
        {error && <div className="error-message">{error}</div>}
        
        <form onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
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
          <button type="submit">Register</button>
        </form>
        
        <p className="switch-auth">
          Already have an account?{' '}
          <span onClick={switchToLogin}>Login</span>
        </p>
      </div>
    </div>
  );
}

export default Register;
