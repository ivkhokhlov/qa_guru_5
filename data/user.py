import os
from dataclasses import dataclass

from config import ROOT_DIR


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    day: str
    month: str
    year: str
    subjects: list
    hobbies: list
    image: str
    address: str
    state: str
    city: str


ivan = User(
    first_name='Ivan',
    last_name='Khokhov',
    email='ivan@example.com',
    gender='Male',
    mobile='0123456789',
    day='07',
    month='08',
    year='2023',
    subjects=['Math', 'Commerce'],
    hobbies=['Reading', 'Music'],
    image=os.path.join(ROOT_DIR, 'tests/resources/img.jpeg'),
    address='г. Магадан, ул. Ленина 21-72',
    state='NCR',
    city='Delhi'
)
