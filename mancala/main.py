"""
main.py
Entry point. Run this file to start the game.
"""

import argparse

try:
    from .game import Game
    from .gui import MancalaGUI
except ImportError:
    from game import Game
    from gui import MancalaGUI


def pick_display_mode():
    print("\nChoose display mode:")
    print("  1. Terminal")
    print("  2. Modern GUI")

    while True:
        raw = input("Select mode (1 or 2): ").strip()
        if raw == "1":
            return "terminal"
        if raw == "2":
            return "gui"
        print("Please enter 1 or 2.")


def run_terminal_mode():
    game = Game(mode="terminal")
    game.play()


def run_gui_mode():
    game = Game(mode="gui")
    # Start everyone with 4 stones in each pit, same as terminal mode.
    for player in game.players:
        for pit in player.pits:
            pit.stones = 4
        player.store.stones = 0

    app = MancalaGUI(game)
    app.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play Mancala in terminal or GUI mode.")
    parser.add_argument(
        "--display",
        choices=["terminal", "gui"],
        help="Display mode to launch directly.",
    )
    args = parser.parse_args()

    mode = args.display or pick_display_mode()
    if mode == "gui":
        run_gui_mode()
    else:
        run_terminal_mode()
