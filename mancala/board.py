import tkinter as tk


class MancalaBoardUI:
    def __init__(self) -> None:
        canvas_width = 1200
        canvas_height = 430

        self.root = tk.Tk()
        self.root.title("Mancala")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=canvas_width,
            height=canvas_height,
            bg="#ffffff",
            highlightthickness=0,
        )
        self.canvas.pack(padx=16, pady=16)

        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        # Keep these for future game-state mapping.
        self.store_ids: list[int] = []
        self.pit_ids: list[int] = []
        self.top_row_pit_ids: list[int] = []
        self.bottom_row_pit_ids: list[int] = []
        self.player1_pits: list[int] = []
        self.player2_pits: list[int] = []
        self.pit_owner: dict[int, str] = {}

        # Logical game-state model (14 assignable spaces total):
        # 0-5   -> Player 1 bottom row pits (left to right)
        # 6     -> Player 1 store (right rectangle)
        # 7-12  -> Player 2 top row pits (left to right)
        # 13    -> Player 2 store (left rectangle)
        self.space_values: list[int] = [0] * 14
        self.space_to_canvas: dict[int, int] = {}
        self.canvas_to_space: dict[int, int] = {}

        self._draw_board()
        self._build_space_mapping()

    def _draw_board(self) -> None:
        board = self._board_bounds()
        self._draw_outer_board(board)
        self._draw_player_zones(board)
        self._draw_stores(board)
        self._draw_pits(board)

    def _board_bounds(self) -> tuple[int, int, int, int]:
        board_margin = 20
        return (
            board_margin,
            board_margin,
            self.canvas_width - board_margin,
            self.canvas_height - board_margin,
        )

    def _draw_outer_board(self, board: tuple[int, int, int, int]) -> None:
        board_color = "#c8a97e"
        board_outline_color = "#6b4f32"

        x1, y1, x2, y2 = board
        self.canvas.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            fill=board_color,
            outline=board_outline_color,
            width=4,
        )

    def _draw_player_zones(self, board: tuple[int, int, int, int]) -> None:
        # Visual split: top area is Player 2, bottom area is Player 1.
        x1, y1, x2, y2 = board
        middle_y = (y1 + y2) // 2
        inset = 6

        self.canvas.create_rectangle(
            x1 + inset,
            y1 + inset,
            x2 - inset,
            middle_y,
            fill="#e3ded3",
            outline="",
        )
        self.canvas.create_rectangle(
            x1 + inset,
            middle_y,
            x2 - inset,
            y2 - inset,
            fill="#d4cec1",
            outline="",
        )

    def _draw_stores(self, board: tuple[int, int, int, int]) -> None:
        store_width = 110
        store_margin = 24
        store_vertical_padding = 26
        player2_store_color = "#cfc8b9"
        player1_store_color = "#bfb7a7"
        shape_outline_color = "#5a3f26"

        x1, y1, x2, y2 = board
        store_top = y1 + store_vertical_padding
        store_bottom = y2 - store_vertical_padding

        left_store = self.canvas.create_rectangle(
            x1 + store_margin,
            store_top,
            x1 + store_margin + store_width,
            store_bottom,
            fill=player2_store_color,
            outline=shape_outline_color,
            width=3,
        )

        right_store = self.canvas.create_rectangle(
            x2 - store_margin - store_width,
            store_top,
            x2 - store_margin,
            store_bottom,
            fill=player1_store_color,
            outline=shape_outline_color,
            width=3,
        )

        self.store_ids = [left_store, right_store]
        self.player2_pits.append(left_store)
        self.player1_pits.append(right_store)
        self.pit_owner[left_store] = "player2"
        self.pit_owner[right_store] = "player1"

    def _draw_pits(self, board: tuple[int, int, int, int]) -> None:
        pits_per_row = 6
        pit_size = 110
        pit_gap = 18
        pit_vertical_offset = 52
        player2_pit_color = "#ddd7ca"
        player1_pit_color = "#cec6b6"
        shape_outline_color = "#5a3f26"

        _, y1, _, y2 = board

        pits_total_width = pits_per_row * pit_size + (pits_per_row - 1) * pit_gap
        pits_start_x = (self.canvas_width - pits_total_width) // 2
        top_pit_y = y1 + pit_vertical_offset
        bottom_pit_y = y2 - pit_vertical_offset - pit_size

        top_row_ids: list[int] = []
        bottom_row_ids: list[int] = []

        for i in range(pits_per_row):
            x1 = pits_start_x + i * (pit_size + pit_gap)
            x2 = x1 + pit_size

            top_pit = self.canvas.create_rectangle(
                x1,
                top_pit_y,
                x2,
                top_pit_y + pit_size,
                fill=player2_pit_color,
                outline=shape_outline_color,
                width=3,
            )
            bottom_pit = self.canvas.create_rectangle(
                x1,
                bottom_pit_y,
                x2,
                bottom_pit_y + pit_size,
                fill=player1_pit_color,
                outline=shape_outline_color,
                width=3,
            )

            self.pit_ids.extend([top_pit, bottom_pit])
            top_row_ids.append(top_pit)
            bottom_row_ids.append(bottom_pit)
            self.player2_pits.append(top_pit)
            self.player1_pits.append(bottom_pit)
            self.pit_owner[top_pit] = "player2"
            self.pit_owner[bottom_pit] = "player1"

        self.top_row_pit_ids = top_row_ids
        self.bottom_row_pit_ids = bottom_row_ids

    def _build_space_mapping(self) -> None:
        if len(self.store_ids) != 2:
            raise ValueError("Expected exactly 2 stores.")
        if len(self.top_row_pit_ids) != 6 or len(self.bottom_row_pit_ids) != 6:
            raise ValueError("Expected exactly 6 top pits and 6 bottom pits.")

        # Player 1 pits and store.
        for index, pit_id in enumerate(self.bottom_row_pit_ids):
            self.space_to_canvas[index] = pit_id

        player1_store_id = self.store_ids[1]
        self.space_to_canvas[6] = player1_store_id

        # Player 2 pits and store.
        for offset, pit_id in enumerate(self.top_row_pit_ids):
            self.space_to_canvas[7 + offset] = pit_id

        player2_store_id = self.store_ids[0]
        self.space_to_canvas[13] = player2_store_id

        self.canvas_to_space = {canvas_id: space for space, canvas_id in self.space_to_canvas.items()}

    def _validate_space(self, space_index: int) -> None:
        if not 0 <= space_index < len(self.space_values):
            raise ValueError("space_index must be between 0 and 13.")

    def get_space_value(self, space_index: int) -> int:
        self._validate_space(space_index)
        return self.space_values[space_index]

    def set_space_value(self, space_index: int, value: int) -> None:
        self._validate_space(space_index)
        if value < 0:
            raise ValueError("value cannot be negative.")
        self.space_values[space_index] = value

    def add_to_space(self, space_index: int, amount: int) -> None:
        self._validate_space(space_index)
        if amount < 0:
            raise ValueError("amount cannot be negative.")
        self.space_values[space_index] += amount

    def remove_from_space(self, space_index: int, amount: int) -> None:
        self._validate_space(space_index)
        if amount < 0:
            raise ValueError("amount cannot be negative.")
        if amount > self.space_values[space_index]:
            raise ValueError("Cannot remove more than the current value.")
        self.space_values[space_index] -= amount

    def set_all_non_store_pits(self, value: int) -> None:
        if value < 0:
            raise ValueError("value cannot be negative.")

        for index in range(14):
            if index in (6, 13):
                continue
            self.space_values[index] = value

    def reset_space_values(self) -> None:
        self.space_values = [0] * 14

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    MancalaBoardUI().run()
