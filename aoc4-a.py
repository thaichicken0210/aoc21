input = []
with open("aoc21.input4.boards.txt") as f:
  input = [line.strip() for line in f.readlines()]
draw1 = []
with open("aoc21.input4.draw.txt") as g:
  draw1 = g.readlines()[0]
draw2 = draw1.split(',')
draw = [int(t) for t in draw2]

# make each board into a list of (in this case) 5 rows of 5 integers
# make a list of board positions that are win states
# use the draw numbers to find which board reaches a win first
  # for the first 5 numbers drawn, find out if any board wins
  # if not, add the next number drawn, and check again
  # etc.
# ???????
# profit

# define some stuff
boards = []
n = int((len(input) + 1) / 6) # the number of bingo boards, since there's no empty line at the end of the last board

# make list of boards
for z in range(0,n):
  boards.append([])
  a = z * 6
  b = a + 1
  c = a + 2
  d = a + 3
  e = a + 4
  boards[z] = [input[a].split(), input[b].split(), input[c].split(), input[d].split(), input[e].split()]

# make boards into lists of integers instead of strings
for board in range(len(boards)):
  for row in range((len(boards[board]))):
    for column in range(len(boards[board][row])):
      boards[board][row][column] = int(boards[board][row][column])

def wincheck(board, draw):
  # checks each row and column of a given board to see whether all elements of that row/column have been drawn
  win = False # assumes a row or column will not win

  for row in board:
    if sum(1 for x in row if x in draw) == 5:
      win = True # shows that it won
  
  for colIx in range(len(board[0])):
    col = [row[colIx] for row in board]
    if sum(1 for w in col if w in draw) == 5:
      win = True # shows that it won

  return win # returns true/false with regards to winning

# print(wincheck(boards[0],draw[0:5]))

# find which board wins first and on what draw it wins
m = len(boards[0]) # number of rows/columns of a square board
q = len(draw) # number of turns taken in the game
winner = None # if no one wins, then the returned winner number is -1
winturn = None # if no one wins, then the returned win turn is -3

for turn in range(m,q):
  for boardIx in range(0,n):
    if wincheck(boards[boardIx], draw[0:turn]):
      winner = boardIx
      winturn = turn
      # print("inner winner:", winner)
      # print("inner winturn:", winturn)
      break
  if winner != None:
    break

print("first winner:", winner)
print("first winturn:", winturn)

def scorecheck(board, draw):
  # calculates the score of a board at the end of a game
  # "draw" as passed into this function should be limited to the numbers actually drawn during a game
  score = 0

  for row in board:
    score += sum(x for x in row if x not in draw)

  return score * draw[-1] # return the score of the board

print(scorecheck(boards[winner], draw[0:winturn]))




### part 2

# when a board wins, append it to a new list
# when the new list is the same length as the original list, scorecheck newlist[-1]

# define the new list
wonboards = []
boards2 = boards[:] # copy the original list so that i can clear boards out of it as i go, and still maintain the original list
n2 = len(boards2)
m = len(boards[0]) # number of rows/columns of a square board
q = len(draw) # number of turns taken in the game

# when a new board wins, append it to wonboards and delete it from boards2
for turn_ in range(m,q):
  for boardIx_ in range(0,n2):
    if wincheck(boards2[boardIx_], draw[0:turn_]):
      wonboards.append(boards2[boardIx_])
      del boards2[boardIx_]
      n2 = n2-1

print(len(wonboards))
print(len(boards2))