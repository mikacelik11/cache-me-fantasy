from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/players", tags=["players"])

@router.get("/", response_model=List[schemas.Player])
def get_all_players(db: Session = Depends(get_db)):
    players = db.query(models.Player).all()
    return players

@router.get("/{player_id}", response_model=schemas.Player)
def get_player(player_id: int, db: Session = Depends(get_db)):
    player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.get("/available/list", response_model=List[schemas.Player])
def get_available_players(db: Session = Depends(get_db)):
    players = db.query(models.Player).filter(models.Player.is_available == True).all()
    return players