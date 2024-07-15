from dotenv import load_dotenv
import requests
import os


class Bamboo:
    BASE_URL = "https://api.jira.org/2.0"
    HEADERS = { "Content-Type": "application/json" }

    def __init__(self):
        load_dotenv()
        self.HEADERS["Authorization"] = f"Bearer {os.getenv('TOKEN_BAMBOO')}"

    def get_server(self) -> dict:
        """
        Get server info
        :return: object
        """
        url = f"{self.BASE_URL}/server"
        try:
            response = requests.get(url, headers=self.HEADERS)
            return response.json()
        except requests.RequestException as e:
            raise f'Error getting server info: {e}'