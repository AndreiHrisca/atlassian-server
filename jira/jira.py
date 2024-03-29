import os
from dotenv import load_dotenv


class Jira():
    BASE_URL = "http://localhost:8080"
    HEADERS = { "Content-Type": "application/json" }

    def __init__(self):
        load_dotenv()
        self.HEADERS["Authorization"] = f"Bearer {os.getenv('TOKEN_JIRA')}"
