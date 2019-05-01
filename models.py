from typing import List


class Character(object):
    def __init__(self, name='bob'):
        self.first_name = name

    def attack(self, target: 'Character'):
        pass

    def special(self, target: 'Character' = None):
        pass


class Alien(Character):
    def __init__(self, name='Xzlty', planet='Earth'):
        super().__init__(name)
        self.planet = planet


class Wizard(Character):
    pass


class Coder(Character):
    pass


class Healer(Character):
    pass


class Party(object):
    def __init__(self, members: List[Character]):
        self.party_members = members
