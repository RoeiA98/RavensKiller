from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os
from utils.utils import convert_to_timedelta

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.venv', '.env'))

# Database connection
def create_connection():
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    if not all([db_host, db_port, db_user, db_password, db_name]):
        raise ValueError("One or more environment variables are missing")

    try:
        client = MongoClient(
            host=db_host,
            port=int(db_port),
            username=db_user,
            password=db_password,
            authSource=db_name
        )
        db = client[db_name]
        return db
    except errors.PyMongoError as e:
        print(f"Error: {e}")
        return None

def save_score(username, score, best_time, highest_level, beat_game):
    """Save player score and best time to the database."""
    # If best_time is a string, convert it to timedelta
    best_time = convert_to_timedelta(best_time)

    # Convert best_time to a string format 'HH:MM:SS' before saving it
    best_time_str = str(best_time)[:-4]

    # Connect to the database
    db = create_connection()
    if db is not None:
        try:
            collection = db['game_scores']
            result = collection.find_one({"username": username})
            
            if result:  # Update the data if user exists
                update_fields = {}
                
                if highest_level > result.get("highest_level", 0):
                    update_fields["highest_level"] = highest_level
                
                if beat_game:
                    stored_best_time = result.get("best_time", "N/A")
                    if stored_best_time == "N/A":
                        update_fields["best_time"] = best_time_str
                        update_fields["beat_game"] = beat_game
                    else:
                        stored_best_time = convert_to_timedelta(stored_best_time)
                        if best_time < stored_best_time:
                            update_fields["best_time"] = best_time_str
                
                if score > result.get("highest_score", 0):
                    update_fields["highest_score"] = score
                
                if update_fields:
                    collection.update_one({"username": username}, {"$set": update_fields})
                        
            else:  # Insert new record if user does not exist
                new_record = {
                    "username": username,
                    "highest_score": score,
                    "highest_level": highest_level,
                    "best_time": "N/A",
                    "beat_game": False
                }
                if beat_game:
                    new_record["best_time"] = best_time_str
                    new_record["beat_game"] = beat_game
                
                collection.insert_one(new_record)
            
            print("Score saved successfully!")
            return {"message": "Score saved successfully!"}, 200
        
        except errors.PyMongoError as e:
            print(f"Error: {e}")
            return {"error": "Database error"}, 500
        
    else:
        print("Database connection failed")
        return {"error": "Database connection failed"}, 500