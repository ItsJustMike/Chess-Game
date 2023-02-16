board = [["-" for i in range(8)] for i in range(8)]
class Piece:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    pass
  
  def set_team(self, team):
    self.team = team
    
  def get_moves(self, x, y):
    pass
    
  def set_coord(self, x, y):
    self.x = x
    self.y = y
    
class Pawn(Piece):
  def __init__(self, x, y):
    super().__init__(x, y)
    self.has_moved = False

  def __str__(self):
    return "p"
  
  def set_team(self, team):
    super().set_team(team)
    
  def get_moves(self):
    moves = []
    if self.team == "black":
      try:
        if board[self.x + 1][self.y] == "-":
          moves.append([self.x + 1, self.y])
      except:
        pass
      try:
        if self.has_moved == False and board[self.x + 2][self.y] == "-":
          moves.append([self.x + 2, self.y])
      except:
        pass
      try:
        if board[self.x + 1][self.y + 1] != "-":
          moves.append([self.x + 1, self.y + 1])
      except:
        pass
      try:
        if board[self.x + 1][self.y - 1] != "-":
          moves.append([self.x + 1, self.y - 1])
      except:
        pass
      return moves
    if self.team == "white":
      try:
        if board[self.x - 1][self.y] == "-":
          moves.append([self.x - 1, self.y])
      except:
        pass
      try:
        if self.has_moved == False and board[self.x - 2][self.y] == "-":
          moves.append([self.x - 2, self.y])
      except:
        pass
      try:
        if board[self.x - 1][self.y + 1] != "-":
          moves.append([self.x - 1, self.y + 1])
      except:
        pass
      try:
        if board[self.x - 1][self.y - 1] != "-" and board[self.x - 1][self.y - 1].team == "black":
          moves.append([self.x - 1, self.y - 1])
      except:
        pass
      return moves

  def set_coord(self, x, y):
    super().set_coord(x, y)
      
    
class Rook(Piece):
  def __init__(self, x, y):
    super().__init__(x, y)
    self.blocked = False
  
  def __str__(self):
    return "r"

  def set_team(self, team):
    super().set_team(team)

  def can_take(self, x, y):
    if board[x][y] != "-" and board[x][y].team != self.team:
      self.blocked = True
      return True
    elif board[x][y] != "-" and board[x][y].team == self.team:
      self.blocked = True
      
  def check_area(self, x, y):
    if (x < 0 or y < 0) or (x > 7 or y > 7):
      return False
    try:
      if board[x][y] == "-" or self.can_take(x, y):
        return True
    except:
      return False
  
  def check_line(self, x, y, incx, incy):
    line = []
    self.blocked = False
    for i in range(8):
      x += incx
      y += incy
      if self.check_area(x, y):
        line.append([x, y])
      if self.blocked == True:
        break
    return line
  def get_moves(self):
    moves = []
    moves.append(self.check_line(self.x, self.y, 0, 1))
    moves.append(self.check_line(self.x, self.y, 1, 0))
    moves.append(self.check_line(self.x, self.y, 0, -1))
    moves.append(self.check_line(self.x, self.y, -1, 0))
    return moves
    # for i in range(8 - self.x):
    #   if i > self.x:
    #     break
    #   if board[self.x - i][self.y] == "-":
    #     moves.append([self.x - i, self.y])
    #   if board[self.x - i][self.y] != "-" and i != 0:
    #     if self.team != board[self.x - i][self.y].team:
    #       moves.append([self.x - i, self.y])
    #     break
    # for i in range(8 - self.x):
    #   try:
    #     if board[self.x + i][self.y] == "-":
    #       moves.append([self.x + i, self.y])
    #     if board[self.x + i][self.y] != "-" and i != 0:
    #       if self.team != board[self.x + i][self.y].team:
    #         moves.append([self.x + 1, self.y])
    #       break
    #   except:
    #     pass
    # for i in range((8 - self.y) + 1):
    #   if i > self.y:
    #     break
    #   if board[self.x][self.y - i] == "-":
    #     moves.append([self.x, self.y - i])
    #   if board[self.x][self.y - i] != "-" and i != 0:
    #     if self.team != board[self.x][self.y - i].team:
    #       moves.append([self.x, self.y - i])
    #     break

    # for i in range(8 - self.y):
    #   try:
    #     if board[self.x][self.y + i] == "-":
    #       moves.append([self.x, self.y + i])
    #     if board[self.x][self.y + i] != "-" and i != 0:
    #       if self.team != board[self.x][self.y + i].team:
    #         moves.append([self.x, self.y + i])
    #       break
    #   except:
    #     pass
    # return moves
  def set_coord(self, x, y):
    super().set_coord(x, y)
    
