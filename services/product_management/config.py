import os

class Config:
    DB_USER = os.getenv("PRODUCT_DB_USER", "root")
    DB_PASSWORD = os.getenv("PRODUCT_DB_PASSWORD", "root_password")
    DB_NAME = os.getenv("PRODUCT_DB_NAME", "product_management")
    DB_HOST = os.getenv("DB_HOST", "product_db")
    DB_PORT = os.getenv("DB_PORT", 3306)
