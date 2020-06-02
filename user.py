from flask_login import UserMixin

from db import get_db


class User(UserMixin):

    def __init__(self, id_, name, email, password):
	self.id = id_
        self.name = name
        self.email = email
        self.password = password

    @staticmethod
    def getByEmail(user_email):
        db = get_db()
        user = db.execute("SELECT * FROM user WHERE email = ?", (user_email,)).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1], email=user[2], password=user[3]
        )
        return user

    @staticmethod
    def get(user_email, user_password):
        db = get_db()
        user = db.execute("SELECT * FROM user WHERE email = ? AND password = ?", (user_email, user_password, )).fetchone()
        if not user:
            return None

        user = User(
            id_=user[0], name=user[1], email=user[2], password=user[3]
        )
        return user

    @staticmethod
    def create(name, email):
        db = get_db()
        db.execute(
            "INSERT INTO user (name, email)"
            " VALUES (?, ?)",
            (name, email),
        )
        db.commit()

    @staticmethod
    def createByForm(name, email, password):
        db = get_db()
        db.execute(
            "INSERT INTO user (name, email, password)"
            " VALUES (?, ?, ?)",
            (name, email, password),
        )
        db.commit()
