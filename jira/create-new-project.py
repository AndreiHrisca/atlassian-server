import json
import requests
from Jira import Jira
from Project import Project
from Group import Group
from Scheme import Scheme
import os

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

# Get the absolute path of the input data file
input_file_path = os.path.abspath('./GitHub-Repos/atlassian-server/inputData.json')

# READ THE JSON FILE DATA.
try:
  with open(input_file_path, 'r') as file:
    input_data = json.load(file)
    file.close()
except Exception as e:
  raise f'Error reading input data file: {e}'

# CHECK IF THE PROJECT EXISTS OR NOT.
if get_project(input_data['Key']) == 404:
  try:
    new_project = Project()
    new_project.project_key = input_data['Key']
    new_project.project_name = input_data['Name']
    new_project.project_description = input_data['Description']
  except Exception as e:
    raise f'Error setting project variables: {e}'

# CHECK IF THE GROUP EXISTS OR NOT.
  for group in ['Administrators', 'Engineers', 'Technicals']:
    new_group = Group(f'PROJECT-{input_data["Key"]}-{group}')
    if get_group(new_group) == 404:
      new_group.create_group()
    else:
      print(f'ERROR - Group {new_group} already exists.')

# CHECK IF THE USER EXISTS OR NOT.
# CHECK IF THE CATEGORY EXISTS OR NOT.
# CHECK IF THE SCHEMES EXISTS OR NOT.



