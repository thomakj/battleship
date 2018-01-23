import unittest
from ..app.player import Player

class TestPlayer(unittest.TestCase):

    """docstring for TestPlayer."""

    def test_player_name_on_object_creation(self):
        self.player = Player("Tester Testersen")
        player_name = self.player.get_name()
        self.assertEqual("Tester Testersen", player_name)

if __name__ == '__main__':
    unittest.main()
