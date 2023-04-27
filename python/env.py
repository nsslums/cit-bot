from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.environ.get("TOKEN")
TOKEN_DEBUG = os.environ.get("TOKEN_DEBUG")
TODOFILE = os.environ.get("TODOFILE")