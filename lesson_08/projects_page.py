import requests
from config import Config


class ProjectsPage:
    def __init__(self):
        self.base_url = f"{Config.API_URL}/projects"
        self.headers = Config.HEADERS

    def create_project(self, project_data):
        response = requests.post(
            self.base_url,
            json=project_data,
            headers=self.headers
        )
        return response

    def get_project(self, project_id):
        response = requests.get(
            f"{self.base_url}/{project_id}",
            headers=self.headers
        )
        return response

    def update_project(self, project_id, update_data):
        response = requests.put(
            f"{self.base_url}/{project_id}",
            json=update_data,
            headers=self.headers
        )
        return response
