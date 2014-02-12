

class Board(object):
    sigils = {1:'x',
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
        return '\n'.join(' '.join(Board.sigils[s] for s in row) for row in self.rows)

if __name__ == '__main__':
    b = Board()
    print b

# this is a fancy class
