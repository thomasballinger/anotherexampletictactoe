

class Board(object):
    def __init__(self):
        self.rows = [[0] * 3 for _ in range(3)]
    def turn(self):
        return sum(len(spot for spot in row if spot != 0) for row in self.rows)



