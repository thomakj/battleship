
class Player(object):

    """docstring for Player."""

    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name

    def get_name(self):
        return self.name
