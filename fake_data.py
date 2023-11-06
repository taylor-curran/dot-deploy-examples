import random
import string
import pandas as pd

def generate_random_string(length=6):
    # Generates a random string of fixed length 
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_list(length=3):
    # Generates a random list of integers of fixed length
    return [random.randint(0, 100) for _ in range(length)]

def generate_random_tuple(length=2):
    # Generates a random tuple of floats of fixed length
    return tuple(random.uniform(0, 100) for _ in range(length))

def create_random_dict():
    return {
        'integer': random.randint(1, 100),
        'float': random.uniform(1, 100),
        'string': generate_random_string(),
        'boolean': random.choice([True, False]),
        'list': generate_random_list(),
        'tuple': generate_random_tuple()
    }

def create_data_set(num_dicts=70):
    return [create_random_dict() for _ in range(num_dicts)]

if __name__ == "__main__":

    # Generate the data
    data_set = create_data_set(500000)

    pd.DataFrame(data_set).to_csv('med_fake_data.csv', index=False)

    # Check the first dictionary to see if it looks okay
    print(data_set[0])
