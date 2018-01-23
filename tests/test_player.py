import unittest
from ..app.player import Player
from ..app.board import Board

class TestPlayer(unittest.TestCase):

    """docstring for TestPlayer."""

    def test_player_name_on_object_creation(self):
        self.player = Player("Tester Testersen")
        player_name = self.player.get_name()
        self.assertEqual("Tester Testersen", player_name)

    def test_two_players_name(self):
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")
        self.assertEqual("Player1", self.player1.get_name())
        self.assertEqual("Player2", self.player2.get_name())

    def test_that_player_have_two_boards(self):
        self.player = Player("Player")
        self.assertIs(self.player.get_tracking_board().__class__, Board)
        self.assertIs(self.player.get_primary_board().__class__, Board)

if __name__ == '__main__':
    unittest.main()
