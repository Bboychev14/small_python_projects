from animal import Animal


class Lion(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender, money_for_care=50)
