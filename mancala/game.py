"""
game.py
Contains the Game class. Controls setup, turns, and the game loop.
"""

try:
    from .board import Board
    from .player import ComputerPlayer, HumanPlayer
except ImportError:
    from board import Board
    from player import ComputerPlayer, HumanPlayer


class Game:
    """Controls setup, turn logic, and the main game loop."""

    def __init__(self, mode="terminal"):
        if mode == "terminal":
            self._setup_from_prompt()
        elif mode == "gui":
            self._setup_programmatic(mode=1, p1_name="Player 1", p2_name="Player 2")
        else:
            raise ValueError("mode must be 'terminal' or 'gui'.")

    def _setup_from_prompt(self):
        """Prompt for mode and player names, build the Board."""
        print("\n" + "=" * 50)
        print("           WELCOME TO MANCALA")
        print("=" * 50)
        print("  1. Two Players")
        print("  2. Player vs Computer")

        while True:
            try:
                mode = int(input("\n  Select mode (1 or 2): "))
                if mode in (1, 2):
                    break
                print("  Please enter 1 or 2.")
            except ValueError:
                print("  Invalid input.")

        if mode == 1:
            name1 = input("  Player 1 name: ").strip() or "Player 1"
            name2 = input("  Player 2 name: ").strip() or "Player 2"
            self._setup_programmatic(mode=1, p1_name=name1, p2_name=name2)
        else:
            name1 = input("  Your name: ").strip() or "Player 1"
            self._setup_programmatic(mode=2, p1_name=name1, p2_name="Computer")

    def _setup_programmatic(self, mode=1, p1_name="Player 1", p2_name="Player 2"):
        """Build a game without prompts for GUI or automation."""
        if mode == 1:
            p1 = HumanPlayer(p1_name)
            p2 = HumanPlayer(p2_name)
        elif mode == 2:
            p1 = HumanPlayer(p1_name)
            p2 = ComputerPlayer(p2_name)
        else:
            raise ValueError("mode must be 1 (PvP) or 2 (PvC).")

        self.board = Board(p1, p2)
        self.players = [p1, p2]
        self.current_idx = 0

    @property
    def current_player(self):
        """Return the player whose turn it is."""
        return self.players[self.current_idx]

    @property
    def opponent(self):
        """Return the other player."""
        return self.players[1 - self.current_idx]

    def switch_player(self):
        """Toggle current_idx between 0 and 1."""
        self.current_idx = 1 - self.current_idx

    def get_player_range(self, player):
        """Return the flat-board indices for a player's pits."""
        return range(0, 6) if player == self.players[0] else range(7, 13)

    def _execute_move(self, player, pit_idx):
        """Sow stones and apply bonus turn / capture rules. Return True if bonus turn."""
        all_pos = self.board.get_all_positions()

        if player == self.players[0]:
            flat_start = pit_idx
            own_range = range(0, 6)
            own_store = 6
            skip_store = 13
        else:
            flat_start = pit_idx + 7
            own_range = range(7, 13)
            own_store = 13
            skip_store = 6

        stones = all_pos[flat_start].sow()
        current = flat_start
        last = None

        for _ in range(stones):
            current = (current + 1) % 14
            if current == skip_store:
                current = (current + 1) % 14
            all_pos[current].add(1)
            last = current

        if last == own_store:
            return True

        if last in own_range and all_pos[last].stones == 1:
            opposite = 12 - last
            if not all_pos[opposite].is_empty():
                captured = all_pos[last].sow() + all_pos[opposite].sow()
                all_pos[own_store].add(captured)
                print(f"  {player.name} captured {captured} stones!")

        return False

    def take_turn(self):
        """Get a move from the current player and execute it."""
        player = self.current_player
        pit_idx = player.get_move(self.board)
        self.execute_turn(pit_idx)

    def execute_turn(self, pit_idx):
        """Execute one turn for current player from a 0-5 local pit index."""
        player = self.current_player

        if pit_idx not in range(0, 6):
            raise ValueError("pit_idx must be between 0 and 5.")
        if player.pits[pit_idx].is_empty():
            raise ValueError("That pit is empty.")

        extra_turn = self._execute_move(player, pit_idx)
        if not extra_turn:
            self.switch_player()
        return extra_turn

    def collect_remaining_and_finish(self):
        """Sweep remaining stones into stores if game has ended."""
        if self.board.is_game_over():
            for player in self.players:
                player.collect_remaining()

    def winner_name(self):
        """Return winner name, or None for tie."""
        p1_score = self.players[0].store.stones
        p2_score = self.players[1].store.stones
        if p1_score > p2_score:
            return self.players[0].name
        if p2_score > p1_score:
            return self.players[1].name
        return None

    def _declare_winner(self):
        """Print final scores and announce the winner."""
        p1 = self.players[0]
        p2 = self.players[1]
        p1_score = p1.store.stones
        p2_score = p2.store.stones

        print("=" * 50)
        print("              GAME OVER")
        print("=" * 50)
        print(f"  {p1.name:<20} {p1_score:>3} stones")
        print(f"  {p2.name:<20} {p2_score:>3} stones")
        print("-" * 50)

        if p1_score > p2_score:
            print(f"  {p1.name} WINS!\n")
        elif p2_score > p1_score:
            print(f"  {p2.name} WINS!\n")
        else:
            print("  It's a TIE!\n")

    def play(self):
        """Main game loop."""
        while not self.board.is_game_over():
            self.board.display()
            print(f"  ── {self.current_player.name}'s turn ──")
            self.take_turn()

        self.collect_remaining_and_finish()

        self.board.display()
        self._declare_winner()
