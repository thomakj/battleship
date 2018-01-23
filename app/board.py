
class Board(object):

    """docstring for Board."""

    def __init__(self):
        super(Board, self).__init__()
        self.grid = [[0 for x in range(10)] for y in range(10)]
