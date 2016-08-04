board = '''
+================================================+
|................................................|
|................................................|
|................................................|
|................................................|
|................#...............................|
|................#...............................|
|................#...............................|
|................#######.........................|
|......................#.........................|
|......................#.........................|
|......................#.........................|
|......................#.........................|
|......................#.........................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
+================================================+
'''.strip()

print(board)

snake_eye = '''

 #

'''

center_up = '''
 #
 #

'''

center_left = '''
 
##

'''

center_right = '''
 
 ##

'''

center_down = '''
 
 #
 #
'''

rules = '''

.. ..
.. ..

.. .# .. .#
.# .# ## ##

.# .# ## ##
.. .# .. .#

#. ## #. ##
.. .. #. #.

.. #. .. #.
#. #. ## ##

## ## ## ##
.. .. #. .#

.. .. #. .#
## ## ## ##

#. #. ## #.
#. #. #. ##

#. #. #. ##
#. #. ## #.

## ##
#. #.

#. #.
## ##

## ##
## ##

'''

def walk_cells(cells):
  irow = 0
  icol = 0

  while irow < rows - 1:
    while icol < cols - 1:
      top = cells[irow][icol] + cells[irow][icol + 1]
      bot = cells[irow + 1][icol] + cells[irow + 1][icol + 1]
      unit = top + bot
      replace_cells(cells, irow, icol, unit)

      icol += 1
    icol = 1
    irow += 1
  return cells

def replace_cells(cells, row, col, unit):
  new_unit = unit

  #if unit == "....":
  #  new_unit = "..#."

  if unit == ".#..":
    new_unit = ".#.#"

  if unit != new_unit:
    print("changed")
    cells[row][col] = new_unit[0]
    cells[row][col + 1] = new_unit[1]
    cells[row + 1][col] = new_unit[2]
    cells[row + 1][col + 1] = new_unit[3]
    print(cells[row][col], new_unit[0])
    print(cells[row][col + 1], new_unit[1])
    print(cells[row + 1][col], new_unit[2])
    print(cells[row + 1][col + 1], new_unit[3])

def board_to_cells(board):
  cells = [list(row.strip()) for row in board.split("\n")]
  return cells

def cells_to_board(cells):
  cells = ["".join(cell) for cell in cells]
  board = "\n".join(cells)
  return board

cells = board_to_cells(board)
rows = len(cells)
cols = len(cells[0])

print("rows:", rows)
print("cols:", cols)

walk_cells(cells)
board = cells_to_board(cells)
print(board)
