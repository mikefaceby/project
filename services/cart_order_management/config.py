import os

class Config:
    DB_USER = os.getenv("CART_ORDER_DB_USER", "root")
    DB_PASSWORD = os.getenv("CART_ORDER_DB_PASSWORD", "root_password")
    DB_NAME = os.getenv("CART_ORDER_DB_NAME", "cart_order_management")
    DB_HOST = os.getenv("DB_HOST", "cart_order_db")
    DB_PORT = os.getenv("DB_PORT", 3306)
