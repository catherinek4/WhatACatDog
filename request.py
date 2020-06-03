from flask_login import UserMixin
from db import get_db
import sqlite3

class Request():
    def __init__(self, animal_type, image_path, breed1, breed2):
        self.type = animal_type
        self.image_path = image_path
        self.breed1 = breed1
        self.breed2 = breed2

    @staticmethod
    def get(user_id, animal_type):
        db = get_db()
        requests = []
        for row in db.execute("SELECT * FROM request WHERE user_id = ? AND animal_type = ?", (user_id, animal_type, )):
            requests.append(Request(row[2], row[3], row[4], row[5]))
            if not requests:
                return None
        return requests
    
    @staticmethod
    def create(user_id, animal_type, image_path, breed1, breed2):
        try:
            db = get_db()
            db.execute("INSERT INTO request (user_id, animal_type, image_path, breed1, breed2)"
            " VALUES (?, ?, ?, ?, ?)",
            (user_id, animal_type, image_path, breed1, breed2))
            db.commit()
        except sqlite3.Error as error:
            print("Failed to insert into sqlite table", error)
