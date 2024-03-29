import unittest
from unittest.mock import patch
from Jira.Project import Project

class TestProject(unittest.TestCase):

    def setUp(self):
        self.project = Project()

    def test_get_project(self):
        project_key = 'PROJ-123'
        expected_url = f"{self.project.BASE_URL}/rest/api/2/project/{project_key}"
        expected_response = {'key': project_key, 'name': 'Test Project'}

        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = expected_response
            result = self.project.get_project(project_key)

            mock_get.assert_called_once_with(expected_url, headers=self.project.HEADERS)
            self.assertEqual(result, expected_response)

    def test_create_project(self):
        expected_url = f"{self.project.BASE_URL}/rest/api/2/project"
        expected_response = {'key': 'PROJ-123', 'name': 'Test Project'}

        with patch('requests.post') as mock_post:
            mock_post.return_value.json.return_value = expected_response
            result = self.project.create_project()

            mock_post.assert_called_once_with(expected_url, headers=self.project.HEADERS, json=self.project.data)
            self.assertEqual(result, expected_response)

    def test_get_all_project_categories(self):
        expected_url = f"{self.project.BASE_URL}/rest/api/2/projectCategory"
        expected_response = [{'id': 1, 'name': 'Category 1'}, {'id': 2, 'name': 'Category 2'}]

        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = expected_response
            result = self.project.get_all_project_categories()

            mock_get.assert_called_once_with(expected_url, headers=self.project.HEADERS)
            self.assertEqual(result, expected_response)

if __name__ == '__main__':
    unittest.main()