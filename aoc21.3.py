diag = []
with open("aoc21.input3.txt") as f:
    diag = [line.strip() for line in f.readlines()]

# extract each place value from each item and collect them separately
# count the number of 1 vs 0 for reach such collection
    # if that number is greater than half of len(diag), register the respective 1 or 0 for that place
    # concatenate into new terms
# convert new terms into binary integers
    # convert binary into decimal integers
# multiply decimal integers

# determine length of diagnostic strings
n = len(diag[0])
# print(n)

### thought process archived for posterity
    ### this version sorts it by input string
    # for i in range(0, len(diag)):
    #     for j in range(0,n):
    #         print(diag[i])
    #         print(diag[i][j])

    ### this version sorts it by place value

    ### but they both are unhelpful because they are interrupted by `print(diag[i])` on every line, but otherwise the printout is unreadable to a human SO we're gonna slow this down a little 

    ### this version sorts it readably by place value, with added "xxxxx" (of length n, but regrettably typed manually atm bc i don't know how to make a string of x's of length n) for ease of seeing which place you're in
    ### eventually this will not be needed to print, but it's here while i'm working
    # for i in range(0, len(diag)):
    #     print(diag[i])
    # print("xxxxx")
    # for i in range(0, len(diag)):
    #     print(diag[i][0])
    # print("xxxxx")
    # for i in range(0, len(diag)):
    #     print(" "+diag[i][1])
    # print("xxxxx")
    # for i in range(0, len(diag)):
    #     print("  "+diag[i][2])
    # print("xxxxx")
    # for i in range(0, len(diag)):
    #     print("   "+diag[i][3])
    # print("xxxxx")
    # for i in range(0, len(diag)):
    # print("    "+diag[i][4])

# name some more lists
gamma = []
epsilon = []
pos = [[], []]
int_pos = [[], []]

### brute force version of loop below
    # # count the number of 1 vs 0 in position 0 (leftmost)
    # pos0 = []
    # for i in range(0, len(diag)):
    #     # int(diag[i][0])       # i want this to be useful, but it doesn't actually achieve anything
    #     pos0.append(diag[i][0])
    # int_pos0 = [int(item) for item in pos0]
    # if sum(int_pos0) > len(diag)/2:
    #     # print(1)
    #     gamma.append(1)
    #     epsilon.append(0)
    # else:
    #     # print(0)
    #     gamma.append(0)
    #     epsilon.append(1)

    # # count the number of 1 vs 0 in position 1 (second left)
    # pos1 = []
    # for i in range(0, len(diag)):
    #     # int(diag[i][0])       # i want this to be useful, but it doesn't actually achieve anything
    #     pos1.append(diag[i][1])
    # int_pos1 = [int(item) for item in pos1]
    # if sum(int_pos1) > len(diag)/2:
    #     # print(1)
    #     gamma.append(1)
    #     epsilon.append(0)
    # else:
    #     # print(0)
    #     gamma.append(0)
    #     epsilon.append(1)

    # # count the number of 1 vs 0 in position 2 (third left)
    # pos2 = []
    # for i in range(0, len(diag)):
    #     # int(diag[i][0])       # i want this to be useful, but it doesn't actually achieve anything
    #     pos2.append(diag[i][2])
    # int_pos2 = [int(item) for item in pos2]
    # if sum(int_pos2) > len(diag)/2:
    #     # print(1)
    #     gamma.append(1)
    #     epsilon.append(0)
    # else:
    #     # print(0)
    #     gamma.append(0)
    #     epsilon.append(1)

    #     # count the number of 1 vs 0 in position 3 (fourth left)
    # pos3 = []
    # for i in range(0, len(diag)):
    #     # int(diag[i][0])       # i want this to be useful, but it doesn't actually achieve anything
    #     pos3.append(diag[i][3])
    # int_pos3 = [int(item) for item in pos3]
    # if sum(int_pos3) > len(diag)/2:
    #     # print(1)
    #     gamma.append(1)
    #     epsilon.append(0)
    # else:
    #     # print(0)
    #     gamma.append(0)
    #     epsilon.append(1)

    # # count the number of 1 vs 0 in position 4 (fifth left)
    # pos4 = []
    # for i in range(0, len(diag)):
    #     # int(diag[i][0])       # i want this to be useful, but it doesn't actually achieve anything
    #     pos4.append(diag[i][4])
    # int_pos4 = [int(item) for item in pos4]
    # if sum(int_pos4) > len(diag)/2:
    #     # print(1)
    #     gamma.append(1)
    #     epsilon.append(0)
    # else:
    #     # print(0)
    #     gamma.append(0)
    #     epsilon.append(1)

