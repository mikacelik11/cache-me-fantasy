# 🏀 Cache Me Fantasy - Fantasy Basketball Platform

A full-stack fantasy basketball web application where users can create leagues, draft NBA players, and compete with friends!

## 🌟 Features

### ✅ Completed Features
- **User Authentication**: Secure registration and login with JWT tokens
- **League Management**: Create private leagues with unique join codes
- **Live Player Database**: 150+ NBA players with real 2024-25 stats
- **Team Management**: Join leagues and build your fantasy roster
- **Player Drafting**: Draft available players to your team
- **Real-time Updates**: View team rosters and available players
- **Responsive UI**: Beautiful, animated interface with modern design
- **Production Deployment**: Fully deployed on Render (backend) and Vercel (frontend)

### 🚧 Planned Features
- Weekly matchups and scoring
- Trade system between teams
- League standings and playoffs
- Live stat tracking and updates
- Commissioner controls
- Mobile app

## 🛠️ Tech Stack

### Frontend
- **React** - UI framework
- **Axios** - HTTP client
- **React Router** - Navigation
- **CSS3** - Styling with animations

### Backend
- **FastAPI** - Python web framework
- **PostgreSQL** - Database
- **SQLAlchemy** - ORM
- **JWT** - Authentication
- **Uvicorn** - ASGI server

### Deployment
- **Frontend**: Vercel
- **Backend**: Render
- **Database**: Render PostgreSQL

## 🚀 Live Application

- **Frontend**: [https://cache-me-fantasy.vercel.app](https://cache-me-fantasy.vercel.app)
- **Backend API**: [https://cache-me-fantasy.onrender.com](https://cache-me-fantasy.onrender.com)
- **API Docs**: [https://cache-me-fantasy.onrender.com/docs](https://cache-me-fantasy.onrender.com/docs)

## 💻 Local Development Setup

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL 13+
- Git

### Backend Setup

1. **Clone the repository**
```bash
   git clone https://github.com/mikacelik11/cache-me-fantasy.git
   cd cache-me-fantasy/backend
```

2. **Create virtual environment**
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Set up PostgreSQL database**
```bash
   # Create database
   createdb cache_me_fantasy
   
   # Or using psql
   psql -U postgres
   CREATE DATABASE cache_me_fantasy;
```

5. **Configure environment variables**
```bash
   # Create .env file (optional for local)
   echo "DATABASE_URL=postgresql://localhost/cache_me_fantasy" > .env
```

6. **Run the server**
```bash
   uvicorn app.main:app --reload
```

   Backend will run at: `http://localhost:8000`

7. **Seed NBA players**
```bash
   python -m app.add_all_nba_players
```

### Frontend Setup

1. **Navigate to frontend directory**
```bash
   cd ../frontend
```

2. **Install dependencies**
```bash
   npm install
```

3. **Configure environment variables**
```bash
   # Create .env file
   echo "REACT_APP_API_URL=http://localhost:8000" > .env
```

4. **Run the development server**
```bash
   npm start
```

   Frontend will run at: `http://localhost:3000`

## 📁 Project Structure
```
cache-me-fantasy/
├── backend/
│   ├── app/
│   │   ├── routers/          # API endpoints
│   │   │   ├── users.py      # Authentication
│   │   │   ├── players.py    # Player management
│   │   │   ├── leagues.py    # League operations
│   │   │   └── teams.py      # Team management
│   │   ├── models.py         # Database models
│   │   ├── database.py       # Database connection
│   │   ├── auth.py           # JWT authentication
│   │   ├── main.py           # FastAPI app
│   │   └── add_all_nba_players.py  # Player seeding
│   └── requirements.txt      # Python dependencies
│
└── frontend/
    ├── public/
    ├── src/
    │   ├── components/       # Reusable components
    │   ├── pages/           # Page components
    │   │   ├── Auth.js      # Login/Register
    │   │   ├── Dashboard.js # Main dashboard
    │   │   └── Draft.js     # Draft interface
    │   ├── services/
    │   │   └── api.js       # API calls
    │   └── App.js           # Main app
    └── package.json         # Node dependencies
```

## 🔑 API Endpoints

### Authentication
- `POST /users/register` - Register new user
- `POST /users/login` - Login user
- `GET /users/me` - Get current user

### Players
- `GET /players/` - Get all NBA players
- `GET /players/available/list` - Get available players
- `GET /players/{player_id}` - Get specific player

### Leagues
- `POST /leagues/create` - Create new league
- `POST /leagues/join/{league_code}` - Join league
- `GET /leagues/my-leagues` - Get user's leagues
- `GET /leagues/{league_code}/teams` - Get league teams

### Teams
- `GET /teams/my-teams` - Get user's teams
- `POST /teams/{team_id}/draft/{player_id}` - Draft player
- `GET /teams/{team_id}/roster` - Get team roster

## 🎮 How to Play

1. **Register/Login**: Create an account or login
2. **Create/Join League**: 
   - Create a private league (get unique code)
   - Or join existing league with code
3. **Draft Players**: Browse 150+ NBA players and draft to your team
4. **Manage Team**: View your roster and available players
5. **Compete**: (Coming soon) Weekly matchups and scoring

## 🔒 Security

- JWT-based authentication
- Password hashing with bcrypt
- SQL injection protection via SQLAlchemy ORM
- CORS configuration for secure cross-origin requests
- Environment variable protection for sensitive data

## 🚀 Deployment

### Backend (Render)
- Automatic deployments from `main` branch
- PostgreSQL database with SSL
- Environment variables configured
- Health checks enabled

### Frontend (Vercel)
- Automatic deployments from `main` branch
- Environment variables configured
- CDN-optimized static hosting

## 👨‍💻 Developer

**Mikael Celik**
- GitHub: [@mikacelik11](https://github.com/mikacelik11)
- LinkedIn: [Mikael Celik](https://www.linkedin.com/in/mikaelcelik/)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- NBA player statistics sourced from various public APIs
- Inspired by classic fantasy basketball platforms
- Built as a portfolio project for learning full-stack development

## 📧 Contact

For questions or feedback, please open an issue on GitHub or contact me directly.

---

**Happy drafting! 🏀**