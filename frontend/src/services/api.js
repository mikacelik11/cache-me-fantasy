import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

// Create axios instance
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if it exists
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth endpoints
export const register = (userData) => api.post('/users/register', userData);
export const login = (username, password) => {
  const formData = new FormData();
  formData.append('username', username);
  formData.append('password', password);
  return api.post('/users/login', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};
export const getCurrentUser = () => api.get('/users/me');

// Player endpoints
export const getAllPlayers = () => api.get('/players/');
export const getAvailablePlayers = () => api.get('/players/available/list');

// League endpoints
export const createLeague = (leagueData) => api.post('/leagues/create', leagueData);
export const joinLeague = (leagueCode, teamName) => 
  api.post(`/leagues/join/${leagueCode}?team_name=${teamName}`);
export const getMyLeagues = () => api.get('/leagues/my-leagues');
export const getLeagueTeams = (leagueCode) => api.get(`/leagues/${leagueCode}/teams`);

// Team endpoints
export const getMyTeams = () => api.get('/teams/my-teams');
export const draftPlayer = (teamId, playerId) => api.post(`/teams/${teamId}/draft/${playerId}`);
export const getTeamRoster = (teamId) => api.get(`/teams/${teamId}/roster`);

export default api;
