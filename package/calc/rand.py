import random
def get_random_number(start=0, end=100):
    return random.randint(start, end)

if __name__ == '__main__':
    print(get_random_number())