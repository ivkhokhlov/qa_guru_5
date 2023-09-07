from dataclasses import dataclass


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
    image='resources/img.jpeg',
    address='г. Магадан, ул. Ленина 21-72',
    state='NCR',
    city='Delhi'
)
