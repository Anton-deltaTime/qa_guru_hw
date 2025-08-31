from datetime import date
import dataclasses
from enum import Enum


class Gender(Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class Hobbies(Enum):
    sports = "Sports"
    reading = "Reading"
    music = "Music"


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile_number: str
    current_address: str
    permanent_address: str
    gender: Gender
    birthday: date
    subjects: str
    hobbies: Hobbies
    state: str
    city: str


petr = User(
    first_name = 'Petr',
    last_name = 'Gorohov',
    email = 'p.goroh@email.com',
    mobile_number = '8999654321',
    current_address = 'str. Sokolniki 15',
    permanent_address = 'str. Volgodonsk 65',
    gender = Gender.male,
    birthday = date.fromisoformat('1995-05-13'),
    subjects = 'Computer Science',
    hobbies = Hobbies.music,
    state = 'Uttar Pradesh',
    city = 'Merrut'
)
