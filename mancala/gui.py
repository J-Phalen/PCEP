"""
gui.py
Tkinter GUI that uses the same game logic from game.py.
"""

import tkinter as tk

try:
    from .game import Game
    from .player import ComputerPlayer
except ImportError:
    from game import Game
    from player import ComputerPlayer


class MancalaGUI:
    """Modern GUI frontend that reuses Game move/capture logic."""

    def __init__(self, game=None):
        self.game = game if game is not None else Game(mode="gui")

        self.root = tk.Tk()
        self.root.title("Mancala - GUI")
        self.root.resizable(False, False)

        self.canvas_width = 1200
        self.canvas_height = 520
        self.canvas = tk.Canvas(
            self.root,
            width=self.canvas_width,
            height=self.canvas_height,
            bg="#f4f1ea",
            highlightthickness=0,
        )
        self.canvas.pack(padx=16, pady=16)

        self.space_to_shape = {}
        self.space_to_text = {}
        self._space_to_local = {
            0: (0, 0),
            1: (0, 1),
            2: (0, 2),
            3: (0, 3),
            4: (0, 4),
            5: (0, 5),
            7: (1, 0),
            8: (1, 1),
            9: (1, 2),
            10: (1, 3),
            11: (1, 4),
            12: (1, 5),
        }

        # Cache previous values so refresh updates only changed text items.
        self._last_space_values = [None] * 14
        self.status_text_id = None

        self._draw_board()
        self._draw_status_panel()
        self.refresh_view(force=True)

        # If current player is a computer in future modes, execute it.
        self.root.after(150, self._maybe_run_computer_turn)

    def _draw_board(self):
        x1, y1 = 20, 20
        x2, y2 = self.canvas_width - 20, self.canvas_height - 120

        self.canvas.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            fill="#c7ab84",
            outline="#5a422c",
            width=4,
        )

        middle_y = (y1 + y2) // 2
        self.canvas.create_rectangle(x1 + 6, y1 + 6, x2 - 6, middle_y, fill="#ddd7ca", outline="")
        self.canvas.create_rectangle(x1 + 6, middle_y, x2 - 6, y2 - 6, fill="#cec6b6", outline="")

        store_width = 110
        store_margin = 24
        store_top = y1 + 26
        store_bottom = y2 - 26

        # Space 13: player 2 store (left)
        left_store = self.canvas.create_rectangle(
            x1 + store_margin,
            store_top,
            x1 + store_margin + store_width,
            store_bottom,
            fill="#cfc8b9",
            outline="#5a3f26",
            width=3,
        )
        self._register_space(13, left_store)

        # Space 6: player 1 store (right)
        right_store = self.canvas.create_rectangle(
            x2 - store_margin - store_width,
            store_top,
            x2 - store_margin,
            store_bottom,
            fill="#bfb7a7",
            outline="#5a3f26",
            width=3,
        )
        self._register_space(6, right_store)

        pits_per_row = 6
        pit_size = 110
        pit_gap = 18
        pits_total_width = pits_per_row * pit_size + (pits_per_row - 1) * pit_gap
        pits_start_x = (self.canvas_width - pits_total_width) // 2
        top_y = y1 + 52
        bottom_y = y2 - 52 - pit_size

        for i in range(pits_per_row):
            px1 = pits_start_x + i * (pit_size + pit_gap)
            px2 = px1 + pit_size

            # Top row belongs to player 2 and maps to spaces 12..7 (left to right).
            top_space = 12 - i
            top_pit = self.canvas.create_rectangle(
                px1,
                top_y,
                px2,
                top_y + pit_size,
                fill="#ddd7ca",
                outline="#5a3f26",
                width=3,
            )
            self._register_space(top_space, top_pit)

            # Bottom row belongs to player 1 and maps to spaces 0..5 (left to right).
            bottom_space = i
            bottom_pit = self.canvas.create_rectangle(
                px1,
                bottom_y,
                px2,
                bottom_y + pit_size,
                fill="#cec6b6",
                outline="#5a3f26",
                width=3,
            )
            self._register_space(bottom_space, bottom_pit)

    def _draw_status_panel(self):
        panel_y = self.canvas_height - 82
        self.canvas.create_rectangle(
            20,
            panel_y,
            self.canvas_width - 20,
            self.canvas_height - 20,
            fill="#ede8dc",
            outline="#8c7a62",
            width=2,
        )

        self.status_text_id = self.canvas.create_text(
            34,
            self.canvas_height - 52,
            text="",
            fill="#2f2418",
            font=("Segoe UI", 12, "bold"),
            anchor="w",
        )

    def _register_space(self, space_index, shape_id):
        self.space_to_shape[space_index] = shape_id
        self.canvas.tag_bind(shape_id, "<Button-1>", lambda _event, s=space_index: self._on_space_click(s))

        x1, y1, x2, y2 = self.canvas.coords(shape_id)
        text_id = self.canvas.create_text(
            (x1 + x2) / 2,
            (y1 + y2) / 2,
            text="0",
            fill="#2f2418",
            font=("Segoe UI", 14, "bold"),
        )
        self.space_to_text[space_index] = text_id

    def _set_status(self, text):
        self.canvas.itemconfigure(self.status_text_id, text=text)

    def _set_status_for_turn(self):
        p1 = self.game.players[0]
        p2 = self.game.players[1]
        turn_text = f"{self.game.current_player.name}'s turn"
        score_text = f"{p1.name}: {p1.store.stones}  |  {p2.name}: {p2.store.stones}"
        self._set_status(f"{turn_text}    {score_text}")

    def _finish_game_if_over(self):
        if not self.game.board.is_game_over():
            return False

        self.game.collect_remaining_and_finish()
        self.refresh_view(force=True)
        winner = self.game.winner_name()
        if winner is None:
            self._set_status("Game over. It's a tie.")
        else:
            self._set_status(f"Game over. {winner} wins!")
        return True

    def _on_space_click(self, space_index):
        if self.game.board.is_game_over():
            return

        mapped = self._space_to_local.get(space_index)
        if mapped is None:
            self._set_status("Store clicked. Choose one of your pits.")
            return

        current_player_idx, local_pit = mapped
        if current_player_idx != self.game.current_idx:
            self._set_status("That pit belongs to the other player.")
            return

        player = self.game.current_player
        if player.pits[local_pit].is_empty():
            self._set_status("That pit is empty. Choose another pit.")
            return

        extra_turn = self.game.execute_turn(local_pit)
        self.refresh_view()

        if self._finish_game_if_over():
            return

        if extra_turn:
            self._set_status(f"Bonus turn for {self.game.current_player.name}.")
        else:
            self._set_status_for_turn()

        self._maybe_run_computer_turn()

    def _maybe_run_computer_turn(self):
        if self.game.board.is_game_over():
            return

        player = self.game.current_player
        if not isinstance(player, ComputerPlayer):
            return

        local_pit = player.get_move(self.game.board)
        extra_turn = self.game.execute_turn(local_pit)
        self.refresh_view()

        if self._finish_game_if_over():
            return

        if extra_turn:
            self._set_status(f"Bonus turn for {self.game.current_player.name}.")
            self.root.after(250, self._maybe_run_computer_turn)
        else:
            self._set_status_for_turn()

    def refresh_view(self, force=False):
        all_positions = self.game.board.get_all_positions()
        for space_index in range(14):
            stones = all_positions[space_index].stones
            if force or stones != self._last_space_values[space_index]:
                text_id = self.space_to_text[space_index]
                self.canvas.itemconfigure(text_id, text=str(stones))
                self._last_space_values[space_index] = stones

        self._set_status_for_turn()

    def run(self):
        self.root.mainloop()
