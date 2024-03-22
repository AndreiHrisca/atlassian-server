import requests
from Bitbucket.Bitbucket import Bitbucket


class Repository(Bitbucket):

  def __init__(self):
    super().__init__()

  def get_repo(self, repo_slug):
    """
    Get a repository by its slug
    :param repo_slug: The slug of the repository
    :return: The repository object
    """
    url = f'{self.base_url}/repositories/{self.username}/{repo_slug}'
    try:
      response = requests.get(f"repositories/{self.username}/{repo_slug}")
      return response.json()
    except requests.exceptions.RequestException as e:
      return f'Error getting repository {repo_slug}: {e}'

    def create_repo(self, repo_slug, description):
      """
      Create a repository
      :param repo_slug: The slug of the repository
      :param description: The description of the repository
      :return: The response of the request
      """
      url = f'{self.base_url}/repositories/{self.username}/{repo_slug}'
      data = {
        'name': repo_slug,
        'description': description
      }
      try:
        response = requests.post(url, json=data)
        return response.json()
      except requests.exceptions.RequestException as e:
        return f'Error creating repository {repo_slug}: {e}'

