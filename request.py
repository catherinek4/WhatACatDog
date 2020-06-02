from flask_login import UserMixin
from db import get_db

class Request():
    def __init__(self, image, breed1, breed2):
        self.image = image
        self.breed1 = breed1
        self.breed2 = breed2

    def convertToBinaryData(filename):
        #Convert digital data to binary format
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData
    
    @staticmethod
    def get(user_id):
        db = get_db()
        requests = []
        for row in db.execute("SELECT * FROM request WHERE user_id = ?", (user_id, )):
            requests.append(Request(image = row[2], breed1 = row[3], breed2 = row[4]))
            if not requests:
                return None
        return requests

    @staticmethod
    def create(user_id, image, breed1, breed2):
        try:
            db = get_db()
            db.execute("INSERT INTO request (user_id, image, breed1, breed2)"
            " VALUES (?, ?, ?, ?)",
            (user_id, image, breed1, breed2),)
            db.commit()
        except sqlite3.Error as error:
            print("Failed to insert into sqlite table", error)
