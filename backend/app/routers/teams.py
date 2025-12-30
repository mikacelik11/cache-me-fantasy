from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, auth
from app.database import get_db

router = APIRouter(prefix="/teams", tags=["teams"])

@router.post("/{team_id}/draft/{player_id}", response_model=schemas.Team)
def draft_player(
    team_id: int,
    player_id: int,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    # Get team and verify ownership
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    if team.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not your team")
    
    # Get player
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    if not player.is_available:
        raise HTTPException(status_code=400, detail="Player already drafted")
    
    # Check if league draft is completed
    league = db.query(models.League).filter(models.League.id == team.league_id).first()
    if league.draft_completed:
        raise HTTPException(status_code=400, detail="Draft already completed")
    
    # Draft the player
    team.players.append(player)
    player.is_available = False
    
    db.commit()
    db.refresh(team)
    return team

@router.get("/{team_id}/roster", response_model=List[schemas.Player])
def get_team_roster(team_id: int, db: Session = Depends(get_db)):
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    return team.players

@router.get("/my-teams", response_model=List[schemas.Team])
def get_my_teams(
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    teams = db.query(models.Team).filter(models.Team.user_id == current_user.id).all()
    return teams

@router.delete("/{team_id}/roster/{player_id}")
def remove_player_from_team(
    team_id: int,
    player_id: int,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(get_db)
):
    # Get team and verify ownership
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    if team.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not your team")
    
    # Get player
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    # Remove player from team
    if player in team.players:
        team.players.remove(player)
        player.is_available = True
        db.commit()
        return {"message": "Player removed from team"}
    else:
        raise HTTPException(status_code=400, detail="Player not on this team") #