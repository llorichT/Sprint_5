import random
import string


def generate_name():
    length = random.randint(5, 10)
    name = ''.join(random.choices(string.ascii_lowercase, k=length))
    return name.capitalize()


def generate_surname():
    length = random.randint(6, 12)
    surname = ''.join(random.choices(string.ascii_lowercase, k=length))
    return surname.capitalize()


def generate_cohort():
    return f"QA-{random.randint(1, 99)}"


def generate_domain():
    domains = ["test.com", "example.com", "mail.com", "qa.com"]
    return random.choice(domains)


def generate_email(name, surname, cohort, domain):
    number = random.randint(100, 999)

    name = name.lower()
    surname = surname.lower()
    cohort = cohort.lower().replace("-", "")

    return f"{name}_{surname}_{cohort}_{number}@{domain}"


def generate_password():
    return f"Pass{random.randint(1000, 9999)}!"


def generate_user_data():
    name = generate_name()
    surname = generate_surname()
    cohort = generate_cohort()
    domain = generate_domain()

    return {
        "name": name,
        "surname": surname,
        "cohort": cohort,
        "email": generate_email(name, surname, cohort, domain),
        "password": generate_password()
    }