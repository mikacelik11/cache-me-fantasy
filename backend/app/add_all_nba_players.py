from app.database import SessionLocal
from app.models import Player

def add_all_nba_players():
    db = SessionLocal()
    
    # Check if players already exist
    existing_count = db.query(Player).count()
    if existing_count > 0:
        print(f"Players already seeded ({existing_count} players in database)")
        db.close()
        return
    
    players = [
        # Atlanta Hawks
        {"name": "Trae Young", "position": "PG", "nba_team": "Atlanta Hawks", "ppg": 26.2, "rpg": 2.8, "apg": 10.8, "spg": 1.1, "bpg": 0.2, "fantasy_points": 45.5},
        {"name": "Dejounte Murray", "position": "SG", "nba_team": "Atlanta Hawks", "ppg": 20.5, "rpg": 5.3, "apg": 6.1, "spg": 1.5, "bpg": 0.3, "fantasy_points": 38.2},
        {"name": "Clint Capela", "position": "C", "nba_team": "Atlanta Hawks", "ppg": 11.5, "rpg": 10.6, "apg": 1.2, "spg": 0.8, "bpg": 1.5, "fantasy_points": 32.1},
        {"name": "De'Andre Hunter", "position": "SF", "nba_team": "Atlanta Hawks", "ppg": 15.4, "rpg": 4.8, "apg": 1.5, "spg": 0.7, "bpg": 0.4, "fantasy_points": 26.8},
        {"name": "Bogdan Bogdanovic", "position": "SG", "nba_team": "Atlanta Hawks", "ppg": 14.2, "rpg": 3.4, "apg": 3.1, "spg": 1.0, "bpg": 0.2, "fantasy_points": 25.3},
        
        # Boston Celtics
        {"name": "Jayson Tatum", "position": "SF", "nba_team": "Boston Celtics", "ppg": 27.1, "rpg": 8.4, "apg": 4.9, "spg": 1.1, "bpg": 0.7, "fantasy_points": 47.3},
        {"name": "Jaylen Brown", "position": "SG", "nba_team": "Boston Celtics", "ppg": 23.6, "rpg": 6.1, "apg": 3.5, "spg": 1.2, "bpg": 0.4, "fantasy_points": 39.8},
        {"name": "Kristaps Porzingis", "position": "C", "nba_team": "Boston Celtics", "ppg": 20.3, "rpg": 7.2, "apg": 2.0, "spg": 0.7, "bpg": 1.9, "fantasy_points": 38.4},
        {"name": "Derrick White", "position": "PG", "nba_team": "Boston Celtics", "ppg": 15.2, "rpg": 4.2, "apg": 5.2, "spg": 1.0, "bpg": 1.2, "fantasy_points": 31.5},
        {"name": "Jrue Holiday", "position": "PG", "nba_team": "Boston Celtics", "ppg": 12.5, "rpg": 5.4, "apg": 6.5, "spg": 1.3, "bpg": 0.6, "fantasy_points": 31.2},
        
        # Brooklyn Nets
        {"name": "Mikal Bridges", "position": "SF", "nba_team": "Brooklyn Nets", "ppg": 21.2, "rpg": 4.3, "apg": 3.6, "spg": 1.1, "bpg": 0.5, "fantasy_points": 35.7},
        {"name": "Cam Thomas", "position": "SG", "nba_team": "Brooklyn Nets", "ppg": 22.5, "rpg": 3.2, "apg": 2.9, "spg": 0.9, "bpg": 0.3, "fantasy_points": 33.8},
        {"name": "Nic Claxton", "position": "C", "nba_team": "Brooklyn Nets", "ppg": 11.8, "rpg": 9.9, "apg": 2.1, "spg": 0.8, "bpg": 2.1, "fantasy_points": 33.2},
        {"name": "Spencer Dinwiddie", "position": "PG", "nba_team": "Brooklyn Nets", "ppg": 12.6, "rpg": 3.4, "apg": 6.0, "spg": 0.6, "bpg": 0.3, "fantasy_points": 26.9},
        
        # Charlotte Hornets
        {"name": "LaMelo Ball", "position": "PG", "nba_team": "Charlotte Hornets", "ppg": 23.9, "rpg": 6.2, "apg": 8.0, "spg": 1.5, "bpg": 0.3, "fantasy_points": 44.4},
        {"name": "Miles Bridges", "position": "PF", "nba_team": "Charlotte Hornets", "ppg": 21.0, "rpg": 7.3, "apg": 3.8, "spg": 1.0, "bpg": 0.7, "fantasy_points": 38.3},
        {"name": "Brandon Miller", "position": "SF", "nba_team": "Charlotte Hornets", "ppg": 17.3, "rpg": 4.3, "apg": 2.4, "spg": 0.9, "bpg": 0.6, "fantasy_points": 29.5},
        {"name": "Mark Williams", "position": "C", "nba_team": "Charlotte Hornets", "ppg": 12.7, "rpg": 9.7, "apg": 1.3, "spg": 0.6, "bpg": 1.6, "fantasy_points": 31.4},
        
        # Chicago Bulls
        {"name": "Zach LaVine", "position": "SG", "nba_team": "Chicago Bulls", "ppg": 24.8, "rpg": 4.5, "apg": 4.2, "spg": 0.9, "bpg": 0.4, "fantasy_points": 39.3},
        {"name": "DeMar DeRozan", "position": "SF", "nba_team": "Chicago Bulls", "ppg": 22.3, "rpg": 4.3, "apg": 5.1, "spg": 1.1, "bpg": 0.5, "fantasy_points": 38.8},
        {"name": "Nikola Vucevic", "position": "C", "nba_team": "Chicago Bulls", "ppg": 17.5, "rpg": 10.2, "apg": 3.2, "spg": 0.9, "bpg": 0.7, "fantasy_points": 37.5},
        {"name": "Coby White", "position": "PG", "nba_team": "Chicago Bulls", "ppg": 19.1, "rpg": 4.5, "apg": 5.1, "spg": 0.9, "bpg": 0.7, "fantasy_points": 35.3},
        
        # Cleveland Cavaliers
        {"name": "Donovan Mitchell", "position": "SG", "nba_team": "Cleveland Cavaliers", "ppg": 27.6, "rpg": 5.3, "apg": 6.2, "spg": 1.8, "bpg": 0.4, "fantasy_points": 46.8},
        {"name": "Darius Garland", "position": "PG", "nba_team": "Cleveland Cavaliers", "ppg": 18.0, "rpg": 2.7, "apg": 6.5, "spg": 1.3, "bpg": 0.1, "fantasy_points": 32.6},
        {"name": "Evan Mobley", "position": "PF", "nba_team": "Cleveland Cavaliers", "ppg": 16.2, "rpg": 9.6, "apg": 3.1, "spg": 0.9, "bpg": 1.5, "fantasy_points": 37.3},
        {"name": "Jarrett Allen", "position": "C", "nba_team": "Cleveland Cavaliers", "ppg": 14.9, "rpg": 10.5, "apg": 2.7, "spg": 0.8, "bpg": 1.2, "fantasy_points": 35.6},
        
        # Dallas Mavericks
        {"name": "Luka Doncic", "position": "PG", "nba_team": "Dallas Mavericks", "ppg": 33.9, "rpg": 9.2, "apg": 9.8, "spg": 1.4, "bpg": 0.5, "fantasy_points": 60.3},
        {"name": "Kyrie Irving", "position": "PG", "nba_team": "Dallas Mavericks", "ppg": 25.6, "rpg": 5.0, "apg": 5.2, "spg": 1.3, "bpg": 0.5, "fantasy_points": 42.6},
        {"name": "Dereck Lively II", "position": "C", "nba_team": "Dallas Mavericks", "ppg": 9.2, "rpg": 7.9, "apg": 1.4, "spg": 0.7, "bpg": 1.4, "fantasy_points": 26.1},
        {"name": "Klay Thompson", "position": "SG", "nba_team": "Dallas Mavericks", "ppg": 14.0, "rpg": 3.3, "apg": 2.3, "spg": 0.6, "bpg": 0.5, "fantasy_points": 24.2},
        
        # Denver Nuggets
        {"name": "Nikola Jokic", "position": "C", "nba_team": "Denver Nuggets", "ppg": 29.7, "rpg": 13.7, "apg": 11.7, "spg": 1.3, "bpg": 0.9, "fantasy_points": 63.5},
        {"name": "Jamal Murray", "position": "PG", "nba_team": "Denver Nuggets", "ppg": 21.2, "rpg": 4.1, "apg": 6.5, "spg": 1.0, "bpg": 0.4, "fantasy_points": 37.7},
        {"name": "Michael Porter Jr.", "position": "SF", "nba_team": "Denver Nuggets", "ppg": 16.7, "rpg": 7.3, "apg": 1.5, "spg": 0.7, "bpg": 0.7, "fantasy_points": 31.4},
        {"name": "Aaron Gordon", "position": "PF", "nba_team": "Denver Nuggets", "ppg": 13.9, "rpg": 6.5, "apg": 3.5, "spg": 0.7, "bpg": 0.7, "fantasy_points": 29.8},
        
        # Detroit Pistons
        {"name": "Cade Cunningham", "position": "PG", "nba_team": "Detroit Pistons", "ppg": 22.7, "rpg": 7.5, "apg": 7.5, "spg": 1.0, "bpg": 0.9, "fantasy_points": 44.1},
        {"name": "Jaden Ivey", "position": "SG", "nba_team": "Detroit Pistons", "ppg": 15.4, "rpg": 3.8, "apg": 3.8, "spg": 0.8, "bpg": 0.4, "fantasy_points": 27.7},
        {"name": "Jalen Duren", "position": "C", "nba_team": "Detroit Pistons", "ppg": 11.6, "rpg": 9.6, "apg": 2.6, "spg": 0.7, "bpg": 1.1, "fantasy_points": 31.1},
        
        # Golden State Warriors
        {"name": "Stephen Curry", "position": "PG", "nba_team": "Golden State Warriors", "ppg": 26.4, "rpg": 4.5, "apg": 5.1, "spg": 0.7, "bpg": 0.4, "fantasy_points": 41.6},
        {"name": "Andrew Wiggins", "position": "SF", "nba_team": "Golden State Warriors", "ppg": 17.1, "rpg": 5.0, "apg": 2.3, "spg": 1.2, "bpg": 0.9, "fantasy_points": 31.0},
        {"name": "Draymond Green", "position": "PF", "nba_team": "Golden State Warriors", "ppg": 8.6, "rpg": 7.2, "apg": 6.0, "spg": 0.9, "bpg": 0.9, "fantasy_points": 28.1},
        {"name": "Jonathan Kuminga", "position": "PF", "nba_team": "Golden State Warriors", "ppg": 16.1, "rpg": 4.8, "apg": 2.2, "spg": 0.7, "bpg": 0.4, "fantasy_points": 27.7},
        
        # Houston Rockets
        {"name": "Alperen Sengun", "position": "C", "nba_team": "Houston Rockets", "ppg": 21.1, "rpg": 9.3, "apg": 5.0, "spg": 0.9, "bpg": 0.8, "fantasy_points": 42.6},
        {"name": "Jalen Green", "position": "SG", "nba_team": "Houston Rockets", "ppg": 19.6, "rpg": 5.2, "apg": 3.5, "spg": 0.8, "bpg": 0.7, "fantasy_points": 34.3},
        {"name": "Fred VanVleet", "position": "PG", "nba_team": "Houston Rockets", "ppg": 17.4, "rpg": 4.4, "apg": 8.1, "spg": 1.4, "bpg": 0.4, "fantasy_points": 36.2},
        {"name": "Jabari Smith Jr.", "position": "PF", "nba_team": "Houston Rockets", "ppg": 13.3, "rpg": 8.1, "apg": 1.5, "spg": 0.8, "bpg": 0.9, "fantasy_points": 28.1},
        
        # Indiana Pacers
        {"name": "Tyrese Haliburton", "position": "PG", "nba_team": "Indiana Pacers", "ppg": 20.1, "rpg": 3.9, "apg": 10.9, "spg": 1.2, "bpg": 0.7, "fantasy_points": 41.3},
        {"name": "Pascal Siakam", "position": "PF", "nba_team": "Indiana Pacers", "ppg": 21.3, "rpg": 7.8, "apg": 3.7, "spg": 0.9, "bpg": 0.3, "fantasy_points": 38.5},
        {"name": "Myles Turner", "position": "C", "nba_team": "Indiana Pacers", "ppg": 17.1, "rpg": 6.9, "apg": 1.5, "spg": 0.6, "bpg": 1.9, "fantasy_points": 33.5},
        {"name": "Bennedict Mathurin", "position": "SG", "nba_team": "Indiana Pacers", "ppg": 14.5, "rpg": 4.0, "apg": 2.0, "spg": 0.7, "bpg": 0.4, "fantasy_points": 25.1},
        
        # LA Clippers
        {"name": "Kawhi Leonard", "position": "SF", "nba_team": "LA Clippers", "ppg": 23.7, "rpg": 6.1, "apg": 3.6, "spg": 1.6, "bpg": 0.9, "fantasy_points": 40.4},
        {"name": "James Harden", "position": "PG", "nba_team": "LA Clippers", "ppg": 16.6, "rpg": 5.1, "apg": 8.5, "spg": 1.1, "bpg": 0.7, "fantasy_points": 36.5},
        {"name": "Paul George", "position": "SF", "nba_team": "LA Clippers", "ppg": 22.6, "rpg": 5.2, "apg": 3.5, "spg": 1.5, "bpg": 0.4, "fantasy_points": 38.7},
        {"name": "Ivica Zubac", "position": "C", "nba_team": "LA Clippers", "ppg": 11.7, "rpg": 9.2, "apg": 1.2, "spg": 0.4, "bpg": 1.0, "fantasy_points": 28.0},
        
        # LA Lakers
        {"name": "LeBron James", "position": "SF", "nba_team": "LA Lakers", "ppg": 25.7, "rpg": 7.3, "apg": 8.3, "spg": 1.3, "bpg": 0.5, "fantasy_points": 47.6},
        {"name": "Anthony Davis", "position": "PF", "nba_team": "LA Lakers", "ppg": 24.7, "rpg": 12.6, "apg": 3.5, "spg": 1.2, "bpg": 2.3, "fantasy_points": 50.8},
        {"name": "Austin Reaves", "position": "SG", "nba_team": "LA Lakers", "ppg": 15.9, "rpg": 4.3, "apg": 5.5, "spg": 0.8, "bpg": 0.4, "fantasy_points": 31.4},
        {"name": "D'Angelo Russell", "position": "PG", "nba_team": "LA Lakers", "ppg": 18.0, "rpg": 3.1, "apg": 6.3, "spg": 0.9, "bpg": 0.3, "fantasy_points": 32.6},
        
        # Memphis Grizzlies
        {"name": "Ja Morant", "position": "PG", "nba_team": "Memphis Grizzlies", "ppg": 25.1, "rpg": 5.6, "apg": 8.1, "spg": 0.9, "bpg": 0.3, "fantasy_points": 44.5},
        {"name": "Jaren Jackson Jr.", "position": "PF", "nba_team": "Memphis Grizzlies", "ppg": 22.5, "rpg": 5.5, "apg": 2.3, "spg": 0.9, "bpg": 1.6, "fantasy_points": 38.3},
        {"name": "Desmond Bane", "position": "SG", "nba_team": "Memphis Grizzlies", "ppg": 24.7, "rpg": 4.9, "apg": 4.0, "spg": 0.9, "bpg": 0.7, "fantasy_points": 39.7},
        {"name": "Marcus Smart", "position": "PG", "nba_team": "Memphis Grizzlies", "ppg": 14.5, "rpg": 3.3, "apg": 4.3, "spg": 1.8, "bpg": 0.3, "fantasy_points": 28.7},
        
        # Miami Heat
        {"name": "Jimmy Butler", "position": "SF", "nba_team": "Miami Heat", "ppg": 20.8, "rpg": 5.3, "apg": 5.0, "spg": 1.3, "bpg": 0.4, "fantasy_points": 37.3},
        {"name": "Bam Adebayo", "position": "C", "nba_team": "Miami Heat", "ppg": 19.3, "rpg": 10.4, "apg": 3.9, "spg": 1.1, "bpg": 0.9, "fantasy_points": 40.1},
        {"name": "Tyler Herro", "position": "SG", "nba_team": "Miami Heat", "ppg": 20.8, "rpg": 5.3, "apg": 4.5, "spg": 0.8, "bpg": 0.3, "fantasy_points": 36.2},
        
        # Milwaukee Bucks
        {"name": "Giannis Antetokounmpo", "position": "PF", "nba_team": "Milwaukee Bucks", "ppg": 30.4, "rpg": 11.5, "apg": 6.5, "spg": 1.2, "bpg": 1.1, "fantasy_points": 56.2},
        {"name": "Damian Lillard", "position": "PG", "nba_team": "Milwaukee Bucks", "ppg": 25.0, "rpg": 4.3, "apg": 7.0, "spg": 1.0, "bpg": 0.3, "fantasy_points": 42.1},
        {"name": "Khris Middleton", "position": "SF", "nba_team": "Milwaukee Bucks", "ppg": 15.1, "rpg": 4.7, "apg": 5.3, "spg": 0.8, "bpg": 0.2, "fantasy_points": 30.6},
        {"name": "Brook Lopez", "position": "C", "nba_team": "Milwaukee Bucks", "ppg": 12.5, "rpg": 5.2, "apg": 1.6, "spg": 0.6, "bpg": 2.4, "fantasy_points": 28.8},
        
        # Minnesota Timberwolves
        {"name": "Anthony Edwards", "position": "SG", "nba_team": "Minnesota Timberwolves", "ppg": 25.9, "rpg": 5.4, "apg": 5.1, "spg": 1.3, "bpg": 0.5, "fantasy_points": 42.7},
        {"name": "Karl-Anthony Towns", "position": "C", "nba_team": "Minnesota Timberwolves", "ppg": 21.8, "rpg": 8.3, "apg": 3.0, "spg": 0.7, "bpg": 0.7, "fantasy_points": 39.0},
        {"name": "Rudy Gobert", "position": "C", "nba_team": "Minnesota Timberwolves", "ppg": 14.0, "rpg": 12.9, "apg": 1.3, "spg": 0.7, "bpg": 2.1, "fantasy_points": 37.5},
        {"name": "Mike Conley", "position": "PG", "nba_team": "Minnesota Timberwolves", "ppg": 11.0, "rpg": 3.0, "apg": 5.9, "spg": 0.8, "bpg": 0.3, "fantasy_points": 25.5},
        
        # New Orleans Pelicans
        {"name": "Zion Williamson", "position": "PF", "nba_team": "New Orleans Pelicans", "ppg": 23.0, "rpg": 5.8, "apg": 5.0, "spg": 1.1, "bpg": 0.6, "fantasy_points": 40.0},
        {"name": "Brandon Ingram", "position": "SF", "nba_team": "New Orleans Pelicans", "ppg": 20.8, "rpg": 5.1, "apg": 5.7, "spg": 0.8, "bpg": 0.6, "fantasy_points": 37.5},
        {"name": "CJ McCollum", "position": "SG", "nba_team": "New Orleans Pelicans", "ppg": 19.2, "rpg": 4.3, "apg": 4.6, "spg": 0.9, "bpg": 0.4, "fantasy_points": 33.9},
        {"name": "Herbert Jones", "position": "SF", "nba_team": "New Orleans Pelicans", "ppg": 9.8, "rpg": 3.6, "apg": 2.6, "spg": 1.7, "bpg": 0.8, "fantasy_points": 23.0},
        
        # New York Knicks
        {"name": "Jalen Brunson", "position": "PG", "nba_team": "New York Knicks", "ppg": 28.7, "rpg": 3.6, "apg": 6.7, "spg": 0.9, "bpg": 0.2, "fantasy_points": 44.6},
        {"name": "Julius Randle", "position": "PF", "nba_team": "New York Knicks", "ppg": 24.0, "rpg": 9.2, "apg": 5.0, "spg": 0.5, "bpg": 0.3, "fantasy_points": 43.5},
        {"name": "OG Anunoby", "position": "SF", "nba_team": "New York Knicks", "ppg": 14.7, "rpg": 4.2, "apg": 2.1, "spg": 1.7, "bpg": 0.2, "fantasy_points": 27.4},
        {"name": "Mitchell Robinson", "position": "C", "nba_team": "New York Knicks", "ppg": 6.2, "rpg": 8.5, "apg": 0.5, "spg": 0.5, "bpg": 1.1, "fantasy_points": 21.3},
        
        # Oklahoma City Thunder
        {"name": "Shai Gilgeous-Alexander", "position": "PG", "nba_team": "Oklahoma City Thunder", "ppg": 30.1, "rpg": 5.5, "apg": 6.2, "spg": 2.0, "bpg": 0.9, "fantasy_points": 50.2},
        {"name": "Chet Holmgren", "position": "C", "nba_team": "Oklahoma City Thunder", "ppg": 16.5, "rpg": 7.9, "apg": 2.4, "spg": 0.6, "bpg": 2.3, "fantasy_points": 35.2},
        {"name": "Jalen Williams", "position": "SF", "nba_team": "Oklahoma City Thunder", "ppg": 19.1, "rpg": 4.0, "apg": 4.5, "spg": 1.1, "bpg": 0.5, "fantasy_points": 34.7},
        {"name": "Josh Giddey", "position": "SG", "nba_team": "Oklahoma City Thunder", "ppg": 12.3, "rpg": 6.4, "apg": 4.8, "spg": 0.9, "bpg": 0.6, "fantasy_points": 29.5},
        
        # Orlando Magic
        {"name": "Paolo Banchero", "position": "PF", "nba_team": "Orlando Magic", "ppg": 22.6, "rpg": 6.9, "apg": 5.4, "spg": 0.9, "bpg": 0.7, "fantasy_points": 41.0},
        {"name": "Franz Wagner", "position": "SF", "nba_team": "Orlando Magic", "ppg": 19.7, "rpg": 5.3, "apg": 3.7, "spg": 1.1, "bpg": 0.6, "fantasy_points": 35.9},
        {"name": "Wendell Carter Jr.", "position": "C", "nba_team": "Orlando Magic", "ppg": 11.0, "rpg": 6.9, "apg": 2.1, "spg": 0.6, "bpg": 0.9, "fantasy_points": 26.0},
        {"name": "Cole Anthony", "position": "PG", "nba_team": "Orlando Magic", "ppg": 11.6, "rpg": 3.5, "apg": 3.0, "spg": 0.8, "bpg": 0.3, "fantasy_points": 23.7},
        
        # Philadelphia 76ers
        {"name": "Joel Embiid", "position": "C", "nba_team": "Philadelphia 76ers", "ppg": 34.7, "rpg": 11.0, "apg": 5.6, "spg": 1.2, "bpg": 1.7, "fantasy_points": 60.7},
        {"name": "Tyrese Maxey", "position": "PG", "nba_team": "Philadelphia 76ers", "ppg": 25.9, "rpg": 3.7, "apg": 6.2, "spg": 1.0, "bpg": 0.5, "fantasy_points": 42.8},
        {"name": "Tobias Harris", "position": "PF", "nba_team": "Philadelphia 76ers", "ppg": 17.2, "rpg": 6.5, "apg": 3.1, "spg": 1.0, "bpg": 0.9, "fantasy_points": 33.2},
        {"name": "Kelly Oubre Jr.", "position": "SF", "nba_team": "Philadelphia 76ers", "ppg": 15.4, "rpg": 5.0, "apg": 1.5, "spg": 1.1, "bpg": 0.8, "fantasy_points": 28.3},
        
        # Phoenix Suns
        {"name": "Kevin Durant", "position": "SF", "nba_team": "Phoenix Suns", "ppg": 27.1, "rpg": 6.6, "apg": 5.0, "spg": 0.9, "bpg": 1.2, "fantasy_points": 45.3},
        {"name": "Devin Booker", "position": "SG", "nba_team": "Phoenix Suns", "ppg": 27.1, "rpg": 4.5, "apg": 6.9, "spg": 0.9, "bpg": 0.5, "fantasy_points": 44.4},
        {"name": "Bradley Beal", "position": "SG", "nba_team": "Phoenix Suns", "ppg": 18.2, "rpg": 4.4, "apg": 5.0, "spg": 1.0, "bpg": 0.4, "fantasy_points": 33.5},
        {"name": "Jusuf Nurkic", "position": "C", "nba_team": "Phoenix Suns", "ppg": 10.9, "rpg": 11.0, "apg": 4.0, "spg": 0.9, "bpg": 1.1, "fantasy_points": 33.4},
        
        # Portland Trail Blazers
        {"name": "Anfernee Simons", "position": "SG", "nba_team": "Portland Trail Blazers", "ppg": 22.6, "rpg": 3.6, "apg": 5.5, "spg": 0.8, "bpg": 0.3, "fantasy_points": 37.3},
        {"name": "Jerami Grant", "position": "PF", "nba_team": "Portland Trail Blazers", "ppg": 21.0, "rpg": 3.5, "apg": 2.8, "spg": 0.9, "bpg": 0.8, "fantasy_points": 33.5},
        {"name": "Deandre Ayton", "position": "C", "nba_team": "Portland Trail Blazers", "ppg": 14.0, "rpg": 10.5, "apg": 1.7, "spg": 0.6, "bpg": 0.9, "fantasy_points": 32.2},
        {"name": "Scoot Henderson", "position": "PG", "nba_team": "Portland Trail Blazers", "ppg": 14.0, "rpg": 3.1, "apg": 5.4, "spg": 0.9, "bpg": 0.6, "fantasy_points": 28.5},
        
        # Sacramento Kings
        {"name": "De'Aaron Fox", "position": "PG", "nba_team": "Sacramento Kings", "ppg": 26.6, "rpg": 4.6, "apg": 5.6, "spg": 2.0, "bpg": 0.4, "fantasy_points": 44.7},
        {"name": "Domantas Sabonis", "position": "C", "nba_team": "Sacramento Kings", "ppg": 19.4, "rpg": 13.7, "apg": 8.2, "spg": 0.9, "bpg": 0.6, "fantasy_points": 48.3},
        {"name": "Keegan Murray", "position": "PF", "nba_team": "Sacramento Kings", "ppg": 15.2, "rpg": 5.5, "apg": 1.4, "spg": 0.9, "bpg": 0.3, "fantasy_points": 27.8},
        {"name": "Kevin Huerter", "position": "SG", "nba_team": "Sacramento Kings", "ppg": 10.2, "rpg": 3.5, "apg": 2.6, "spg": 0.6, "bpg": 0.2, "fantasy_points": 20.6},
        
        # San Antonio Spurs
        {"name": "Victor Wembanyama", "position": "C", "nba_team": "San Antonio Spurs", "ppg": 21.4, "rpg": 10.6, "apg": 3.9, "spg": 1.2, "bpg": 3.6, "fantasy_points": 47.2},
        {"name": "Devin Vassell", "position": "SG", "nba_team": "San Antonio Spurs", "ppg": 19.5, "rpg": 4.1, "apg": 3.8, "spg": 1.1, "bpg": 0.7, "fantasy_points": 34.7},
        {"name": "Keldon Johnson", "position": "SF", "nba_team": "San Antonio Spurs", "ppg": 15.7, "rpg": 5.5, "apg": 2.8, "spg": 0.9, "bpg": 0.4, "fantasy_points": 29.8},
        {"name": "Tre Jones", "position": "PG", "nba_team": "San Antonio Spurs", "ppg": 10.0, "rpg": 3.3, "apg": 6.2, "spg": 1.0, "bpg": 0.3, "fantasy_points": 25.3},
        
        # Toronto Raptors
        {"name": "Scottie Barnes", "position": "PF", "nba_team": "Toronto Raptors", "ppg": 19.9, "rpg": 8.2, "apg": 6.1, "spg": 1.5, "bpg": 1.5, "fantasy_points": 42.7},
        {"name": "RJ Barrett", "position": "SG", "nba_team": "Toronto Raptors", "ppg": 18.6, "rpg": 5.7, "apg": 3.3, "spg": 0.9, "bpg": 0.3, "fantasy_points": 33.3},
        {"name": "Immanuel Quickley", "position": "PG", "nba_team": "Toronto Raptors", "ppg": 18.6, "rpg": 4.5, "apg": 6.8, "spg": 0.9, "bpg": 0.5, "fantasy_points": 35.8},
        {"name": "Jakob Poeltl", "position": "C", "nba_team": "Toronto Raptors", "ppg": 11.1, "rpg": 8.6, "apg": 2.9, "spg": 0.7, "bpg": 1.5, "fantasy_points": 30.3},
        
        # Utah Jazz
        {"name": "Lauri Markkanen", "position": "PF", "nba_team": "Utah Jazz", "ppg": 23.2, "rpg": 8.2, "apg": 2.0, "spg": 0.9, "bpg": 0.5, "fantasy_points": 39.3},
        {"name": "Jordan Clarkson", "position": "SG", "nba_team": "Utah Jazz", "ppg": 17.1, "rpg": 3.4, "apg": 5.0, "spg": 1.0, "bpg": 0.3, "fantasy_points": 31.3},
        {"name": "Collin Sexton", "position": "PG", "nba_team": "Utah Jazz", "ppg": 18.7, "rpg": 2.9, "apg": 4.9, "spg": 0.8, "bpg": 0.2, "fantasy_points": 31.0},
        {"name": "Walker Kessler", "position": "C", "nba_team": "Utah Jazz", "ppg": 8.1, "rpg": 7.5, "apg": 1.0, "spg": 0.7, "bpg": 2.4, "fantasy_points": 25.2},
        
        # Washington Wizards
        {"name": "Kyle Kuzma", "position": "PF", "nba_team": "Washington Wizards", "ppg": 22.2, "rpg": 6.6, "apg": 4.2, "spg": 0.5, "bpg": 0.5, "fantasy_points": 38.5},
        {"name": "Jordan Poole", "position": "SG", "nba_team": "Washington Wizards", "ppg": 17.4, "rpg": 2.7, "apg": 4.4, "spg": 1.1, "bpg": 0.3, "fantasy_points": 30.4},
        {"name": "Tyus Jones", "position": "PG", "nba_team": "Washington Wizards", "ppg": 12.0, "rpg": 2.7, "apg": 7.3, "spg": 1.1, "bpg": 0.2, "fantasy_points": 27.8},
        {"name": "Deni Avdija", "position": "SF", "nba_team": "Washington Wizards", "ppg": 14.7, "rpg": 7.2, "apg": 3.8, "spg": 0.9, "bpg": 0.6, "fantasy_points": 31.7},
    ]
    
    added = 0
    skipped = 0
    
    for player_data in players:
        existing = db.query(Player).filter(Player.name == player_data["name"]).first()
        if not existing:
            player = Player(**player_data)
            db.add(player)
            added += 1
        else:
            skipped += 1
    
    db.commit()
    db.close()
    
    print(f"Player seeding complete! Added: {added}, Skipped: {skipped}")

if __name__ == "__main__":
    add_all_nba_players()