import React, { useState, useEffect } from 'react';
import { getMyLeagues, createLeague, joinLeague } from '../services/api';
import Draft from './Draft';
import './Dashboard.css';

function Dashboard({ onLogout }) {
  const [leagues, setLeagues] = useState([]);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [showJoinModal, setShowJoinModal] = useState(false);
  const [showDraft, setShowDraft] = useState(false);
  const [newLeagueName, setNewLeagueName] = useState('');
  const [joinCode, setJoinCode] = useState('');
  const [teamName, setTeamName] = useState('');

  useEffect(() => {
    loadLeagues();
  }, []);

  const loadLeagues = async () => {
    try {
      const response = await getMyLeagues();
      console.log('Leagues loaded:', response.data);
      setLeagues(response.data);
    } catch (err) {
      console.error('Error loading leagues:', err);
      console.error('Error details:', err.response?.data);
    }
  };

  const handleCreateLeague = async (e) => {
    e.preventDefault();
    try {
      const response = await createLeague({ name: newLeagueName, max_teams: 10 });
      const leagueCode = response.data.league_code;
      
      // Automatically join the league with a team
      const teamNamePrompt = `${newLeagueName} - My Team`;
      await joinLeague(leagueCode, teamNamePrompt);
      
      setShowCreateModal(false);
      setNewLeagueName('');
      loadLeagues();
    } catch (err) {
      console.error('Error creating league:', err);
      alert('Error creating league');
    }
  };

  const handleJoinLeague = async (e) => {
    e.preventDefault(); //
    try {
      await joinLeague(joinCode, teamName);
      setShowJoinModal(false);
      setJoinCode('');
      setTeamName('');
      loadLeagues();
    } catch (err) {
      alert(err.response?.data?.detail || 'Error joining league');
    }
  };

  // If showing draft page, render that instead
  if (showDraft) {
    return <Draft onBack={() => setShowDraft(false)} />;
  }

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>🏀 Cache Me Fantasy</h1>
        <button onClick={onLogout} className="logout-btn">Logout</button>
      </header>

      <div className="dashboard-content">
        <div className="actions">
          <button onClick={() => setShowCreateModal(true)} className="action-btn">
            Create League
          </button>
          <button onClick={() => setShowJoinModal(true)} className="action-btn">
            Join League
          </button>
          <button onClick={() => setShowDraft(true)} className="action-btn draft-btn-main">
            🏀 Draft Players
          </button>
        </div>

        <div className="leagues-section">
          <h2>My Leagues</h2>
          {leagues.length === 0 ? (
            <p className="no-leagues">No leagues yet. Create or join one!</p>
          ) : (
            <div className="leagues-grid">
              {leagues.map((league) => (
                <div key={league.id} className="league-card">
                  <h3>{league.name}</h3>
                  <p className="league-code">Code: {league.league_code}</p>
                  <p>Max Teams: {league.max_teams}</p>
                  <p>Draft: {league.draft_completed ? '✅ Complete' : '⏳ Pending'}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Create League Modal */}
      {showCreateModal && (
        <div className="modal-overlay" onClick={() => setShowCreateModal(false)}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <h2>Create New League</h2>
            <form onSubmit={handleCreateLeague}>
              <input
                type="text"
                placeholder="League Name"
                value={newLeagueName}
                onChange={(e) => setNewLeagueName(e.target.value)}
                required
              />
              <div className="modal-buttons">
                <button type="submit">Create</button>
                <button type="button" onClick={() => setShowCreateModal(false)}>
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Join League Modal */}
      {showJoinModal && (
        <div className="modal-overlay" onClick={() => setShowJoinModal(false)}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <h2>Join League</h2>
            <form onSubmit={handleJoinLeague}>
              <input
                type="text"
                placeholder="League Code"
                value={joinCode}
                onChange={(e) => setJoinCode(e.target.value.toUpperCase())}
                required
              />
              <input
                type="text"
                placeholder="Your Team Name"
                value={teamName}
                onChange={(e) => setTeamName(e.target.value)}
                required
              />
              <div className="modal-buttons">
                <button type="submit">Join</button>
                <button type="button" onClick={() => setShowJoinModal(false)}>
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

export default Dashboard; 