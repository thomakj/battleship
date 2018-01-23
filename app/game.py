from .player import Player
class Game(object):

    """docstring for Game."""

    def __init__(self):
        super(Game, self).__init__()
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")
