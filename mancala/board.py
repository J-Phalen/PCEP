"""
board.py
Contains the Board class. Handles layout and terminal display.
"""


class Board:
    """Assembles both players and renders the terminal board."""

    PW = 8  # Pit cell inner width
    SW = 10  # Store cell inner width
    N = 6  # Pits per player

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def display(self):
        """Render the full board to the terminal."""
        pw, sw, n = self.PW, self.SW, self.N

        p2_pits = list(reversed(self.player2.pits))

        border = "+" + "-" * sw + "+" + "+".join(["-" * pw] * n) + "+" + "-" * sw + "+"
        r_p2_labels = "|" + " " * sw + "|" + "|".join(f"{n - i:^{pw}}" for i in range(n)) + "|" + " " * sw + "|"
        r_p2_stones = (
            "|"
            + f"   {self.player2.name[:6]:^6} "
            + "|"
            + "|".join(f"  ({pit.stones:2})  " for pit in p2_pits)
            + "|"
            + f"   {self.player1.name[:6]:^6} "
            + "|"
        )
        r_mid = (
            "|"
            + f"   [{self.player2.store.stones:2}]   "
            + "+"
            + "+".join(["-" * pw] * n)
            + "+"
            + f"   [{self.player1.store.stones:2}]   "
            + "|"
        )
        r_p1_labels = "|" + " " * sw + "|" + "|".join(f"{i + 1:^{pw}}" for i in range(n)) + "|" + " " * sw + "|"
        r_p1_stones = "|" + " " * sw + "|" + "|".join(f"  ({pit.stones:2})  " for pit in self.player1.pits) + "|" + " " * sw + "|"

        print()
        for row in [border, r_p2_labels, r_p2_stones, r_mid, r_p1_labels, r_p1_stones, border]:
            print(row)
        print()

    def is_game_over(self):
        """Return True if either player has no valid moves."""
        return not self.player1.has_valid_moves() or not self.player2.has_valid_moves()

    def get_all_positions(self):
        """Return all 14 positions as a flat list for sowing."""
        return self.player1.pits + [self.player1.store] + self.player2.pits + [self.player2.store]
