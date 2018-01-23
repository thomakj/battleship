import unittest
from ..app.board import Board

class TestBoard(unittest.TestCase):

    """docstring for TestBoard."""

    def test_board_size(self):
        self.board = Board()
        num_rows = len(self.board.grid)
        num_cols = len(self.board.grid[0])
        self.assertEqual(10, num_cols)
        self.assertEqual(10, num_rows)


if __name__ == '__main__':
    unittest.main()
