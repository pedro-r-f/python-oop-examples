class Address:
    def __init__(self, city, state) -> None:
        self._city = city
        self._state = state
    def get_city(self):
        return self._city

class User:
    def __init__(self, address: Address) -> None:
        self._address = address
    def show_city(self):
        print(f"{self._address.get_city()}")

address = Address('Manhattan', 'New York')
person = User(address)
person.show_city()



