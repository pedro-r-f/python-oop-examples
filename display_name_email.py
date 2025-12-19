class User:
    def __init__(self, name, email) -> None:
        self._name = name
        self._email = email

    def Display(self):
        print(f"Name: {self._name} | Email: {self._email}")

    def Change_email(self, new_email):
        if '@' not in new_email:
            raise ValueError('Invalid email')
        self._email = new_email

user = User('Lea', 'lea@gmail.com')
user.Display()
user.Change_email('lea12345@gmail.com')
user.Display()

