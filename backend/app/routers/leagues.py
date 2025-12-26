from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import random
import string
from app import models, schemas, auth
from app.database import get_db

router = APIRouter(prefix="/leagues", tags=["leagues"])

def generate_league_code():
    """Generate a random 6-character league code"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@router.post("/create", response_model=schemas.League, status_code=status.HTTP_201_CREATED)
def create_league(
    league: schemas.LeagueCreate,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    # Generate unique league code
    while True:
        league_code = generate_league_code()
        existing = db.query(models.League).filter(models.League.league_code == league_code).first()
        if not existing:
            break
    
    # Create league
    new_league = models.League(
        name=league.name,
        league_code=league_code,
        max_teams=league.max_teams
    )
    db.add(new_league)
    db.commit()
    db.refresh(new_league)
    return new_league

@router.post("/join/{league_code}", response_model=schemas.Team, status_code=status.HTTP_201_CREATED)
def join_league(
    league_code: str,
    team_name: str,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    # Find league
    league = db.query(models.League).filter(models.League.league_code == league_code).first()
    if not league:
        raise HTTPException(status_code=404, detail="League not found")
    
    # Check if league is full
    team_count = db.query(models.Team).filter(models.Team.league_id == league.id).count()
    if team_count >= league.max_teams:
        raise HTTPException(status_code=400, detail="League is full")
    
    # Check if user already has a team in this league
    existing_team = db.query(models.Team).filter(
        models.Team.user_id == current_user.id,
        models.Team.league_id == league.id
    ).first()
    if existing_team:
        raise HTTPException(status_code=400, detail="You already have a team in this league")
    
    # Create team
    new_team = models.Team(
        name=team_name,
        user_id=current_user.id,
        league_id=league.id
    )
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team

@router.get("/my-leagues", response_model=List[schemas.League])
def get_my_leagues(
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    # Get all leagues where user has a team
    teams = db.query(models.Team).filter(models.Team.user_id == current_user.id).all()
    league_ids = [team.league_id for team in teams]
    leagues = db.query(models.League).filter(models.League.id.in_(league_ids)).all()
    return leagues

@router.get("/{league_code}", response_model=schemas.League)
def get_league(league_code: str, db: Session = Depends(get_db)):
    league = db.query(models.League).filter(models.League.league_code == league_code).first()
    if not league:
        raise HTTPException(status_code=404, detail="League not found")
    return league

@router.get("/{league_code}/teams", response_model=List[schemas.Team])
def get_league_teams(league_code: str, db: Session = Depends(get_db)):
    league = db.query(models.League).filter(models.League.league_code == league_code).first()
    if not league:
        raise HTTPException(status_code=404, detail="League not found")
    
    teams = db.query(models.Team).filter(models.Team.league_id == league.id).all()
    return teams