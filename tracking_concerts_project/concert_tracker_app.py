from band import Band
from band_members.drummer import Drummer
from band_members.guitarist import Guitarist
from band_members.singer import Singer
from concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ["Guitarist", "Drummer", "Singer"]:
            raise ValueError("Invalid musician type!")
        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")
        else:
            if musician_type == "Guitarist":
                self.musicians.append(Guitarist(name, age))
            elif musician_type == "Drummer":
                self.musicians.append(Drummer(name, age))
            elif musician_type == "Singer":
                self.musicians.append(Singer(name, age))
            return f"{name} is now a {musician_type}."

    def create_band(self, name:str):
        for band in self.bands:
            if name == band.name:
                raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician_names = []
        band_names = []
        temp_musician = None
        temp_band = None
        for musician in self.musicians:
            musician_names.append(musician.name)
            if musician.name == musician_name:
                temp_musician = musician

        for band in self.bands:
            band_names.append(band.name)
            if band.name == band_name:
                temp_band = band

        if musician_name not in musician_names:
            raise Exception(f"{musician_name} isn't a musician!")
        elif band_name not in band_names:
            raise Exception(f"{band_name} isn't a band!")
        else:
            temp_band.members.append(temp_musician)
            return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band_names = []
        temp_musician = None
        temp_band = None
        for musician in self.musicians:
            if musician.name == musician_name:
                temp_musician = musician

        for band in self.bands:
            band_names.append(band.name)
            if band.name == band_name:
                temp_band = band

        if band_name not in band_names:
            raise Exception(f"{band_name} isn't a band!")
        elif temp_musician not in temp_band.members:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        else:
            temp_band.members.remove(temp_musician)
            return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        temp_band = None
        member_types = []
        for band in self.bands:
            if band.name == band_name:
                temp_band = band
        for member in temp_band.members:
            member_types.append(member.__class__.__name__)


musician_types = ["Singer", "Drummer", "Guitarist"]
names = ["George", "Alex", "Lilly"]

app = ConcertTrackerApp()

for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))

print(app.create_band("RockName"))
for i in range(3):
    print(app.add_musician_to_band(names[i], "RockName"))

print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))

print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))
