from dataclasses import dataclass


@dataclass
class User:
    full_name: str
    email: str
    gender: str
    mobile: str
    birthday: str
    subjects: list
    hobbies: list
    address: str
    state: str
    city: str


ivan = User(
    full_name='Ivan Khokhlov',
    email='ivan@example.com',
    gender='Male',
    mobile='0123456789',
    birthday='07 September,2023',
    subjects=['Math', 'Commerce'],
    hobbies=['Reading', 'Music'],
    address='г. Магадан, ул. Ленина 21-72',
    state='NCR',
    city='Delhi'
)
