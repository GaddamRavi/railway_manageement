from utils.db import db

def book_seat(user_id, train_id):
    cursor = db.cursor()
    cursor.execute("SELECT available_seats FROM trains WHERE id=%s FOR UPDATE", (train_id,))
    train = cursor.fetchone()
    if train['available_seats'] > 0:
        cursor.execute("UPDATE trains SET available_seats=available_seats-1 WHERE id=%s", (train_id,))
        cursor.execute("INSERT INTO bookings (user_id, train_id) VALUES (%s, %s)", (user_id, train_id))
        db.commit()
        return True
    return False
