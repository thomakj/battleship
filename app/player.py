from .board import Board

class Player(object):

    """docstring for Player."""

    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.tracking_board = Board()
        self.primary_board = Board()

    def get_name(self):
        return self.name

    def get_tracking_board(self):
        return self.tracking_board

    def get_primary_board(self):
        return self.primary_board
