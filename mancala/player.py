"""
player.py
Contains Player (base), HumanPlayer, and ComputerPlayer.
"""

import random

try:
    from .pit import Pit, Store
except ImportError:
    from pit import Pit, Store


class Player:
    """Abstract base class for all player types."""

    def __init__(self, name):
        self.name = name
        self.pits = [Pit() for _ in range(6)]
        self.store = Store()

        # Verify no stores accidentally ended up in pits
        assert not any(pit.is_store for pit in self.pits), "pits must not contain Store objects"
        # Verify store is actually a Store
        assert self.store.is_store, "store must be a Store object"

    def has_valid_moves(self):
        """Return True if at least one pit is non-empty."""
        return any(not pit.is_empty() for pit in self.pits)

    def collect_remaining(self):
        """Sweep all pit stones into the store at game end."""
        for pit in self.pits:
            if not pit.is_store:
                self.store.add(pit.sow())

    def get_move(self, board):
        """Return a 0-indexed pit choice. Must be overridden."""
        raise NotImplementedError("Subclasses must implement get_move()")


class HumanPlayer(Player):
    """Prompts the user for input."""

    def get_move(self, board):
        while True:
            try:
                choice = int(input(f"  {self.name}, pick a pit (1-6): "))
                if choice not in range(1, 7):
                    print("  Please enter a number between 1 and 6.")
                    continue
                if self.pits[choice - 1].is_empty():
                    print("  That pit is empty! Choose another.")
                    continue
                return choice - 1
            except ValueError:
                print("  Invalid input — enter a whole number between 1 and 6.")


class ComputerPlayer(Player):
    """Randomly selects a valid pit."""

    def get_move(self, board):
        valid_moves = [i for i, pit in enumerate(self.pits) if not pit.is_empty()]
        choice = random.choice(valid_moves)
        print(f"  {self.name} selects pit {choice + 1}.")
        return choice
