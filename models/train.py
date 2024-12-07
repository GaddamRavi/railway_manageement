from utils.db import db

def get_trains_by_route(source, destination):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM trains WHERE source=%s AND destination=%s", (source, destination))
    return cursor.fetchall()
