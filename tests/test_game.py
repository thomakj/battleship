import unittest
from ..app.game import Game
from ..app.board import Board

class TestGame(unittest.TestCase):

    """docstring for TestGame."""

    @classmethod
    def setUpClass(Game):
        self.game = Game()

    def test_that_there_are_four_grids_in_game(self):
        self.assertIs(self.game.player1.get_primary_board().__class__, Board)
        self.assertIs(self.game.player1.get_tracking_board().__class__, Board)
        self.assertIs(self.game.player2.get_primary_board().__class__, Board)
        self.assertIs(self.game.player2.get_tracking_board().__class__, Board)
