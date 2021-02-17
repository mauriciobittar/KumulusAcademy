class RepositoryModel:

    def __init__(self, name):
        self.name = name

    def set_repositories(self, repositories):
        self.repositories = repositories

    def get_name(self):
        return self.name

    def get_repositories(self):
        return self.repositories