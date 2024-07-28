import chess

players = ["White", "Black"]

board = chess.Board()
print(board)

def Move():
    move = chess.Move.from_uci(input("move: "))
    if move in board.legal_moves:
        board.push(move)
    else:
        print(f"{move} is not legal")

def Board_controll(player):
    print(board)
    if board.is_checkmate():
        print(f"{player} win")
        return True
    if board.is_stalemate():
        print("Stalemate")
        return True

    return False

while True:
    for i in players:
        Move()
        if Board_controll(i):
            break
