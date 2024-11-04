import os

class Config:
    DB_USER = os.getenv("RETURN_REFUND_DB_USER", "root")
    DB_PASSWORD = os.getenv("RETURN_REFUND_DB_PASSWORD", "root_password")
    DB_NAME = os.getenv("RETURN_REFUND_DB_NAME", "return_refund")
    DB_HOST = os.getenv("DB_HOST", "return_refund_db")
    DB_PORT = os.getenv("DB_PORT", 3306)
