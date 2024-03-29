from dotenv import load_dotenv
import os


class Bamboo:
    BASE_URL = "https://api.jira.org/2.0"
    HEADERS = { "Content-Type": "application/json" }

    def __init__(self):
        load_dotenv()
        self.HEADERS["Authorization"] = f"Bearer {os.getenv('TOKEN_BAMBOO')}"
