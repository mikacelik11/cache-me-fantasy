from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# Player Schemas
class PlayerBase(BaseModel):
    name: str
    position: str
    nba_team: str
    points_per_game: float
    rebounds_per_game: float
    assists_per_game: float
    steals_per_game: float
    blocks_per_game: float

class PlayerCreate(PlayerBase):
    pass

class Player(PlayerBase):
    id: int
    fantasy_points: float
    is_available: bool
    
    class Config:
        from_attributes = True

# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# League Schemas
class LeagueBase(BaseModel):
    name: str
    max_teams: int = 10

class LeagueCreate(LeagueBase):
    pass

class League(LeagueBase):
    id: int
    league_code: str
    draft_completed: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Team Schemas
class TeamBase(BaseModel):
    name: str

class TeamCreate(TeamBase):
    league_id: int

class Team(TeamBase):
    id: int
    user_id: int
    league_id: int
    total_points: float
    
    class Config:
        from_attributes = True