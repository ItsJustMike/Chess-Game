from piece import *
winner = None
def main_loop():
  initialize_board()
  display_board()
  move_piece(board[0][3], 3, 3)
  print(board[3][3].get_moves())
  # while winner == None:
  #   x = int(input("X coordinate: "))
  #   y = int(input("Y coordinate: "))
  #   newx = int(input("New X: "))
  #   newy = int(input("New Y: "))
  #   if [newx, newy] in board[x][y].get_moves():
  #     move_piece(board[x][y], newx, newy)
  #   else:
  #     print("Invalid Move")
  #     continue
  display_board()
  
main_loop()
#add check for enemy team






















