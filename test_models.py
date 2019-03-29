from models import *


def test_character_name():
    bob_character = Character('bob')
    assert bob_character.first_name == 'bob'

def test_inherits_name():
    alien_bob = Alien('bob', 'Betelgeuse')
    assert alien_bob.first_name == 'bob'
    assert alien_bob.planet == 'Betelgeuse'
