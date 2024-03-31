import json
import requests
from Jira import Jira


class Project(Jira):
  project_key: str
  project_name: str
  project_description: str
  project_lead: str
  project_category_id: int

  def __init__(self, project_key: str):
    self.project_key = project_key
    super().__init__()

  def create_project(self):
    """
    Create a project
    :return: object
    """
    url = f'{self.BASE_URL}/rest/api/2/project'
    data = {
      "key": self.project_key,
      "name": self.project_name,
      "projectTypeKey": "business",
      "projectTemplateKey": "com.atlassian.jira-core-project-templates:jira-core-simplified-process",
      "description": self.project_description,
      "lead": self.project_lead,
      "assigneeType": "PROJECT_LEAD",
      "avatarId": 10200,
      "issueSecurityScheme": 10001,
      "categoryId": 10120
    }
    try:
      response = requests.post(url, headers=self.HEADERS, json=data)
      return response.json()
    except requests.RequestException as e:
      raise f'Error creating project {self.project_key}: {e}'

  def get_project(self):
    """
    Get a project by its key
    :param project_key: str
    :return: status code
    """
    url = f"{self.BASE_URL}/rest/api/2/project/{self.project_key}"
    try:
      response = requests.get(url, headers=self.HEADERS)
      #print(json.dumps(response.json(), indent=2))
      return response.status_code
    except requests.RequestException as e:
      raise f'Error getting project {self.project_key}: {e}'

  def get_all_project_categories(self):
    """
    Get all project categories
    :return: object
    """
    url = f'{self.BASE_URL}/rest/api/2/projectCategory'
    try:
      response = requests.get(url, headers=self.HEADERS)
      return json.dumps(response.json(), indent=2)
    except requests.RequestException as e:
      raise f'Error getting project categories: {e}'