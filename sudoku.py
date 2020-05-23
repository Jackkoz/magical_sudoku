# Global variable for number of solved sudoku boards.
num_solutions = 0

def fill_board(current_number, current_square, board):
  global num_solutions
  if current_number == 10:
      num_solutions += 1
      if num_solutions == 1:
        print_board(board)
      if num_solutions % 10000 == 0:
        print(num_solutions)
      return
  if current_square == 9:
      new_number = current_number + 1
      fill_board(new_number, 0, board)
      return
  if current_number == 1 and current_square == 3:
      if (is_move_valid(board, 38, 1)):
          place_number(current_number, current_square, 38, board)
          return
  if current_number == 2 and current_square == 5:
      if (is_move_valid(board, 51, 2)):
          place_number(current_number, current_square, 51, board)
          return

  for position in get_square_positions(current_square):
      if is_move_valid(board, position, current_number):
          place_number(current_number, current_square, position, board)

def place_number(current_number, current_square, position, board):
    new_board = board.copy()
    new_board[position] = current_number
    next_square = current_square + 1
    fill_board(current_number, next_square, new_board)


def is_move_valid(board, position, number):
    if (position > 80 or position < 0):
        raise Exception('bad position number: %d' % position)
    if board[position] != 0:
        return False
    if any(number == board[x] for x in get_row_from_position(position)):
        return False
    if any(number == board[x] for x in get_column_from_position(position)):
        return False
    if any(number == board[x] for x in get_square_positions(get_square_id_from_position(position))):
        return False

    return True

# Returns the board positions in the square with the provided id.
def get_square_positions(square_id):
   return list(map(lambda x: x % 3 + (square_id % 3) * 3 + 9 * (x // 3) + 27 * (square_id // 3), range(0, 9)))

def print_board(board):
    for x in range(0, 9):
        print(board[x], end = '  ')
    print("")
    for x in range(9, 81):
        print(board[x], end = '  ')
        if x % 9 == 8:
            print("")

# Returns all positions in the row of the provided position
def get_row_from_position(position):
    row_start = position - position % 9
    return range(row_start, row_start + 9)

# Returns all positions in the column of the provided position
def get_column_from_position(position):
    return list(map(lambda x: x * 9 + position % 9, range(0, 9)))

# Returns square id of the provided position
def get_square_id_from_position(position):
    return (position // 27) * 3 + (position % 9) // 3

fill_board(1, 0, [0] * 81)
print(num_solutions)


# SQUARES:
# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]

# 0  1  2  3  4  5  6  7  8
# 9  10 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24 25 26
