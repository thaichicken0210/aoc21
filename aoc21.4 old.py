input = []
with open("aoc21.sample4.boards.txt") as f:
  input = [line.strip() for line in f.readlines()]

# make a list of lists, where each sublist contains rows of boards
  # so boards[0] = [[row 1], [row 2], [row3], [row4], [row5]]
    # not sure if each row needs to be the string it currently is or a list of integers
    # or maybe it doesn't matter
# append to boards[i] for i in range (0, len(boards)) items that are lists of the fist item in each row
  # i.e. turn columns into rows
  # this means i do need lists of integers, or at least lists of single-number strings, instead of five-number strings
# ???????
# profit

# define some stuff
boards = []
n = int((len(input) + 1) / 6) # the number of bingo boards, since there's no empty line at the end of the last board

# make the first list of lists
for z in range(0,n):
  boards.append([])
  a = z * 6
  b = a + 1
  c = a + 2
  d = a + 3
  e = a + 4
  boards[z] = [input[a], input[b], input[c], input[d], input[e]]
print(boards)