from app.database import SessionLocal
from app.models import Player

def add_nba_players():
    """Add more real NBA players to the database"""
    
    db = SessionLocal()
    
    # Check existing count
    existing = db.query(Player).count()
    print(f"Current players in database: {existing}")
    
    # Real NBA players with realistic 2024-25 stats
    nba_players = [
        # Lakers
        {"name": "LeBron James", "position": "SF", "nba_team": "Lakers", "ppg": 25.0, "rpg": 7.5, "apg": 7.8, "spg": 1.3, "bpg": 0.6, "fp": 45.0},
        {"name": "Anthony Davis", "position": "PF", "nba_team": "Lakers", "ppg": 27.8, "rpg": 11.6, "apg": 3.5, "spg": 1.2, "bpg": 2.3, "fp": 52.0},
        
        # Warriors
        {"name": "Stephen Curry", "position": "PG", "nba_team": "Warriors", "ppg": 26.4, "rpg": 4.5, "apg": 5.1, "spg": 0.7, "bpg": 0.4, "fp": 42.0},
        {"name": "Klay Thompson", "position": "SG", "nba_team": "Warriors", "ppg": 17.9, "rpg": 3.3, "apg": 2.3, "spg": 0.6, "bpg": 0.5, "fp": 28.0},
        
        # Bucks
        {"name": "Giannis Antetokounmpo", "position": "PF", "nba_team": "Bucks", "ppg": 30.4, "rpg": 11.5, "apg": 6.5, "spg": 1.2, "bpg": 1.1, "fp": 54.0},
        {"name": "Damian Lillard", "position": "PG", "nba_team": "Bucks", "ppg": 25.0, "rpg": 4.3, "apg": 7.0, "spg": 1.0, "bpg": 0.3, "fp": 41.0},
        
        # Mavericks
        {"name": "Luka Doncic", "position": "PG", "nba_team": "Mavericks", "ppg": 28.4, "rpg": 9.1, "apg": 8.7, "spg": 1.4, "bpg": 0.5, "fp": 52.0},
        {"name": "Kyrie Irving", "position": "PG", "nba_team": "Mavericks", "ppg": 25.6, "rpg": 5.0, "apg": 5.2, "spg": 1.3, "bpg": 0.5, "fp": 42.0},
        
        # 76ers
        {"name": "Joel Embiid", "position": "C", "nba_team": "76ers", "ppg": 34.7, "rpg": 11.0, "apg": 5.6, "spg": 1.2, "bpg": 1.7, "fp": 58.0},
        {"name": "Tyrese Maxey", "position": "PG", "nba_team": "76ers", "ppg": 25.9, "rpg": 3.7, "apg": 6.2, "spg": 1.0, "bpg": 0.5, "fp": 42.0},
        
        # Celtics
        {"name": "Jayson Tatum", "position": "SF", "nba_team": "Celtics", "ppg": 26.9, "rpg": 8.1, "apg": 4.9, "spg": 1.1, "bpg": 0.7, "fp": 45.0},
        {"name": "Jaylen Brown", "position": "SG", "nba_team": "Celtics", "ppg": 23.0, "rpg": 5.5, "apg": 3.6, "spg": 1.2, "bpg": 0.4, "fp": 38.0},
        
        # Nuggets  
        {"name": "Nikola Jokic", "position": "C", "nba_team": "Nuggets", "ppg": 26.4, "rpg": 12.4, "apg": 9.0, "spg": 1.4, "bpg": 0.9, "fp": 55.0},
        {"name": "Jamal Murray", "position": "PG", "nba_team": "Nuggets", "ppg": 21.2, "rpg": 4.1, "apg": 6.5, "spg": 1.0, "bpg": 0.3, "fp": 37.0},
        
        # Suns
        {"name": "Kevin Durant", "position": "SF", "nba_team": "Suns", "ppg": 27.1, "rpg": 6.7, "apg": 5.0, "spg": 0.9, "bpg": 1.3, "fp": 45.0},
        {"name": "Devin Booker", "position": "SG", "nba_team": "Suns", "ppg": 27.1, "rpg": 4.5, "apg": 6.9, "spg": 0.9, "bpg": 0.5, "fp": 44.0},
        
        # Heat
        {"name": "Jimmy Butler", "position": "SF", "nba_team": "Heat", "ppg": 20.8, "rpg": 5.3, "apg": 5.0, "spg": 1.3, "bpg": 0.4, "fp": 37.0},
        {"name": "Bam Adebayo", "position": "C", "nba_team": "Heat", "ppg": 19.3, "rpg": 10.4, "apg": 3.9, "spg": 1.2, "bpg": 0.9, "fp": 40.0},
        
        # Thunder
        {"name": "Shai Gilgeous-Alexander", "position": "PG", "nba_team": "Thunder", "ppg": 30.1, "rpg": 5.5, "apg": 6.2, "spg": 2.0, "bpg": 0.9, "fp": 50.0},
        {"name": "Chet Holmgren", "position": "C", "nba_team": "Thunder", "ppg": 16.5, "rpg": 7.9, "apg": 2.4, "spg": 0.6, "bpg": 2.3, "fp": 35.0},
        
        # Timberwolves
        {"name": "Anthony Edwards", "position": "SG", "nba_team": "Timberwolves", "ppg": 25.9, "rpg": 5.4, "apg": 5.1, "spg": 1.3, "bpg": 0.5, "fp": 42.0},
        {"name": "Karl-Anthony Towns", "position": "C", "nba_team": "Timberwolves", "ppg": 21.8, "rpg": 8.3, "apg": 3.0, "spg": 0.7, "bpg": 0.7, "fp": 39.0},
        
        # Kings
        {"name": "De'Aaron Fox", "position": "PG", "nba_team": "Kings", "ppg": 26.6, "rpg": 4.6, "apg": 5.6, "spg": 2.0, "bpg": 0.4, "fp": 43.0},
        {"name": "Domantas Sabonis", "position": "C", "nba_team": "Kings", "ppg": 19.4, "rpg": 13.7, "apg": 8.2, "spg": 0.9, "bpg": 0.6, "fp": 47.0},
        
        # Knicks
        {"name": "Jalen Brunson", "position": "PG", "nba_team": "Knicks", "ppg": 28.7, "rpg": 3.6, "apg": 6.7, "spg": 0.9, "bpg": 0.2, "fp": 44.0},
        {"name": "Julius Randle", "position": "PF", "nba_team": "Knicks", "ppg": 24.0, "rpg": 9.2, "apg": 5.0, "spg": 0.5, "bpg": 0.3, "fp": 43.0},
        
        # Clippers
        {"name": "Kawhi Leonard", "position": "SF", "nba_team": "Clippers", "ppg": 23.7, "rpg": 6.1, "apg": 3.6, "spg": 1.6, "bpg": 0.9, "fp": 40.0},
        {"name": "Paul George", "position": "SF", "nba_team": "Clippers", "ppg": 22.6, "rpg": 5.2, "apg": 3.5, "spg": 1.5, "bpg": 0.4, "fp": 38.0},
        
        # Pelicans
        {"name": "Zion Williamson", "position": "PF", "nba_team": "Pelicans", "ppg": 22.9, "rpg": 5.8, "apg": 5.0, "spg": 1.1, "bpg": 0.6, "fp": 40.0},
        {"name": "Brandon Ingram", "position": "SF", "nba_team": "Pelicans", "ppg": 20.8, "rpg": 5.1, "apg": 5.7, "spg": 0.8, "bpg": 0.5, "fp": 37.0},
        
        # Cavaliers
        {"name": "Donovan Mitchell", "position": "SG", "nba_team": "Cavaliers", "ppg": 26.6, "rpg": 5.1, "apg": 6.1, "spg": 1.8, "bpg": 0.4, "fp": 44.0},
        {"name": "Jarrett Allen", "position": "C", "nba_team": "Cavaliers", "ppg": 16.5, "rpg": 10.5, "apg": 2.7, "spg": 0.8, "bpg": 1.1, "fp": 36.0},
    ]
    
    added_count = 0
    
    for player_data in nba_players:
        # Check if player already exists
        existing_player = db.query(Player).filter(Player.name == player_data["name"]).first()
        if existing_player:
            print(f"Skipping {player_data['name']} - already exists")
            continue
        
        player = Player(
            name=player_data["name"],
            position=player_data["position"],
            nba_team=player_data["nba_team"],
            points_per_game=player_data["ppg"],
            rebounds_per_game=player_data["rpg"],
            assists_per_game=player_data["apg"],
            steals_per_game=player_data["spg"],
            blocks_per_game=player_data["bpg"],
            fantasy_points=player_data["fp"],
            is_available=True
        )
        
        db.add(player)
        added_count += 1
        print(f"Added: {player_data['name']}")
    
    db.commit()
    print(f"\n✅ Successfully added {added_count} new NBA players!")
    print(f"Total players in database: {db.query(Player).count()}")
    db.close()

if __name__ == "__main__":
    add_nba_players()