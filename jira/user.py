import requests
from Jira import Jira


class User(Jira):
  user_name: str

  def get_user(self) -> dict:
    """
    Get a user by name
    :param user_name: str
    :return: object
    """
    url = f"{self.BASE_URL}/rest/api/2/user?username={self.user_name}"
    try:
      response = requests.get(url, headers=self.HEADERS)
      return response.json()
    except requests.RequestException as e:
      raise f'Error getting user {self.user_name}: {e}'

    def create_user(self) -> dict:
      pass