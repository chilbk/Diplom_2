import random as rnd

class AuthHelper:
    def generate_login(self) -> str:
        return f'vda_diplom_{rnd.randint(100, 999)}@example.com'

    def generate_password(self) -> str:
        return 'diplom_' + str(rnd.randint(100000, 999999))

    def generate_name(self) -> str:
        names = ['Spasibo', 'Zaa', 'Review', 'Diploma', 'Tovarish', 'Reviewer']
        return f"{rnd.choice(names)}_{rnd.randint(1, 999)}"