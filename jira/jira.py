import os
from dotenv import load_dotenv


class Jira():
    BASE_URL = "https://api.jira.org/2.0"
    HEADERS = { "Content-Type": "application/json" }

    def __init__(self):
        load_dotenv()
        self.HEADERS["Authorization"] = f"Bearer {os.getenv('TOKEN_JIRA')}"
