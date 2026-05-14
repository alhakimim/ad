# مسؤول عن إدارة الاتصال بقاعدة البيانات
import sqlite3
from settings import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)
