class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, user_id):
        for u in self.users:
            if u.user_id == user_id:
                return u
        return None

    def remove_user(self, user_id):
        self.users = [u for u in self.users if u.user_id != user_id]
