class Character(object):
    def __init__(self, name):
        self.first_name = name

    def attack(self):
        pass


class Alien(Character):
    def __init__(self, name, planet):
        super().__init__(name)
        self.planet = planet


class Wizard(Character):
    pass


class Coder(Character):
    pass


class Healer(Character):
    pass