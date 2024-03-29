import json
import requests
from Jira import Jira
from Project import Project
from Group import Group

users_admins = []
users_engineers = []
users_technicals = []
new_groups_for_project = []

def get_project(project_key):
  """
  Get a project by its key
  :param project_key: str
  :return: status code
  """
  url = f"{jira.BASE_URL}/rest/api/2/project/{project_key}"
  try:
    response = requests.get(url, headers=jira.HEADERS)
    #print(json.dumps(response.json(), indent=2))
    return response.status_code
  except requests.RequestException as e:
    raise f'Error getting project {project_key}: {e}'

def get_all_project_categories():
  """
  Get all project categories
  :return: object
  """
  url = f'{jira.BASE_URL}/rest/api/2/projectCategory'
  try:
    response = requests.get(url, headers=jira.HEADERS)
    return json.dumps(response.json(), indent=2)
  except requests.RequestException as e:
    raise f'Error getting project categories: {e}'

def get_group(group_name):
  """
  Get a group by name
  :param group_name: str
  :return: object
  """
  url = f"{jira.BASE_URL}/rest/api/2/group?groupname={group_name}"
  try:
    response = requests.get(url, headers=jira.HEADERS)
    return response.json()
  except requests.RequestException as e:
    raise f'Error getting group {group_name}: {e}'

def get_user(user_name):
  """
  Get a user by name
  :param user_name: str
  :return: object
  """
  url = f"{jira.BASE_URL}/rest/api/2/user?username={user_name}"
  try:
    response = requests.get(url, headers=jira.HEADERS)
    return response.json()
  except requests.RequestException as e:
    raise f'Error getting user {user_name}: {e}'

# CREATE A NEW PROJECT LOGIC.

jira = Jira()
new_project = Project()
print(get_user('andrei'))


# CHECK IF THE PROJECT EXISTS OR NOT.
# CHECK IF THE GROUP EXISTS OR NOT.
# CHECK IF THE USER EXISTS OR NOT.
# CHECK IF THE CATEGORY EXISTS OR NOT.
for category in get_all_project_categories():
  print(category)