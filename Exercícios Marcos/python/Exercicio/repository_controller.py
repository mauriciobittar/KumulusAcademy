import requests

class RepositoryController:
    def __init__(self, url):
        self.url = url

    def get_user_repositories(self, user):
        path = self.url
        route = "/users/"
        endpoint = user + "/repos"

        try:
            print("\nSENDING GET REQUEST TO: {}" .format(path + route + endpoint))
            response = requests.get(path + route + endpoint)

            if response.status_code != 200:
                print("ERROR: {} - {}" .format(response.status_code, response.reason))
            else:
                print("STATUS: {} - {}" .format(response.status_code, response.reason))

            return response
        
        except requests.exceptions.ConnectionError as error:
            print("ERROR: Failed to establish a new connection")
            return error