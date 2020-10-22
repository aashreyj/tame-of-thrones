import unittest
from geektrust import *

DECRYPTED_MESSAGE = 'AFRICAISWILD'
ALLEGIANCE_MESSAGE = 'AFRICAHASOWLSGORILLASBUTNOTPANDAS'


# test case class to run unit tests
class MyTestCase(unittest.TestCase):

    # test to check if kingdom-emblem mapping is functioning properly
    def test_kingdom_emblem(self):
        kingdom_emblem_dict = {'AIR': 'OWL', 'SPACE': 'GORILLA', 'FIRE': 'DRAGON', 'WATER': 'OCTOPUS', 'LAND': 'PANDA', 'ICE': 'MAMMOTH'}
        for kingdom in kingdom_emblem_dict:
            self.assertEqual(get_kingdom_emblem(kingdom), kingdom_emblem_dict[kingdom])

    # test to check decryption method of AIR Kingdom
    def test_air_decryption(self):
        kingdom = Kingdom('AIR', get_kingdom_emblem('AIR'))
        test_message = Message('DIULFDLVZLOG')
        decrypted_message = kingdom.decrypt(test_message)
        self.assertEqual(decrypted_message, DECRYPTED_MESSAGE)

    # test to check decryption method of SPACE Kingdom
    def test_space_decryption(self):
        kingdom = Kingdom('SPACE', get_kingdom_emblem('SPACE'))
        test_message = Message('HMYPJHPZDPSK')
        decrypted_message = kingdom.decrypt(test_message)
        self.assertEqual(decrypted_message, DECRYPTED_MESSAGE)

    # test to check decryption method of FIRE Kingdom
    def test_fire_decryption(self):
        kingdom = Kingdom('FIRE', get_kingdom_emblem('FIRE'))
        test_message = Message('GLXOIGOYCORJ')
        decrypted_message = kingdom.decrypt(test_message)
        self.assertEqual(decrypted_message, DECRYPTED_MESSAGE)

    # test to check decryption method of WATER Kingdom
    def test_water_decryption(self):
        kingdom = Kingdom('WATER', get_kingdom_emblem('WATER'))
        test_message = Message('HMYPJHPZDPSK')
        decrypted_message = kingdom.decrypt(test_message)
        self.assertEqual(decrypted_message, DECRYPTED_MESSAGE)

    # test to check decryption method of ICE Kingdom
    def test_ice_decryption(self):
        kingdom = Kingdom('ICE', get_kingdom_emblem('ICE'))
        test_message = Message('HMYPJHPZDPSK')
        decrypted_message = kingdom.decrypt(test_message)
        self.assertEqual(decrypted_message, 'AFRICAISWILD')

    # test to check decryption method of LAND Kingdom
    def test_land_decryption(self):
        kingdom = Kingdom('LAND', get_kingdom_emblem('LAND'))
        test_message = Message('FKWNHFNXBNQI')
        decrypted_message = kingdom.decrypt(test_message)
        self.assertEqual(decrypted_message, DECRYPTED_MESSAGE)

    # test to check give_allegiance method of AIR Kingdom
    def test_air_allegiance(self):
        kingdom = Kingdom('AIR', get_kingdom_emblem('AIR'))
        decrypted_message = Message(ALLEGIANCE_MESSAGE)
        is_ally = kingdom.give_allegiance(decrypted_message)
        self.assertEqual(is_ally, True)

    # test to check give_allegiance method of SPACE Kingdom
    def test_space_allegiance(self):
        kingdom = Kingdom('SPACE', get_kingdom_emblem('SPACE'))
        decrypted_message = Message(ALLEGIANCE_MESSAGE)
        is_ally = kingdom.give_allegiance(decrypted_message)
        self.assertEqual(is_ally, True)

    # test to check give_allegiance method of FIRE Kingdom
    def test_fire_allegiance(self):
        kingdom = Kingdom('FIRE', get_kingdom_emblem('FIRE'))
        decrypted_message = Message(ALLEGIANCE_MESSAGE)
        is_ally = kingdom.give_allegiance(decrypted_message)
        self.assertEqual(is_ally, True)

    # test to check give_allegiance method of WATER Kingdom
    def test_water_allegiance(self):
        kingdom = Kingdom('WATER', get_kingdom_emblem('WATER'))
        decrypted_message = Message(ALLEGIANCE_MESSAGE)
        is_ally = kingdom.give_allegiance(decrypted_message)
        self.assertEqual(is_ally, True)

    # test to check give_allegiance method of LAND Kingdom
    def test_land_allegiance(self):
        kingdom = Kingdom('LAND', get_kingdom_emblem('LAND'))
        decrypted_message = Message(ALLEGIANCE_MESSAGE)
        is_ally = kingdom.give_allegiance(decrypted_message)
        self.assertEqual(is_ally, True)

    # test to check give_allegiance method of ICE Kingdom
    def test_ice_allegiance(self):
        kingdom = Kingdom('ICE', get_kingdom_emblem('ICE'))
        decrypted_message = Message(ALLEGIANCE_MESSAGE)
        is_ally = kingdom.give_allegiance(decrypted_message)
        self.assertEqual(is_ally, False)



if __name__ == '__main__':
    unittest.main()
