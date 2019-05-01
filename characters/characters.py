from typing import List
from copy import copy


class Character(object):
    def __init__(self, name='bob', party: 'Party' = None):
        self.first_name = name
        self.party = party

    def attack(self, target: 'Character'):
        pass

    def special(self, target: 'Character' = None):
        pass


class Alien(Character):
    def __init__(self, name='Xzlty', planet='Earth'):
        super().__init__(name)
        self.planet = planet

    def attack(self, target: 'Character'):
        return f'The alien aggressively reads poetry at {target.first_name}!'

    def special(self, target: 'Character' = None):
        self.party.remove(self)
        self.party = None


class Wizard(Character):
    def __init__(self, name=None):
        super().__init__(name)

    def attack(self, target: 'Character'):
        return f"The wizard drops a heavy book on {target.first_name}'s foot!"

    def special(self, target: 'Character' = None):
        self.party.add(target)


class Coder(Character):
    def __init__(self, name=None):
        super().__init__(name)

    def attack(self, target: 'Character'):
        return f"The coder tells {target.first_name} a dad joke. It's super effective!"

    def special(self, target: 'Character' = None):
        if not isinstance(target, Coder):
            cloned_character = self.clone(target)
            cloned_character.first_name = self.reverse_name(target.first_name)
            self.party.add(cloned_character)
        else:
            print(f"Can't clone another coder!")

    def clone(self, target: Character):
        return copy(target)

    def reverse_name(self, name: str):
        return name[::-1].capitalize()


class Party(object):
    def __init__(self, members: List[Character]):
        self.party_members = members
        self.update_party()

    def update_party(self):
        for member in self.party_members:
            member.party = self

    def add(self, target: Character):
        self.party_members.append(target)
        target.party = self

    def remove(self, target: Character):
        self.party_members.remove(target)
        target.party = None
