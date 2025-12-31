from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app import models
from app.routers import players, users, leagues, teams

# Create all database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cache Me Fantasy API")

# CORS configuration - Add port 3001!
origins = [
    "http://localhost:3000",
    "http://localhost:3001",  # Add this line!
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",  # Add this line!
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Include routers AFTER CORS middleware
app.include_router(users.router)
app.include_router(players.router)
app.include_router(leagues.router)
app.include_router(teams.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Cache Me Fantasy API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}