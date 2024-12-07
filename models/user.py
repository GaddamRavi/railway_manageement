from utils.db import db

def create_user(username, password_hash, role='user'):
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)", 
                   (username, password_hash, role))
    db.commit()
