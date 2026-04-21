import random

def generate_email():
    number = random.randint(100, 999)
    return f"test_user_12_{number}@yandex.ru"

def generate_password():
    return f"pass{random.randint(1000,9999)}"

