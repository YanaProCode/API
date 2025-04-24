import requests


class UserService:
    BASE_URL = "https://jsonplaceholder.typicode.com/users"

    @staticmethod
    def get_user(user_id):
        return requests.get(f"{UserService.BASE_URL}/{user_id}")


    @staticmethod
    def get_all_users():
        return requests.get(f"{UserService.BASE_URL}")


    @staticmethod
    def create_user(user_data):
        headers = {"Content-Type": "application/json"}
        return requests.post(f"{UserService.BASE_URL}", json=user_data, headers=headers)


    @staticmethod
    def update_user(user_id, updated_data):
        headers = {"Content-Type": "application/json"}
        return requests.put(f"{UserService.BASE_URL}/{user_id}", json=updated_data, headers=headers)


    @staticmethod
    def delete_user(user_id):
        #headers = {"Content-Type": "application/json"}
        return requests.delete(f"{UserService.BASE_URL}/{user_id}")

