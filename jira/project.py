import json
import requests
from Jira import Jira


class Project(Jira):
  project_key: str
  project_name: str
  project_description: str
  project_lead: str
  project_category_id: int

  def __init__(self):
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
