import requests
from Jira import Jira


class Scheme(Jira):

  def get_notification_scheme(self):
    """
    Get all notification schemes
    :return: object
    """
    url = f'{self.BASE_URL}/rest/api/2/notificationscheme'
    try:
      response = requests.get(url, headers=self.HEADERS)
      return response.json()
    except requests.RequestException as e:
      return f'Error getting notification scheme: {e}'

  def get_permission_scheme(self):
    """
    Get all permission schemes
    :return: object
    """
    url = f'{self.BASE_URL}/rest/api/2/permissionscheme'
    try:
      response = requests.get(url, headers=self.HEADERS)
      return response.json()
    except requests.RequestException as e:
      return f'Error getting permission scheme: {e}'
