from app.database import SessionLocal
from app.models import Player

def add_all_nba_players():
    """Add comprehensive list of NBA players across all teams"""
    
    db = SessionLocal()
    
    print(f"Current players in database: {db.query(Player).count()}")
    
    # Comprehensive NBA player list with realistic stats
    all_players = [
        # Atlanta Hawks
        {"name": "Trae Young", "position": "PG", "nba_team": "Hawks", "ppg": 26.4, "rpg": 2.8, "apg": 10.8, "spg": 1.3, "bpg": 0.2, "fp": 45.0},
        {"name": "Dejounte Murray", "position": "PG", "nba_team": "Hawks", "ppg": 20.5, "rpg": 5.3, "apg": 6.1, "spg": 1.5, "bpg": 0.3, "fp": 38.0},
        {"name": "Clint Capela", "position": "C", "nba_team": "Hawks", "ppg": 11.5, "rpg": 10.6, "apg": 0.9, "spg": 0.7, "bpg": 1.5, "fp": 29.0},
        {"name": "Bogdan Bogdanovic", "position": "SG", "nba_team": "Hawks", "ppg": 16.9, "rpg": 3.4, "apg": 3.1, "spg": 1.0, "bpg": 0.2, "fp": 28.0},
        
        # Boston Celtics
        {"name": "Kristaps Porzingis", "position": "PF", "nba_team": "Celtics", "ppg": 20.1, "rpg": 7.2, "apg": 1.9, "spg": 0.8, "bpg": 1.9, "fp": 36.0},
        {"name": "Derrick White", "position": "PG", "nba_team": "Celtics", "ppg": 15.2, "rpg": 4.2, "apg": 5.2, "spg": 1.0, "bpg": 1.2, "fp": 31.0},
        {"name": "Jrue Holiday", "position": "PG", "nba_team": "Celtics", "ppg": 12.5, "rpg": 5.4, "apg": 6.5, "spg": 1.5, "bpg": 0.5, "fp": 31.0},
        
        # Brooklyn Nets
        {"name": "Mikal Bridges", "position": "SF", "nba_team": "Nets", "ppg": 21.2, "rpg": 4.3, "apg": 3.3, "spg": 1.0, "bpg": 0.5, "fp": 35.0},
        {"name": "Cam Thomas", "position": "SG", "nba_team": "Nets", "ppg": 22.5, "rpg": 3.2, "apg": 2.9, "spg": 0.8, "bpg": 0.6, "fp": 34.0},
        {"name": "Nic Claxton", "position": "C", "nba_team": "Nets", "ppg": 11.8, "rpg": 9.9, "apg": 2.1, "spg": 0.8, "bpg": 2.1, "fp": 31.0},
        {"name": "Spencer Dinwiddie", "position": "PG", "nba_team": "Nets", "ppg": 12.6, "rpg": 3.0, "apg": 6.0, "spg": 0.5, "bpg": 0.3, "fp": 26.0},
        
        # Charlotte Hornets
        {"name": "LaMelo Ball", "position": "PG", "nba_team": "Hornets", "ppg": 23.9, "rpg": 5.1, "apg": 8.0, "spg": 1.8, "bpg": 0.2, "fp": 43.0},
        {"name": "Terry Rozier", "position": "PG", "nba_team": "Hornets", "ppg": 21.4, "rpg": 4.2, "apg": 4.3, "spg": 1.1, "bpg": 0.3, "fp": 36.0},
        {"name": "Miles Bridges", "position": "SF", "nba_team": "Hornets", "ppg": 19.6, "rpg": 7.0, "apg": 3.6, "spg": 1.0, "bpg": 0.7, "fp": 36.0},
        {"name": "Mark Williams", "position": "C", "nba_team": "Hornets", "ppg": 12.7, "rpg": 9.7, "apg": 1.3, "spg": 0.6, "bpg": 1.1, "fp": 29.0},
        
        # Chicago Bulls
        {"name": "DeMar DeRozan", "position": "SF", "nba_team": "Bulls", "ppg": 24.0, "rpg": 4.3, "apg": 5.3, "spg": 1.1, "bpg": 0.6, "fp": 40.0},
        {"name": "Zach LaVine", "position": "SG", "nba_team": "Bulls", "ppg": 24.8, "rpg": 4.5, "apg": 4.2, "spg": 0.9, "bpg": 0.4, "fp": 39.0},
        {"name": "Nikola Vucevic", "position": "C", "nba_team": "Bulls", "ppg": 17.5, "rpg": 11.0, "apg": 3.2, "spg": 0.8, "bpg": 0.7, "fp": 38.0},
        {"name": "Coby White", "position": "PG", "nba_team": "Bulls", "ppg": 19.1, "rpg": 4.5, "apg": 5.1, "spg": 1.0, "bpg": 0.9, "fp": 35.0},
        
        # Cleveland Cavaliers
        {"name": "Darius Garland", "position": "PG", "nba_team": "Cavaliers", "ppg": 18.0, "rpg": 2.7, "apg": 6.5, "spg": 1.3, "bpg": 0.1, "fp": 33.0},
        {"name": "Evan Mobley", "position": "PF", "nba_team": "Cavaliers", "ppg": 15.7, "rpg": 9.4, "apg": 3.2, "spg": 0.9, "bpg": 1.5, "fp": 35.0},
        {"name": "Caris LeVert", "position": "SG", "nba_team": "Cavaliers", "ppg": 14.0, "rpg": 3.9, "apg": 4.8, "spg": 1.1, "bpg": 0.4, "fp": 29.0},
        
        # Dallas Mavericks
        {"name": "Derrick Jones Jr.", "position": "SF", "nba_team": "Mavericks", "ppg": 8.6, "rpg": 3.3, "apg": 1.0, "spg": 0.9, "bpg": 0.5, "fp": 18.0},
        {"name": "Josh Green", "position": "SG", "nba_team": "Mavericks", "ppg": 9.1, "rpg": 3.0, "apg": 1.9, "spg": 0.9, "bpg": 0.3, "fp": 19.0},
        {"name": "Daniel Gafford", "position": "C", "nba_team": "Mavericks", "ppg": 11.0, "rpg": 7.6, "apg": 1.1, "spg": 0.6, "bpg": 2.1, "fp": 26.0},
        
        # Denver Nuggets
        {"name": "Michael Porter Jr.", "position": "SF", "nba_team": "Nuggets", "ppg": 16.7, "rpg": 7.0, "apg": 1.5, "spg": 0.7, "bpg": 0.6, "fp": 30.0},
        {"name": "Aaron Gordon", "position": "PF", "nba_team": "Nuggets", "ppg": 13.9, "rpg": 6.5, "apg": 3.5, "spg": 0.7, "bpg": 0.7, "fp": 30.0},
        {"name": "Kentavious Caldwell-Pope", "position": "SG", "nba_team": "Nuggets", "ppg": 10.1, "rpg": 2.4, "apg": 2.4, "spg": 1.5, "bpg": 0.5, "fp": 21.0},
        
        # Detroit Pistons
        {"name": "Cade Cunningham", "position": "PG", "nba_team": "Pistons", "ppg": 22.7, "rpg": 4.3, "apg": 7.5, "spg": 1.0, "bpg": 0.7, "fp": 41.0},
        {"name": "Jaden Ivey", "position": "SG", "nba_team": "Pistons", "ppg": 15.4, "rpg": 3.8, "apg": 5.2, "spg": 1.2, "bpg": 0.7, "fp": 31.0},
        {"name": "Jalen Duren", "position": "C", "nba_team": "Pistons", "ppg": 13.8, "rpg": 11.6, "apg": 2.9, "spg": 0.9, "bpg": 0.8, "fp": 34.0},
        {"name": "Bojan Bogdanovic", "position": "SF", "nba_team": "Pistons", "ppg": 20.2, "rpg": 3.8, "apg": 2.6, "spg": 0.8, "bpg": 0.2, "fp": 32.0},
        
        # Golden State Warriors
        {"name": "Andrew Wiggins", "position": "SF", "nba_team": "Warriors", "ppg": 13.2, "rpg": 4.5, "apg": 1.7, "spg": 1.2, "bpg": 0.7, "fp": 26.0},
        {"name": "Draymond Green", "position": "PF", "nba_team": "Warriors", "ppg": 8.6, "rpg": 7.2, "apg": 6.0, "spg": 0.8, "bpg": 0.8, "fp": 28.0},
        {"name": "Jonathan Kuminga", "position": "PF", "nba_team": "Warriors", "ppg": 16.1, "rpg": 4.8, "apg": 2.2, "spg": 0.7, "bpg": 0.5, "fp": 29.0},
        
        # Houston Rockets
        {"name": "Alperen Sengun", "position": "C", "nba_team": "Rockets", "ppg": 21.1, "rpg": 9.3, "apg": 5.0, "spg": 0.9, "bpg": 0.7, "fp": 42.0},
        {"name": "Jalen Green", "position": "SG", "nba_team": "Rockets", "ppg": 19.6, "rpg": 5.2, "apg": 3.5, "spg": 0.8, "bpg": 0.7, "fp": 34.0},
        {"name": "Fred VanVleet", "position": "PG", "nba_team": "Rockets", "ppg": 17.4, "rpg": 3.8, "apg": 8.1, "spg": 1.4, "bpg": 0.4, "fp": 36.0},
        {"name": "Jabari Smith Jr.", "position": "PF", "nba_team": "Rockets", "ppg": 13.7, "rpg": 8.1, "apg": 1.6, "spg": 0.8, "bpg": 1.1, "fp": 29.0},
        
        # Indiana Pacers
        {"name": "Tyrese Haliburton", "position": "PG", "nba_team": "Pacers", "ppg": 20.1, "rpg": 3.9, "apg": 10.9, "spg": 1.2, "bpg": 0.7, "fp": 42.0},
        {"name": "Myles Turner", "position": "C", "nba_team": "Pacers", "ppg": 17.1, "rpg": 6.9, "apg": 1.3, "spg": 0.6, "bpg": 2.3, "fp": 33.0},
        {"name": "Pascal Siakam", "position": "PF", "nba_team": "Pacers", "ppg": 21.3, "rpg": 7.8, "apg": 3.7, "spg": 0.7, "bpg": 0.3, "fp": 38.0},
        {"name": "Bennedict Mathurin", "position": "SG", "nba_team": "Pacers", "ppg": 14.5, "rpg": 4.0, "apg": 1.7, "spg": 0.8, "bpg": 0.3, "fp": 26.0},
        
        # LA Clippers
        {"name": "James Harden", "position": "PG", "nba_team": "Clippers", "ppg": 16.6, "rpg": 5.1, "apg": 8.5, "spg": 1.1, "bpg": 0.8, "fp": 37.0},
        {"name": "Russell Westbrook", "position": "PG", "nba_team": "Clippers", "ppg": 11.1, "rpg": 5.0, "apg": 4.5, "spg": 0.9, "bpg": 0.3, "fp": 26.0},
        {"name": "Norman Powell", "position": "SG", "nba_team": "Clippers", "ppg": 13.9, "rpg": 2.6, "apg": 1.3, "spg": 0.9, "bpg": 0.4, "fp": 23.0},
        
        # LA Lakers
        {"name": "D'Angelo Russell", "position": "PG", "nba_team": "Lakers", "ppg": 18.0, "rpg": 3.1, "apg": 6.3, "spg": 0.9, "bpg": 0.3, "fp": 33.0},
        {"name": "Austin Reaves", "position": "SG", "nba_team": "Lakers", "ppg": 15.9, "rpg": 5.5, "apg": 5.5, "spg": 0.8, "bpg": 0.4, "fp": 32.0},
        {"name": "Rui Hachimura", "position": "PF", "nba_team": "Lakers", "ppg": 13.6, "rpg": 4.3, "apg": 1.2, "spg": 0.7, "bpg": 0.4, "fp": 24.0},
        
        # Memphis Grizzlies
        {"name": "Ja Morant", "position": "PG", "nba_team": "Grizzlies", "ppg": 25.1, "rpg": 5.6, "apg": 8.1, "spg": 1.1, "bpg": 0.3, "fp": 44.0},
        {"name": "Jaren Jackson Jr.", "position": "PF", "nba_team": "Grizzlies", "ppg": 22.5, "rpg": 5.5, "apg": 2.3, "spg": 1.0, "bpg": 1.6, "fp": 38.0},
        {"name": "Desmond Bane", "position": "SG", "nba_team": "Grizzlies", "ppg": 23.7, "rpg": 5.5, "apg": 5.3, "spg": 1.1, "bpg": 0.8, "fp": 41.0},
        {"name": "Marcus Smart", "position": "PG", "nba_team": "Grizzlies", "ppg": 14.5, "rpg": 2.7, "apg": 4.3, "spg": 1.8, "bpg": 0.3, "fp": 28.0},
        
        # Miami Heat
        {"name": "Tyler Herro", "position": "SG", "nba_team": "Heat", "ppg": 20.8, "rpg": 5.3, "apg": 4.5, "spg": 0.8, "bpg": 0.1, "fp": 36.0},
        {"name": "Kyle Lowry", "position": "PG", "nba_team": "Heat", "ppg": 8.2, "rpg": 3.2, "apg": 4.0, "spg": 0.9, "bpg": 0.2, "fp": 20.0},
        {"name": "Duncan Robinson", "position": "SG", "nba_team": "Heat", "ppg": 12.9, "rpg": 2.9, "apg": 1.5, "spg": 0.5, "bpg": 0.3, "fp": 22.0},
        
        # Milwaukee Bucks
        {"name": "Brook Lopez", "position": "C", "nba_team": "Bucks", "ppg": 11.9, "rpg": 5.2, "apg": 1.6, "spg": 0.6, "bpg": 2.4, "fp": 26.0},
        {"name": "Khris Middleton", "position": "SF", "nba_team": "Bucks", "ppg": 15.1, "rpg": 4.7, "apg": 5.3, "spg": 0.8, "bpg": 0.2, "fp": 31.0},
        {"name": "Bobby Portis", "position": "PF", "nba_team": "Bucks", "ppg": 13.8, "rpg": 7.8, "apg": 1.2, "spg": 0.6, "bpg": 0.4, "fp": 28.0},
        
        # Minnesota Timberwolves
        {"name": "Rudy Gobert", "position": "C", "nba_team": "Timberwolves", "ppg": 14.0, "rpg": 12.9, "apg": 1.3, "spg": 0.7, "bpg": 2.1, "fp": 36.0},
        {"name": "Mike Conley", "position": "PG", "nba_team": "Timberwolves", "ppg": 10.9, "rpg": 2.5, "apg": 5.9, "spg": 0.8, "bpg": 0.3, "fp": 24.0},
        {"name": "Jaden McDaniels", "position": "SF", "nba_team": "Timberwolves", "ppg": 10.5, "rpg": 3.9, "apg": 1.8, "spg": 1.2, "bpg": 0.9, "fp": 23.0},
        
        # New Orleans Pelicans
        {"name": "CJ McCollum", "position": "SG", "nba_team": "Pelicans", "ppg": 20.0, "rpg": 4.4, "apg": 4.6, "spg": 1.0, "bpg": 0.4, "fp": 35.0},
        {"name": "Jonas Valanciunas", "position": "C", "nba_team": "Pelicans", "ppg": 12.2, "rpg": 8.8, "apg": 2.1, "spg": 0.6, "bpg": 0.8, "fp": 29.0},
        {"name": "Herb Jones", "position": "SF", "nba_team": "Pelicans", "ppg": 9.8, "rpg": 3.6, "apg": 2.6, "spg": 1.4, "bpg": 0.9, "fp": 23.0},
        
        # New York Knicks
        {"name": "RJ Barrett", "position": "SF", "nba_team": "Knicks", "ppg": 18.2, "rpg": 4.3, "apg": 2.8, "spg": 0.9, "bpg": 0.4, "fp": 31.0},
        {"name": "Mitchell Robinson", "position": "C", "nba_team": "Knicks", "ppg": 8.5, "rpg": 8.5, "apg": 0.8, "spg": 0.6, "bpg": 1.8, "fp": 24.0},
        {"name": "Immanuel Quickley", "position": "PG", "nba_team": "Knicks", "ppg": 15.0, "rpg": 4.2, "apg": 3.5, "spg": 0.8, "bpg": 0.3, "fp": 28.0},
        
        # Oklahoma City Thunder
        {"name": "Jalen Williams", "position": "SF", "nba_team": "Thunder", "ppg": 19.1, "rpg": 4.0, "apg": 4.5, "spg": 1.1, "bpg": 0.7, "fp": 34.0},
        {"name": "Josh Giddey", "position": "PG", "nba_team": "Thunder", "ppg": 12.3, "rpg": 7.8, "apg": 6.2, "spg": 0.8, "bpg": 0.6, "fp": 32.0},
        {"name": "Luguentz Dort", "position": "SG", "nba_team": "Thunder", "ppg": 10.9, "rpg": 3.0, "apg": 1.7, "spg": 1.0, "bpg": 0.4, "fp": 21.0},
        
        # Orlando Magic
        {"name": "Paolo Banchero", "position": "PF", "nba_team": "Magic", "ppg": 20.0, "rpg": 6.9, "apg": 3.7, "spg": 0.8, "bpg": 0.7, "fp": 37.0},
        {"name": "Franz Wagner", "position": "SF", "nba_team": "Magic", "ppg": 19.7, "rpg": 5.3, "apg": 3.7, "spg": 1.1, "bpg": 0.6, "fp": 35.0},
        {"name": "Wendell Carter Jr.", "position": "C", "nba_team": "Magic", "ppg": 15.2, "rpg": 9.0, "apg": 2.9, "spg": 0.9, "bpg": 0.8, "fp": 33.0},
        {"name": "Markelle Fultz", "position": "PG", "nba_team": "Magic", "ppg": 14.0, "rpg": 3.9, "apg": 5.7, "spg": 1.2, "bpg": 0.4, "fp": 29.0},
        
        # Philadelphia 76ers
        {"name": "Tobias Harris", "position": "PF", "nba_team": "76ers", "ppg": 17.2, "rpg": 5.5, "apg": 3.5, "spg": 1.0, "bpg": 0.6, "fp": 32.0},
        {"name": "De'Anthony Melton", "position": "SG", "nba_team": "76ers", "ppg": 11.1, "rpg": 3.7, "apg": 3.0, "spg": 1.6, "bpg": 0.8, "fp": 25.0},
        {"name": "Kelly Oubre Jr.", "position": "SF", "nba_team": "76ers", "ppg": 15.4, "rpg": 5.0, "apg": 1.4, "spg": 1.1, "bpg": 0.7, "fp": 28.0},
        
        # Phoenix Suns
        {"name": "Bradley Beal", "position": "SG", "nba_team": "Suns", "ppg": 18.2, "rpg": 4.4, "apg": 5.0, "spg": 1.0, "bpg": 0.4, "fp": 34.0},
        {"name": "Jusuf Nurkic", "position": "C", "nba_team": "Suns", "ppg": 10.9, "rpg": 11.0, "apg": 4.0, "spg": 0.8, "bpg": 1.1, "fp": 32.0},
        {"name": "Grayson Allen", "position": "SG", "nba_team": "Suns", "ppg": 11.5, "rpg": 3.9, "apg": 3.0, "spg": 0.9, "bpg": 0.4, "fp": 24.0},
        
        # Portland Trail Blazers
        {"name": "Anfernee Simons", "position": "PG", "nba_team": "Trail Blazers", "ppg": 22.6, "rpg": 2.6, "apg": 5.5, "spg": 0.8, "bpg": 0.3, "fp": 36.0},
        {"name": "Jerami Grant", "position": "PF", "nba_team": "Trail Blazers", "ppg": 21.0, "rpg": 3.5, "apg": 2.4, "spg": 0.9, "bpg": 0.9, "fp": 34.0},
        {"name": "Deandre Ayton", "position": "C", "nba_team": "Trail Blazers", "ppg": 14.0, "rpg": 10.5, "apg": 1.7, "spg": 0.6, "bpg": 0.9, "fp": 32.0},
        {"name": "Shaedon Sharpe", "position": "SG", "nba_team": "Trail Blazers", "ppg": 15.9, "rpg": 5.0, "apg": 2.9, "spg": 0.9, "bpg": 0.6, "fp": 30.0},
        
        # Sacramento Kings
        {"name": "Keegan Murray", "position": "PF", "nba_team": "Kings", "ppg": 15.2, "rpg": 5.5, "apg": 1.9, "spg": 1.0, "bpg": 0.6, "fp": 29.0},
        {"name": "Kevin Huerter", "position": "SG", "nba_team": "Kings", "ppg": 10.2, "rpg": 3.5, "apg": 2.2, "spg": 0.7, "bpg": 0.3, "fp": 21.0},
        {"name": "Harrison Barnes", "position": "SF", "nba_team": "Kings", "ppg": 15.0, "rpg": 4.5, "apg": 1.6, "spg": 0.7, "bpg": 0.3, "fp": 26.0},
        
        # San Antonio Spurs
        {"name": "Victor Wembanyama", "position": "C", "nba_team": "Spurs", "ppg": 21.4, "rpg": 10.6, "apg": 3.9, "spg": 1.2, "bpg": 3.6, "fp": 48.0},
        {"name": "Devin Vassell", "position": "SG", "nba_team": "Spurs", "ppg": 19.5, "rpg": 4.1, "apg": 4.5, "spg": 1.1, "bpg": 0.6, "fp": 35.0},
        {"name": "Keldon Johnson", "position": "SF", "nba_team": "Spurs", "ppg": 15.7, "rpg": 5.5, "apg": 2.8, "spg": 0.9, "bpg": 0.4, "fp": 30.0},
        {"name": "Tre Jones", "position": "PG", "nba_team": "Spurs", "ppg": 10.0, "rpg": 3.3, "apg": 6.2, "spg": 1.1, "bpg": 0.2, "fp": 25.0},
        
        # Toronto Raptors
        {"name": "Scottie Barnes", "position": "SF", "nba_team": "Raptors", "ppg": 19.9, "rpg": 8.2, "apg": 6.1, "spg": 1.3, "bpg": 1.5, "fp": 42.0},
        {"name": "Pascal Siakam", "position": "PF", "nba_team": "Raptors", "ppg": 24.2, "rpg": 7.8, "apg": 5.8, "spg": 0.9, "bpg": 0.4, "fp": 44.0},
        {"name": "OG Anunoby", "position": "SF", "nba_team": "Raptors", "ppg": 16.8, "rpg": 5.0, "apg": 2.6, "spg": 1.9, "bpg": 0.7, "fp": 32.0},
        {"name": "Jakob Poeltl", "position": "C", "nba_team": "Raptors", "ppg": 11.1, "rpg": 8.6, "apg": 2.9, "spg": 0.7, "bpg": 1.5, "fp": 29.0},
        
        # Utah Jazz
        {"name": "Lauri Markkanen", "position": "PF", "nba_team": "Jazz", "ppg": 23.5, "rpg": 8.6, "apg": 1.9, "spg": 0.9, "bpg": 0.6, "fp": 40.0},
        {"name": "Jordan Clarkson", "position": "SG", "nba_team": "Jazz", "ppg": 17.1, "rpg": 3.4, "apg": 5.0, "spg": 0.9, "bpg": 0.3, "fp": 31.0},
        {"name": "Walker Kessler", "position": "C", "nba_team": "Jazz", "ppg": 9.2, "rpg": 8.4, "apg": 1.0, "spg": 0.7, "bpg": 2.3, "fp": 26.0},
        {"name": "Collin Sexton", "position": "PG", "nba_team": "Jazz", "ppg": 18.7, "rpg": 2.5, "apg": 4.9, "spg": 0.7, "bpg": 0.2, "fp": 31.0},
        
        # Washington Wizards
        {"name": "Kyle Kuzma", "position": "PF", "nba_team": "Wizards", "ppg": 21.2, "rpg": 6.6, "apg": 4.2, "spg": 0.5, "bpg": 0.5, "fp": 38.0},
        {"name": "Jordan Poole", "position": "PG", "nba_team": "Wizards", "ppg": 17.4, "rpg": 2.7, "apg": 4.4, "spg": 0.9, "bpg": 0.2, "fp": 30.0},
        {"name": "Tyus Jones", "position": "PG", "nba_team": "Wizards", "ppg": 12.0, "rpg": 2.7, "apg": 7.3, "spg": 1.1, "bpg": 0.3, "fp": 28.0},
        {"name": "Daniel Gafford", "position": "C", "nba_team": "Wizards", "ppg": 11.0, "rpg": 7.6, "apg": 1.1, "spg": 0.6, "bpg": 2.1, "fp": 27.0},
    ]
    
    added_count = 0
    skipped_count = 0
    
    for player_data in all_players:
        # Check if player already exists
        existing_player = db.query(Player).filter(Player.name == player_data["name"]).first()
        if existing_player:
            print(f"⏭️  Skipping {player_data['name']} - already exists")
            skipped_count += 1
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
        print(f"✅ Added: {player_data['name']} - {player_data['nba_team']}")
    
    db.commit()
    
    total = db.query(Player).count()
    
    print(f"\n{'='*60}")
    print(f"✅ Successfully added {added_count} new NBA players!")
    print(f"⏭️  Skipped {skipped_count} existing players")
    print(f"🏀 Total players in database: {total}")
    print(f"{'='*60}")
    
    db.close()

if __name__ == "__main__":
    add_all_nba_players()