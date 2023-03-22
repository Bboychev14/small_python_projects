from abc import ABC, abstractmethod

from tracking_concerts_project.core.validator import Validator


class Musician(ABC):
    AVAILABLE_SKILLS = []

    @abstractmethod
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_null_or_whitespace(value, "Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_if_age_is_less_than_16(value, "Musicians should be at least 16 years old!")
        self.__age = value

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.AVAILABLE_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")
        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        else:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."