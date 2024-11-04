import os

class Config:
    DB_USER = os.getenv("SALES_PAYMENT_DB_USER", "root")
    DB_PASSWORD = os.getenv("SALES_PAYMENT_DB_PASSWORD", "root_password")
    DB_NAME = os.getenv("SALES_PAYMENT_DB_NAME", "sales_payment")
    DB_HOST = os.getenv("DB_HOST", "sales_payment_db")
    DB_PORT = os.getenv("DB_PORT", 3306)
