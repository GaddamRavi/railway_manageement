from flask import Flask
from flask_jwt_extended import JWTManager
from utils.db import initialize_db
from routes.user_routes import user_routes
from routes.admin_routes import admin_routes
from dotenv import load_dotenv
import os

load_dotenv()
ADMIN_API_KEY = os.getenv('ADMIN_API_KEY')

app = Flask(__name__)

 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'railway_system'

@app.route('/')
def home():
    return "Welcome to the Railway Management System!"
 
jwt = JWTManager(app)
initialize_db(app)
for rule in app.url_map.iter_rules():
    print(f"Route: {rule.rule}, Methods: {rule.methods}")
 
app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(admin_routes, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)
