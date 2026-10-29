
import os

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = os.getenv('DB_PASSWORD', '')
MYSQL_DB = 'internship_system'
UPLOAD_FOLDER = 'static/uploads'
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-only-change-me')
