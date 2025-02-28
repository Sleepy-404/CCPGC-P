# prompt: make a chess site that allows you to make an AI to mimicyour moves.

import chess

def print_board(board):
  print(board)

def main():
  board = chess.Board()
  print_board(board)

  while not board.is_game_over():
    try:
      move_str = input("Enter your move (e.g., e2e4): ")
      move = chess.Move.from_uci(move_str)

      if move in board.legal_moves:
        board.push(move)
        print_board(board)
        # Add AI move logic here (replace with actual AI)
        print("AI making move...")  
        ai_move = list(board.legal_moves)[0] # Placeholder: AI chooses the first legal move. 
        board.push(ai_move)
        print_board(board)
      else:
        print("Illegal move. Try again.")

    except ValueError:
      print("Invalid move format.  Use UCI notation (e.g., e2e4).")

  print("Game Over")


if __name__ == "__main__":
  main()
