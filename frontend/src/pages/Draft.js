import React, { useState, useEffect } from 'react';
import { getAvailablePlayers, draftPlayer, getMyTeams, getTeamRoster } from '../services/api';
import './Draft.css';

function Draft({ onBack }) {
  const [availablePlayers, setAvailablePlayers] = useState([]);
  const [myTeam, setMyTeam] = useState(null);
  const [roster, setRoster] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      // Get user's first team
      const teamsResponse = await getMyTeams();
      if (teamsResponse.data.length > 0) {
        const team = teamsResponse.data[0];
        setMyTeam(team);
        
        // Load roster
        const rosterResponse = await getTeamRoster(team.id);
        setRoster(rosterResponse.data);
      }
      
      // Load available players
      const playersResponse = await getAvailablePlayers();
      setAvailablePlayers(playersResponse.data);
      
      setLoading(false);
    } catch (err) {
      console.error('Error loading draft data:', err);
      setLoading(false);
    }
  };

  const handleDraft = async (playerId) => {
    if (!myTeam) {
      alert('You need to join a league first!');
      return;
    }
    
    try {
      await draftPlayer(myTeam.id, playerId);
      alert('Player drafted successfully!');
      loadData(); // Reload to update available players and roster
    } catch (err) {
      alert(err.response?.data?.detail || 'Error drafting player');
    }
  };

  if (loading) {
    return <div className="loading">Loading draft...</div>;
  }

  if (!myTeam) {
    return (
      <div className="draft-container">
        <h2>You need to join a league first!</h2>
        <button onClick={onBack}>Back to Dashboard</button>
      </div>
    );
  }

  return (
    <div className="draft-container">
      <header className="draft-header">
        <button onClick={onBack} className="back-btn">← Back</button>
        <h1>Draft Players - {myTeam.name}</h1>
      </header>

      <div className="draft-content">
        {/* My Roster */}
        <div className="roster-section">
          <h2>My Roster ({roster.length} players)</h2>
          {roster.length === 0 ? (
            <p className="no-players">No players drafted yet</p>
          ) : (
            <div className="player-list">
              {roster.map((player) => (
                <div key={player.id} className="player-card drafted">
                  <div className="player-info">
                    <h3>{player.name}</h3>
                    <p>{player.position} - {player.nba_team}</p>
                  </div>
                  <div className="player-stats">
                    <span>{player.points_per_game} PPG</span>
                    <span>{player.rebounds_per_game} RPG</span>
                    <span>{player.assists_per_game} APG</span>
                  </div>
                  <div className="fantasy-points">
                    {player.fantasy_points} FP
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Available Players */}
        <div className="available-section">
          <h2>Available Players ({availablePlayers.length})</h2>
          <div className="player-list">
            {availablePlayers.map((player) => (
              <div key={player.id} className="player-card">
                <div className="player-info">
                  <h3>{player.name}</h3>
                  <p>{player.position} - {player.nba_team}</p>
                </div>
                <div className="player-stats">
                  <span>{player.points_per_game} PPG</span>
                  <span>{player.rebounds_per_game} RPG</span>
                  <span>{player.assists_per_game} APG</span>
                </div>
                <div className="fantasy-points">
                  {player.fantasy_points} FP
                </div>
                <button 
                  onClick={() => handleDraft(player.id)}
                  className="draft-btn"
                >
                  Draft
                </button>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Draft;