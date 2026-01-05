from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, SessionLocal
from app import models
from app.routers import players, users, leagues, teams

# Create all database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cache Me Fantasy API")

# CORS configuration
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    "https://cache-me-fantasy.vercel.app",  # Production URL
    "https://cache-me-fantasy-dcpu0m3b9-mikaels-projects-9a5fce72.vercel.app",  # Preview URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Seed players on startup if database is empty
@app.on_event("startup")
async def startup_event():
    db = SessionLocal()
    try:
        player_count = db.query(models.Player).count()
        print(f"Database currently has {player_count} players")
        print("Running player seed script...")
        from app.add_all_nba_players import add_all_nba_players
        add_all_nba_players()
        print("Player seeding complete!")
    finally:
        db.close()

# Include routers
app.include_router(users.router)
app.include_router(players.router)
app.include_router(leagues.router)
app.include_router(teams.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Cache Me Fantasy API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} #