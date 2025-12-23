from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

# Association table for many-to-many relationship (teams and players)
team_players = Table(
    'team_players',
    Base.metadata,
    Column('team_id', Integer, ForeignKey('teams.id')),
    Column('player_id', Integer, ForeignKey('players.id'))
)

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    teams = relationship("Team", back_populates="owner")

class League(Base):
    __tablename__ = "leagues"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    league_code = Column(String, unique=True, index=True)
    max_teams = Column(Integer, default=10)
    draft_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    teams = relationship("Team", back_populates="league")

class Team(Base):
    __tablename__ = "teams"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    league_id = Column(Integer, ForeignKey("leagues.id"))
    total_points = Column(Float, default=0.0)
    
    owner = relationship("User", back_populates="teams")
    league = relationship("League", back_populates="teams")
    players = relationship("Player", secondary=team_players, back_populates="teams")

class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    position = Column(String)  # PG, SG, SF, PF, C
    nba_team = Column(String)
    points_per_game = Column(Float, default=0.0)
    rebounds_per_game = Column(Float, default=0.0)
    assists_per_game = Column(Float, default=0.0)
    steals_per_game = Column(Float, default=0.0)
    blocks_per_game = Column(Float, default=0.0)
    fantasy_points = Column(Float, default=0.0)
    is_available = Column(Boolean, default=True)
    
    teams = relationship("Team", secondary=team_players, back_populates="players")