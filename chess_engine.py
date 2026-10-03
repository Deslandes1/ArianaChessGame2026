"""
Ariana Chess Engine — pure-Python chess rules.
Mirrors the JavaScript engine running inside chess_game.html.
Useful for server-side validation, testing, and future analysis features.
"""

from __future__ import annotations
from typing import Optional

FILES = "abcdefgh"
PIECE_LETTERS = {
    "K": "♔", "Q": "♕", "R": "♖", "B": "♗", "N": "♘", "P": "♙",
    "k": "♚", "q": "♛", "r": "♜", "b": "♝", "n": "♞", "p": "♟",
}

START_BOARD = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]


def inside(r: int, c: int) -> bool:
    return 0 <= r < 8 and 0 <= c < 8


def is_white(p: str) -> bool:
    return bool(p) and p == p.upper()


class ChessEngine:
    """Fully self-contained chess position + legal move generator."""

    def __init__(self):
        self.board = [row[:] for row in START_BOARD]
        self.turn = "w"
        self.last_move: Optional[tuple[tuple[int, int], tuple[int, int]]] = None

    # ── helpers ──────────────────────────────────────────────
    def piece_at(self, r: int, c: int) -> str:
        return self.board[r][c] if inside(r, c) else ""

    def find_king(self, white: bool) -> Optional[tuple[int, int]]:
        target = "K" if white else "k"
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == target:
                    return (r, c)
        return None

    def ascii_board(self) -> str:
        lines = []
        lines.append("  +------------------------+")
        for r in range(8):
            rank = 8 - r
            row = " | ".join(PIECE_LETTERS.get(self.board[r][c], "·")
                            for c in range(8))
            lines.append(f"{rank} | {row} |")
        lines.append("  +------------------------+")
        lines.append("    a   b   c   d   e   f   g   h")
        return "\n".join(lines)

    # ── attack detection ─────────────────────────────────────
    def is_attacked(self, r: int, c: int, by_white: bool) -> bool:
        b = self.board
        # pawns
        pr = r + (1 if by_white else -1)
        for dc in (-1, 1):
            if inside(pr, c + dc):
                p = b[pr][c + dc]
                if p == ("P" if by_white else "p"):
                    return True
        # knights
        for dr, dc in ((-2, -1), (-2, 1), (-1, -2), (-1, 2),
                       (1, -2), (1, 2), (2, -1), (2, 1)):
            rr, cc = r + dr, c + dc
            if inside(rr, cc) and b[rr][cc] == ("N" if by_white else "n"):
                return True
        # adjacent king
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if inside(rr, cc) and b[rr][cc] == ("K" if by_white else "k"):
                    return True
        # sliders
        straight = ((-1, 0), (1, 0), (0, -1), (0, 1))
        diagonal = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        for dr, dc in straight:
            rr, cc = r + dr, c + dc
            while inside(rr, cc):
                p = b[rr][cc]
                if p:
                    if p == ("R" if by_white else "r") or p == ("Q" if by_white else "q"):
                        return True
                    break
                rr += dr
                cc += dc
        for dr, dc in diagonal:
            rr, cc = r + dr, c + dc
            while inside(rr, cc):
                p = b[rr][cc]
                if p:
                    if p == ("B" if by_white else "b") or p == ("Q" if by_white else "q"):
                        return True
                    break
                rr += dr
                cc += dc
        return False

    def is_in_check(self, white: bool) -> bool:
        k = self.find_king(white)
        return bool(k) and self.is_attacked(k[0], k[1], not white)

    # ── move generation ──────────────────────────────────────
    def _pseudo_moves_from(self, r: int, c: int) -> list[tuple[int, int]]:
        p = self.board[r][c]
        if not p:
            return []
        white = is_white(p)
        moves: list[tuple[int, int]] = []

        def can_land(rr: int, cc: int) -> bool:
            if not inside(rr, cc):
                return False
            t = self.board[rr][cc]
            return not t or is_white(t) != white

        # PAWN
        if p in ("P", "p"):
            direction = -1 if white else 1
            start_rank = 6 if white else 1
            one = r + direction
            if inside(one, c) and not self.board[one][c]:
                moves.append((one, c))
                two = r + 2 * direction
                if r == start_rank and not self.board[two][c]:
                    moves.append((two, c))
            for dc in (-1, 1):
                rr, cc = r + direction, c + dc
                if inside(rr, cc):
                    t = self.board[rr][cc]
                    if t and is_white(t) != white:
                        moves.append((rr, cc))
            return moves

        # KNIGHT
        if p in ("N", "n"):
            for dr, dc in ((-2, -1), (-2, 1), (-1, -2), (-1, 2),
                           (1, -2), (1, 2), (2, -1), (2, 1)):
                if can_land(r + dr, c + dc):
                    moves.append((r + dr, c + dc))
            return moves

        # BISHOP / ROOK / QUEEN
        dirs = []
        if p in ("B", "b", "Q", "q"):
            dirs += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        if p in ("R", "r", "Q", "q"):
            dirs += [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in dirs:
            rr, cc = r + dr, c + dc
            while inside(rr, cc):
                t = self.board[rr][cc]
                if not t:
                    moves.append((rr, cc))
                else:
                    if is_white(t) != white:
                        moves.append((rr, cc))
                    break
                rr += dr
                cc += dc
        if dirs:
            return moves

        # KING
        if p in ("K", "k"):
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    if can_land(r + dr, c + dc):
                        moves.append((r + dr, c + dc))
            return moves

        return moves

    def legal_moves_from(self, r: int, c: int) -> list[tuple[int, int]]:
        p = self.board[r][c]
        if not p:
            return []
        white = is_white(p)
        legal = []
        for tr, tc in self._pseudo_moves_from(r, c):
            captured = self.board[tr][tc]
            self.board[tr][tc] = p
            self.board[r][c] = ""
            safe = not self.is_in_check(white)
            self.board[r][c] = p
            self.board[tr][tc] = captured
            if safe:
                legal.append((tr, tc))
        return legal

    def all_legal_moves(self) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        white = self.turn == "w"
        out = []
        for r in range(8):
            for c in range(8):
                p = self.board[r][c]
                if not p or is_white(p) != white:
                    continue
                for tr, tc in self.legal_moves_from(r, c):
                    out.append(((r, c), (tr, tc)))
        return out

    # ── game state ───────────────────────────────────────────
    def is_checkmate(self) -> bool:
        return self.is_in_check(self.turn == "w") and not self.all_legal_moves()

    def is_stalemate(self) -> bool:
        return not self.is_in_check(self.turn == "w") and not self.all_legal_moves()

    # ── making a move ────────────────────────────────────────
    def make_move(self, from_sq: tuple[int, int], to_sq: tuple[int, int]) -> bool:
        r, c = from_sq
        tr, tc = to_sq
        if (tr, tc) not in self.legal_moves_from(r, c):
            return False
        p = self.board[r][c]
        self.board[tr][tc] = p
        self.board[r][c] = ""
        # promotion
        if p == "P" and tr == 0:
            self.board[tr][tc] = "Q"
        elif p == "p" and tr == 7:
            self.board[tr][tc] = "q"
        self.last_move = (from_sq, to_sq)
        self.turn = "b" if self.turn == "w" else "w"
        return True

    def square_name(self, r: int, c: int) -> str:
        return f"{FILES[c]}{8 - r}"


# ─────────────────────────────────────────────────────────────
# Quick self-test (runs only when executing this file directly)
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    eng = ChessEngine()
    print(eng.ascii_board())
    print(f"\nTurn: {'White' if eng.turn == 'w' else 'Black'}")
    print(f"Legal moves for White: {len(eng.all_legal_moves())}")

    # Play the classic 1. e4 e5 2. Qh5 Nc6 3. Bc4 Nf6 4. Qxf7# (Scholar's mate)
    for move in [((6, 4), (4, 4)), ((1, 4), (3, 4)),
                 ((7, 3), (3, 7)), ((0, 1), (2, 2)),
                 ((7, 5), (4, 2)), ((0, 6), (2, 5)),
                 ((3, 7), (1, 5))]:
        eng.make_move(*move)

    print("\nAfter Scholar's mate attempt:")
    print(eng.ascii_board())
    print(f"Checkmate: {eng.is_checkmate()}")
