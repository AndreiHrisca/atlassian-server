
from Bitbucket.Bitbucket import Bitbucket


class Project(Bitbucket):

    def __init__(self, name, key):
        super().__init__()
        self.name = name
        self.key = key

    def create_project(self):
        # Code to create a project in Bitbucket
        pass

    def delete_project(self):
        # Code to delete a project from Bitbucket
        pass

    def get_info_project(self):
        # Code to get information about the project from Bitbucket
        pass
