from core.validator import Validator


class Concert:
    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        Validator.raise_if_genre_is_invalid(value, f"Our group doesn't play {value}!")
        self.__genre = value

    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value):
        Validator.raise_if_num_is_less_than_one(value, "At least one person should attend the concert!")
        self.__audience = value

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        Validator.raise_if_num_is_less_than_one(value, "Ticket price must be at least 1.00$!")
        self.__ticket_price = value

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        Validator.raise_if_num_is_less_than_zero(value, "Expenses cannot be a negative number!")
        self.__expenses = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        Validator.raise_if_place_is_invalid(value, "Place must contain at least 2 chars. It cannot be empty!")
        self.__place = value

    def __str__(self):
        return f"{self.genre} concert at {self.place}."
