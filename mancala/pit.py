class Pit:
    """Represents a single pit on the Mancala board."""

    is_store = False

    def __init__(self, stones=4):
        self.stones = stones

    def add(self, count):
        self.stones += count

    def sow(self):
        count = self.stones
        self.stones = 0
        return count

    def is_empty(self):
        if self.stones == 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.stones)


class Store(Pit):
    """A player's scoring store. Inherits from Pit."""

    is_store = True

    def __init__(self):
        super().__init__(stones=0)