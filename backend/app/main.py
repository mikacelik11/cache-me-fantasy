from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app import models
from app.routers import players

# Create all database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cache Me Fantasy API")

# CORS - allows React frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(players.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Cache Me Fantasy API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}