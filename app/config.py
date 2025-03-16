import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # get the mongoUri from the environment
    MONGO_URI = os.getenv("MONGO_URI")
