import random
from random import choice

blank_board = '''
+================================================+
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
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

speckled_board = '''
+================================================+
|................................................|
|................................................|
|................................................|
|................................................|
|......#.........................................|
|................................................|
|......................................#.........|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|................................................|
|..................#.............................|
|................................................|
|................................................|
|................................................|
|................................................|
+================================================+
'''.strip()

seeded_board = '''
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
    ".#.#",
    ".#.#",
    ".#.#",
    ".#.#",
    "..##",
    "..##",
    "..##",
    "..##",
    "..##",
    #".###"
  ],
  ".#..": [
    ".#.#",
    ".#.#",
    ".#.#",
    ".#.#",
    ".#.#",
    "##..",
    "##..",
    "##..",
    "##..",
    "##..",
    #"##.#"
  ],
  "#...": [
    "##..",
    "##..",
    "##..",
    "##..",
    "##..",
    "#.#.",
    "#.#.",
    "#.#.",
    "#.#.",
    "#.#.",
    #"###."
  ],
  "..#.": [
    "#.#.",
    "#.#.",
    "#.#.",
    "#.#.",
    "#.#.",
    "..##",
    "..##",
    "..##",
    "..##",
    "..##",
    #"#.##"
  ],
  "##..": [
    "##..",
    "##..",
    "##..",
    "##..",
    "##..",
    "##..",
    #"###.",
    #"##.#"
  ],
  "..##": [
    "..##",
    "..##",
    "..##",
    "..##",
    "..##",
    "..##",
    #"#.##",
    #".###"
  ],
  "#.#.": [
    "#.#.",
    "#.#.",
    "#.#.",
    "#.#.",
    "#.#.",
    "#.#.",
    #"###.",
    #"#.##"
  ],
  ".#.#": [
    ".#.#",
    ".#.#",
    ".#.#",
    ".#.#",
    ".#.#",
    ".#.#",
    #"#.##",
    #"###."
  ],
  "###.": [
    #"#.#."
    "###."
  ],
  "#.##": [
    #"#.#."
    "#.##"
  ],
  "####": [
    "..##"
    "##.."
    ".##."
    "#.#."
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
      step_size = 2
      top = new_cells[irow][icol] + new_cells[irow][icol + 1]
      bot = new_cells[irow + 1][icol] + new_cells[irow + 1][icol + 1]
      unit = top + bot
      changed = replace_cells(old_cells, new_cells, irow, icol, unit)
      if not changed:
        step_size = 1

      icol += step_size
    icol = 1
    irow += step_size
  return cells_to_board(new_cells)

def replace_cells(old_cells, new_cells, row, col, unit):
  new_unit = unit

  if unit in rules:
    new_unit = choice(rules[unit])

  if unit != new_unit:
    new_cells[row][col] = new_unit[0]
    new_cells[row][col + 1] = new_unit[1]
    new_cells[row + 1][col] = new_unit[2]
    new_cells[row + 1][col + 1] = new_unit[3]

  return unit != new_unit

def board_to_cells(board):
  cells = [list(row.strip()) for row in board.split("\n")]
  return cells

def cells_to_board(cells):
  cells = ["".join(cell) for cell in cells]
  board = "\n".join(cells)
  return board

board = speckled_board
print(board)
print()

again = True
while again:
  board = walk_board(board)
  print(board)
  print()

  again = not bool(input("[n] to quit. [enter] to continue.]"))
