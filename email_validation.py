class User:
    def __init__(self, email) -> None:
        self._email = email
    def get_email(self):
        return self._email

class UserRepository:
    def __init__(self) -> None:
        self._users = []
    def save(self, user):
        self._users.append(user)
    def check_email(self, email):
        return any(u.get_email() == email for u in self._users)
    def find_email(self, email):
        for user in self._users:
            if user.get_email() == email:
                return user
        return None

class UserService:
    def __init__(self, repository) -> None:
        self._repository = repository
    def create_user(self, email):
        if self._repository.check_email(email):
            raise ValueError('This email has already been registered.')

        user = User(email)
        self._repository.save(user)

    def get_user(self, email):
        user = self._repository.find_email(email)

        if not user:
            raise ValueError('This email does not exist')

        return user


repo = UserRepository()
service = UserService(repo)
service.create_user('lea@gmail.com')
service.get_user('lea@gmail.com')





