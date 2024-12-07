Railway Management System
A Python-based railway management system built using Flask and MySQL. 
It allows users to register, log in, book seats, check availability, and manage train schedules.
Admin endpoints are protected using an API key, and user endpoints require JWT-based authentication.

--->Features:
User registration and login with JWT-based authentication.
Secure endpoints for managing train schedules (Admin only).
Real-time seat availability checks and booking.
Protected API endpoints using:
Admin API Key for admin operations.
JWT Tokens for user authentication.
Handles concurrent seat bookings efficiently.

--->Tech Stack:
Backend: Python (Flask)
Database: MySQL
Authentication: JWT (JSON Web Tokens)

--->Setup Instructions
1. Prerequisites
Python 3.8 or above installed.
MySQL installed and running.

2. Install Dependencies
Use pip to install the required Python packages:
pip install -r requirements.txt

3. Configure Environment Variables
Create a .env file in the root directory and add the following:

4. Setup the Database
Log in to MySQL:
mysql -u root -p
Create the database:
sql:
CREATE DATABASE railway_management;
Run the migrations:
bash code:
python database/migrations.py

5. Run the Application
Start the Flask server:

----->bash code:
python app.py
The app will be available at http://127.0.0.1:5000.
#### API key:railway_management

Assumptions
Concurrency: The booking system uses database locks to prevent race conditions.
Authentication: Admin API keys and JWT tokens are assumed to be shared securely.
Deployment: This project is meant for development purposes and is not production-ready

