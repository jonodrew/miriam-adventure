from models import *
import pytest


def test_character_name():
    bob_character = Character('bob')
    assert bob_character.first_name == 'bob'


def test_inherits_name():
    alien_bob = Alien('bob', 'Betelgeuse')
    assert alien_bob.first_name == 'bob'
    assert alien_bob.planet == 'Betelgeuse'


@pytest.mark.parametrize("character, outcome", [
    (Alien(), "The alien aggressively reads poetry at bob!"),
    (Wizard(), "The wizard drops a heavy book on bob's foot!"),
    (Coder(), "The coder tells bob a dad joke. It's super effective!"),
    (Healer(), "The healer makes bob feel bad for not going to the doctor more frequently")
])
def test_attack(character, outcome):
    bob = Character('bob')
    assert character.attack(bob) == outcome


class TestAlien:
    def test_alien_special_removes_alien_from_party(self):
        alan_the_alien = Alien('Alan')
        bob = Character()
        party = Party([bob, alan_the_alien])
        alan_the_alien.special()
        assert party.party_members == [bob]


class TestWizard:
    def test_wizard_special_adds_member_to_party(self):
        anya_the_wizard = Wizard('Anya')
        party = Party([anya_the_wizard])
        alan_the_alien = Alien('Alan')
        anya_the_wizard.special(alan_the_alien)
        assert party.party_members == [anya_the_wizard, alan_the_alien]


class TestCoder:
    """
    The coder's special clones a party member. The new character is included in the party, and their name is the
    reverse of their originator - for example, 'Lucy' would become 'Ycul'. Coders cannot clone Coders!
    """
    def test_coder_special_clones_party_member(self):
        """
        This test needs to be written!
        :return:
        :rtype:
        """
        assert False

    def test_coder_cannot_clone_coder(self):
        anish_the_coder = Coder('Anish')
        antonia_the_coder = Coder('Antonia')
        party = Party([anish_the_coder, antonia_the_coder])
        anish_the_coder.special(antonia_the_coder)
        assert len(party.party_members) == 2
