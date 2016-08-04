from random import choice

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

rules = {
  "....": [
      "...."
  ],
  "...#": [
    ".#.#",
    "..##",
    ".###"
  ],
  ".#..": [
    ".#.#",
    "##..",
    "##.#"
  ],
  "#...": [
    "##..",
    "#.#.",
    "###."
  ],
  "..#.": [
    "#.#.",
    "..##",
    "#.##"
  ],
  "##..": [
    "##..",
    "###.",
    "##.#"
  ],
  "..##": [
    "..##",
    "#.##",
    ".###"
  ],
  "#.#.": [
    "#.#.",
    "###.",
    "#.##"
  ],
  "#.#.": [
    "#.#.",
    "#.##",
    "###."
  ],
  "###.": [
    "###."
  ],
  "#.##": [
    "#.##"
  ],
  "####": [
    "####"
  ]
}

doc_rules = '''

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

def walk_board(board):
  irow = 0
  icol = 0

  old_cells = board_to_cells(board)
  new_cells = board_to_cells(board)

  rows = len(old_cells)
  cols = len(old_cells[0])

  while irow < rows - 1:
    while icol < cols - 1:
      top = old_cells[irow][icol] + old_cells[irow][icol + 1]
      bot = old_cells[irow + 1][icol] + old_cells[irow + 1][icol + 1]
      unit = top + bot
      replace_cells(old_cells, new_cells, irow, icol, unit)

      icol += 1
    icol = 1
    irow += 1
  return cells_to_board(new_cells)

def replace_cells(old_cells, new_cells, row, col, unit):
  new_unit = unit

  if unit in rules:
    print(unit, "in rules")
    new_unit = choice(rules[unit])
  #if unit == ".#..":
  #  new_unit = ".#.#"

  if unit != new_unit:
    print("changed")
    new_cells[row][col] = new_unit[0]
    new_cells[row][col + 1] = new_unit[1]
    new_cells[row + 1][col] = new_unit[2]
    new_cells[row + 1][col + 1] = new_unit[3]
    print(old_cells[row][col], new_unit[0])
    print(old_cells[row][col + 1], new_unit[1])
    print(old_cells[row + 1][col], new_unit[2])
    print(old_cells[row + 1][col + 1], new_unit[3])

def board_to_cells(board):
  cells = [list(row.strip()) for row in board.split("\n")]
  return cells

def cells_to_board(cells):
  cells = ["".join(cell) for cell in cells]
  board = "\n".join(cells)
  return board

print(board)
print()

again = True
while again:
  board = walk_board(board)
  print(board)
  print()

  again = not bool(input("[n] to quit. [enter] to continue.]"))
