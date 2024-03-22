import os
from dotenv import load_dotenv

class Bitbucket:
    BASE_URL = "https://AndreiHri@bitbucket.org"
    HEADERS = { "Content-Type": "application/json" }

    def __init__(self):
        load_dotenv()
        self.HEADERS["Authorization"] = f"Bearer {os.getenv('TOKEN_BITBUKET')}"
