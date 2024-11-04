import os

class Config:
    DB_USER = os.getenv("USER_DB_USER", "root")
    DB_PASSWORD = os.getenv("USER_DB_PASSWORD", "root_password")
    DB_NAME = os.getenv("USER_DB_NAME", "user_management")
    DB_HOST = os.getenv("DB_HOST", "user_db")
    DB_PORT = os.getenv("DB_PORT", 3306)
