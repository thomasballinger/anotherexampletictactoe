

class Board(object):
    signs = {1:'x',
              -1:'0',
              0:'.',}
    def __init__(self):
        self.rows = [[0] * 3 for _ in range(3)] 
    @property
    def columns(self):
        return zip(*self.rows)
    @property
    def spots(self):
        return sum(self.rows, [])
    def __str__(self):
        return '\n'.join(' '.join(Board.symbols[s] for s in row) for row in self.rows)
    def turn(self):
        return sum(len(spot for spot in row if spot != 0) for row in self.rows)

if __name__ == '__main__':
    b = Board()
    b.turn('x')
    b.turn('x')
    print b

# this is a fancy class
