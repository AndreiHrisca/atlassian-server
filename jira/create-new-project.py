import os
import json
from Jira import Jira
from Project import Project
from Group import Group

# Get the absolute path of the input data file
input_file_path = os.path.abspath('./GitHub-Repos/atlassian-server/inputData.json')

# READ THE JSON FILE DATA.
try:
  with open(input_file_path, 'r') as file:
    input_data = json.load(file)
    file.close()
except Exception as e:
  raise f'Error reading input data file: {e}'

jira = Jira()
new_project = Project(input_data('Key'))

# CHECK IF THE PROJECT EXISTS OR NOT.
if new_project.get_project() == 404:
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
    if new_group.get_group() == 404:
      new_group.create_group()
    else:
      print(f'ERROR - Group {new_group} already exists.')

# CHECK IF THE USER EXISTS OR NOT.
# CHECK IF THE CATEGORY EXISTS OR NOT.
# CHECK IF THE SCHEMES EXISTS OR NOT.
