from app.database import SessionLocal
from app.models import Player

def seed_players():
    db = SessionLocal()
    
    # Check if players already exist
    existing = db.query(Player).first()
    if existing:
        print("Players already seeded!")
        db.close()
        return
    
    # Sample NBA players with stats
    players = [
        {"name": "LeBron James", "position": "SF", "nba_team": "Lakers", "points_per_game": 25.7, "rebounds_per_game": 7.3, "assists_per_game": 8.3, "steals_per_game": 1.3, "blocks_per_game": 0.5, "fantasy_points": 45.2},
        {"name": "Stephen Curry", "position": "PG", "nba_team": "Warriors", "points_per_game": 26.4, "rebounds_per_game": 4.5, "assists_per_game": 5.1, "steals_per_game": 0.7, "blocks_per_game": 0.4, "fantasy_points": 42.8},
        {"name": "Giannis Antetokounmpo", "position": "PF", "nba_team": "Bucks", "points_per_game": 30.4, "rebounds_per_game": 11.5, "assists_per_game": 6.5, "steals_per_game": 1.2, "blocks_per_game": 1.1, "fantasy_points": 53.7},
        {"name": "Kevin Durant", "position": "SF", "nba_team": "Suns", "points_per_game": 27.1, "rebounds_per_game": 6.7, "assists_per_game": 5.0, "steals_per_game": 0.9, "blocks_per_game": 1.3, "fantasy_points": 44.5},
        {"name": "Nikola Jokic", "position": "C", "nba_team": "Nuggets", "points_per_game": 26.4, "rebounds_per_game": 12.4, "assists_per_game": 9.0, "steals_per_game": 1.3, "blocks_per_game": 0.7, "fantasy_points": 54.2},
        {"name": "Luka Doncic", "position": "PG", "nba_team": "Mavericks", "points_per_game": 28.4, "rebounds_per_game": 9.1, "assists_per_game": 8.7, "steals_per_game": 1.4, "blocks_per_game": 0.5, "fantasy_points": 51.8},
        {"name": "Joel Embiid", "position": "C", "nba_team": "76ers", "points_per_game": 33.1, "rebounds_per_game": 10.2, "assists_per_game": 4.2, "steals_per_game": 1.0, "blocks_per_game": 1.7, "fantasy_points": 54.3},
        {"name": "Jayson Tatum", "position": "SF", "nba_team": "Celtics", "points_per_game": 26.9, "rebounds_per_game": 8.1, "assists_per_game": 4.9, "steals_per_game": 1.1, "blocks_per_game": 0.7, "fantasy_points": 44.9},
        {"name": "Damian Lillard", "position": "PG", "nba_team": "Bucks", "points_per_game": 24.3, "rebounds_per_game": 4.4, "assists_per_game": 7.0, "steals_per_game": 1.0, "blocks_per_game": 0.3, "fantasy_points": 40.5},
        {"name": "Anthony Davis", "position": "PF", "nba_team": "Lakers", "points_per_game": 24.7, "rebounds_per_game": 12.6, "assists_per_game": 3.5, "steals_per_game": 1.1, "blocks_per_game": 2.0, "fantasy_points": 47.4},
    ]
    
    for player_data in players:
        player = Player(**player_data)
        db.add(player)
    
    db.commit()
    print(f"Successfully added {len(players)} players!")
    db.close()

if __name__ == "__main__":
    seed_players()
