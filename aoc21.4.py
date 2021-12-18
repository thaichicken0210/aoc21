input = []
with open("aoc21.sample4.boards.txt") as f:
  input = [line.strip() for line in f.readlines()]

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
q = 5 # number of rows/columns of a square board

for z in range(0,n):
  boards.append([])
  a = z * 6
  b = a + 1
  c = a + 2
  d = a + 3
  e = a + 4
  boards[z] = [input[a], input[b], input[c], input[d], input[e]]

[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
[10, 11, 12, 13, 14]
[15, 16, 17, 18, 19]
[20, 21, 22, 23, 24]
[0, 5, 10, 15, 20]
[1, 6, ]

