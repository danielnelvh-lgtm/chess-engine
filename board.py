#Board class: squares, side to move, castling, en passant, make/unmake
EMPTY = 0
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

#Forsyth–Edwards Notation (FEN)
FEN_TO_PIECE = {"p": PAWN, "n": KNIGHT, "b": BISHOP, "r": ROOK, "q": QUEEN, "k": KING,}

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

class Board:
    def __init__(self, fen=START_FEN):
        self.squares = [EMPTY] * 64
        self.side.to_move = True
        self.load_fen(fen)