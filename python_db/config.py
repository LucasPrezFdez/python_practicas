from dotenv import load_dotenv
import os

DATABASE_URL = load_dotenv()

os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("No fui capaz de cargar el .env")
