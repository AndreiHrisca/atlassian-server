import requests
from Jira import Jira


class Group(Jira):
  group_name: str

  def __init__(self, group_name: str):
    self.group_name = group_name

  def create_group(self):
    """
    Create a new group
    :return: object
    """
    url = f'{self.BASE_URL}/rest/api/2/group'
    data = {
      "name": self.group_name,
      "description": self.group_description
    }
    try:
      response = self.post(url, json=data)
      return response.json()
    except requests.RequestException as e:
      raise f'Error creating group {self.group_name}: {e}'

  def add_user_to_group(self, user_name: str):
    """
    Add user to group
    :param user_name: str
    :return: object
    """
    url = f'{self.BASE_URL}/rest/api/2/group/user'
    data = {
      "name": self.group_name,
      "user": user_name
    }
    try:
      response = self.post(url, json=data)
      return response.json()
    except requests.RequestException as e:
      raise f'Error adding user {user_name} to group {self.group_name}: {e}'