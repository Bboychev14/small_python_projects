from animal import Animal
from worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_salaries = 0
        for worker in self.workers:
            all_salaries += worker.salary
        if all_salaries <= self.__budget:
            self.__budget -= all_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money = 0
        for animal in self.animals:
            needed_money += animal.money_for_care
        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__build_animal_string("Lion")
        result += self.__build_animal_string("Tiger")
        result += self.__build_animal_string("Cheetah")
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__build_job_string("Keeper")
        result += self.__build_job_string("Caretaker")
        result += self.__build_job_string("Vet")
        return result

    def __build_job_string(self, temp_job):
        people_on_this_position = []
        for man in self.workers:
            if man.__class__.__name__ == temp_job:
                people_on_this_position.append(man)
        temp_result = f"----- {len(people_on_this_position)} {temp_job}s\n"
        for guy in people_on_this_position:
            temp_result += guy.__repr__() + '\n'
        return temp_result

    def __build_animal_string(self, temp_animal):
        animals_of_this_kind = []
        for animal in self.animals:
            if animal.__class__.__name__ == temp_animal:
                animals_of_this_kind.append(animal)
        temp_result = f"----- {len(animals_of_this_kind)} {temp_animal}s\n"
        for animal in animals_of_this_kind:
            temp_result += animal.__repr__() + '\n'
        return temp_result