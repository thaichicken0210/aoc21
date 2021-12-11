list = []
with open("aoc21.input1.txt") as f:
    list = [line.strip() for line in f.readlines()]
print(list[0:9])