### take the just-previous commented section and loop it for any input data of any length
for k in range(0,n):
    for i in range(0, len(diag)):
        # int(diag[i][k])       # i want this to be useful, but it doesn't actually achieve anything
        pos.append([])
        pos[k].append(diag[i][k])
    int_pos.append([])
    int_pos[k] = [int(item) for item in pos[k]]
    if sum(int_pos[k]) > len(diag)/2:
        # print(1)
        gamma.append(1)
        epsilon.append(0)
    else:
        # print(0)
        gamma.append(0)
        epsilon.append(1)

# concatenate
ans_gamma = "".join(map(str,gamma))
print("gamma = "+ ans_gamma)
ans_epsilon = "".join(map(str,epsilon))
print("epsilon = " + ans_epsilon)
print("")
dec_gamma = int(ans_gamma, 2)
dec_epsilon = int(ans_epsilon, 2)
print("gamma =")
print(dec_gamma)
print("epsilon =")
print(dec_epsilon)
print("final answer")
print(dec_gamma * dec_epsilon)
print("========")


### PART TWO
# run part of the loop from part 1 to determine which bit is more common
    # for elements of diag that start with that more-common bit, create sublist for O2 (or those that start with 1, for even splits)
    # for elements of diag that do not start with the O2 bit, create a sublist for CO2
# loop that shit til the sub-sub-sub-etc-list is down to one item
    # find out how to know when that happens

### previous thought process for posterity
    # name some more new lists
    # pos2 = []
    # int_pos2 = []

    # # i think i need an initial one to get items out of the initial diagnostic list, then i can make a loop with sublists
    # for k in range(0, 1):
    #     for i in range(0, len(diag)):
    #         pos2.append([])
    #         pos2[k].append(diag[i][k])
    #         # pos2.append(diag[i][k])
    #     int_pos2.append([])
    #     int_pos2[k] = [int(item) for item in pos2[k]]
    #     # int_pos2 = [int(item) for item in pos2]
    #     if sum(int_pos2[k]) >= len(diag)/2:
    #     # if sum(int_pos2) >= len(diag)/2:
    #     # if 1 is the more common bit in this position
    #         # then for items that start with 1, add them to O2[k]
    #         # and for items that start with 0, add them to CO2[k]
    #         O2 = ([x for x in diag if x.startswith('1')])
    #         CO2 = ([y for y in diag if y.startswith('0')])
    #     if sum(int_pos2[k]) < len(diag)/2:   # idk why `else` didn't work here
    #         O2 = ([y for y in diag if y.startswith('0')])
    #         CO2 = ([x for x in diag if x.startswith('1')])

    # print("")
    # print(pos2)
    # print(int_pos2)

    # print("O2 = ")
    # print(O2)
    # print("CO2 = ")
    # print(CO2)

# name yet more new lists
O2 = diag
CO2 = diag

# loop for O2
for k in range (0,n):
    one = [item for item in O2 if item[k]=="1"]
    zero = [item for item in O2 if item[k]=="0"]
    # print("")
    # print("one:", len(one),"|", one)
    # print("zero:", len(zero), "|", zero)
    if zero == [] or one == []:
        break
    if len(one) >= len(zero):
        O2 = one
    if len(one) < len(zero):
        O2 = zero

# loop for CO2
for k in range (0,n):
    one = [item for item in CO2 if item[k]=="1"]
    zero = [item for item in CO2 if item[k]=="0"]
    # print("")
    # print("one:", len(one),"|", one)
    # print("zero:", len(zero), "|", zero)
    if zero == [] or one == []:
        break
    if len(one) < len(zero):
        CO2 = one
    if len(one) >= len(zero):
        CO2 = zero

#print results
print("")
print("O2:",O2)
dec_O2 = int(O2[0],2)
print(dec_O2)
print("CO2",CO2)
dec_CO2 = int(CO2[0],2)
print(dec_CO2)
print("final answer:", dec_O2 * dec_CO2)