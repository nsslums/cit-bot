from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.environ.get("TOKEN")
TODOFILE = os.environ.get("TODOFILE")