class Knight(Piece):
  def __init__(self, x, y):
    super().__init__(x, y)
    
  def __str__(self):
    return "k"

  def set_team(self, team):
    super().set_team(team)
    
  def can_take(self, x, y):
    if board[x][y] != "-" and board[x][y].team != self.team:
        return True
      
  def check_area(self, x, y):
    if (x < 0 or y < 0) or (x > 7 or y > 7):
      return False
    if board[x][y] == "-" or self.can_take(x, y):
        return True
    return False
      
  def get_moves(self):
    moves = []
    #Check down to the right
    if self.check_area(self.x + 2, self.y + 1):
      moves.append([self.x + 2, self.y + 1])
    #Check down to the left
    if self.check_area(self.x + 2, self.y - 1):
      moves.append([self.x + 2, self.y - 1])
    #Check up to the right
    if self.check_area(self.x - 2, self.y + 1):
      moves.append([self.x - 2, self.y + 1])
    #Check up to the left
    if self.check_area(self.x - 2, self.y - 1):
      moves.append([self.x - 2, self.y - 1])
    #Check left-up
    if self.check_area(self.x - 1, self.y - 2):
      moves.append([self.x - 1, self.y - 2])
    #Check left-down
    if self.check_area(self.x + 1, self.y - 2):
      moves.append([self.x + 1, self.y - 2])
    #Check right-up
    if self.check_area(self.x - 1, self.y + 2):
      moves.append([self.x - 1, self.y + 2])
    #Check right-down
    if self.check_area(self.x + 1, self.y + 2):
      moves.append([self.x + 1, self.y + 2])
    return moves
  def set_coord(self, x, y):
    super().set_coord(x, y)

class Bishop(Piece):
  def __init__(self, x, y):
    super().__init__(x, y)
    self.blocked = False

  def __str__(self):
    return "b"

  def set_team(self, team):
    super().set_team(team)
      
  def can_take(self, x, y):
    if board[x][y] != "-" and board[x][y].team != self.team:
      self.blocked = True 
      return True
    elif board[x][y] != "-" and board[x][y].team == self.team:
      self.blocked = True
      return False

      
  def check_area(self, x, y):
    if (x < 0 or y < 0) or (x > 7 or y > 7):
      return False
    if board[x][y] == "-" or self.can_take(x, y):
        return True
    return False
    
  def diagonal(self, x, y, incx, incy):
    diagonal = []
    self.blocked = False
    for i in range(8):
      x += incx
      y += incy
      if self.check_area(x, y):
        diagonal.append([x, y])
      if self.blocked == True:
        break
    return diagonal
      

  def get_moves(self):
    moves = []
    moves.append(self.diagonal(self.x, self.y, -1, -1))
    moves.append(self.diagonal(self.x, self.y, -1, 1))
    moves.append(self.diagonal(self.x, self.y, 1, -1))
    moves.append(self.diagonal(self.x, self.y, 1, 1))
    return moves

  def set_coord(self, x, y):
    super().set_coord(x, y)
    
