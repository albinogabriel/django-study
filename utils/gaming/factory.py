from random import randint
from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)

fake = Faker('pt_BR')

def make_game () :
    return {
        'id': fake.random_number(digits=2, fix_len=True),
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_game())