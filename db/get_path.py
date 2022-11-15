from dotenv import load_dotenv
import os


load_dotenv(".env")

def get_db_url():
    return os.getenv("DB_URL")