class King(Piece):

  def __init__(self, x, y):
    super().__init__(x, y)

  def __str__(self):
    return "K"

  def set_team(self, team):
    super().set_team(team)
    
  def can_take(self, x, y):
    if board[x][y] != "-" and board[x][y].team != self.team:
      self.blocked = True 
      return True
    elif board[x][y] != "-" and board[x][y].team == self.team:
      self.blocked = True
      return False

  def check_area(self, x, y):
    if (x < 0 or y < 0) or (x > 7 or y > 7):
      return False
    if board[x][y] == "-" or self.can_take(x, y):
        return True
    return False
    
  def get_moves(self):
    moves = []
    if self.check_area(self.x + 1, self.y + 1):
      moves.append([self.x + 1, self.y + 1])
    if self.check_area(self.x + 1, self.y):
      moves.append([self.x + 1, self.y])
    if self.check_area(self.x, self.y + 1):
      moves.append([self.x, self.y + 1])
    if self.check_area(self.x - 1, self.y):
      moves.append([self.x - 1, self.y])
    if self.check_area(self.x, self.y - 1):
      moves.append([self.x, self.y - 1])
    if self.check_area(self.x - 1, self.y - 1):
      moves.append([self.x - 1, self.y - 1])
    if self.check_area(self.x - 1, self.y + 1):
      moves.append([self.x - 1, self.y + 1])
    if self.check_area(self.x + 1, self.y - 1):
      moves.append([self.x + 1, self.y - 1])
    return moves
  def set_coord(self, x, y):
    super().set_coord(x, y)
    
class Queen(Piece):

  def __init__(self, x, y):
    super().__init__(x, y)

  def __str__(self):
    return "q"

  def set_team(self, team):
    super().set_team(team)
    
  def can_take(self, x, y):
    if board[x][y] != "-" and board[x][y].team != self.team:
      self.blocked = True 
      return True
    elif board[x][y] != "-" and board[x][y].team == self.team:
      self.blocked = True
      return False

      
  def check_area(self, x, y):
    if (x < 0 or y < 0) or (x > 7 or y > 7):
      return False
    if board[x][y] == "-" or self.can_take(x, y):
        return True
    return False
    
  def diagonal(self, x, y, incx, incy):
    diagonal = []
    self.blocked = False
    for i in range(8):
      x += incx
      y += incy
      if self.check_area(x, y):
        diagonal.append([x, y])
      if self.blocked == True:
        break
    return diagonal
    
  def check_line(self, x, y, incx, incy):
    line = []
    self.blocked = False
    for i in range(8):
      x += incx
      y += incy
      if self.check_area(x, y):
        line.append([x, y])
      if self.blocked == True:
        break
    return line
    
  def get_moves(self):
    moves = []
    moves.append(Bishop.get_moves(self))
    moves.append(Rook.get_moves(self))
    return Bishop.get_moves(self) + Rook.get_moves(self)
    
  def set_coord(self, x, y):
    super().set_coord(x, y)
def initialize_board():
  board[0][0] = Rook(0, 0)
  board[0][0].set_team("black")
  board[0][1] = Knight(0, 1)
  board[0][1].set_team("black")
  board[0][2] = Bishop(0, 2)
  board[0][2].set_team("black")
  board[0][3] = Queen(0, 3)
  board[0][3].set_team("black")
  board[0][4] = King(0, 4)
  board[0][4].set_team("black")
  board[0][5] = Bishop(0, 5)
  board[0][5].set_team("black")
  board[0][6] = Knight(0, 6)
  board[0][6].set_team("black")
  board[0][7] = Rook(0, 7)
  board[0][7].set_team("black")
  board[7][0] = Rook(7, 0)
  board[7][0].set_team("white")
  board[7][1] = Knight(7, 1)
  board[7][1].set_team("white")
  board[7][2] = Bishop(7, 2)
  board[7][2].set_team("white")
  board[7][3] = Queen(7, 3)
  board[7][3].set_team("white")
  board[7][4] = King(7, 4)
  board[7][4].set_team("white")
  board[7][5] = Bishop(7, 5)
  board[7][5].set_team("white")
  board[7][6] = Knight(7, 6)
  board[7][6].set_team("white")
  board[7][7] = Rook(7, 7)
  board[7][7].set_team("white")
  print()
  for i in range(8):
    board[1][i] = Pawn(1, i)
    board[1][i].set_team("black")
    board[6][i] = Pawn(6, i)
    board[6][i].set_team("white")
def display_board():
  for x in range(8):
    print()
    for y in range(8):
      try:
        print(board[x][y].__str__(), end=" ")
      except:
        print(end="-")
  print()

def move_piece(piece, x1, y1):
  board[piece.x][piece.y] = "-"
  board[x1][y1] = piece
  piece.set_coord(x1, y1)
  piece.has_moved = True