

class Board(object):
    def __init__(self):
        self.rows = [[0] * 3 for _ in range(3)]
    @property
    def columns(self):
        return zip(*self.rows)



