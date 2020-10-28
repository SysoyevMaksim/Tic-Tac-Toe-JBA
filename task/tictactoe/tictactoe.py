import math

input_ = input("Enter cells: ")
print("---------")
print("|" + " " + input_[0] + " " + input_[1] + " " + input_[2] + " " + "|")
print("|" + " " + input_[3] + " " + input_[4] + " " + input_[5] + " " + "|")
print("|" + " " + input_[6] + " " + input_[7] + " " + input_[8] + " " + "|")
print("---------")
field = [[input_[0], input_[1], input_[2]],
         [input_[3], input_[4], input_[5]],
         [input_[6], input_[7], input_[8]]]
a = field[0][0] == field[0][1] == field[0][2]
b = field[1][0] == field[1][1] == field[1][2]
c = field[2][0] == field[2][1] == field[2][2]
d = field[0][0] == field[1][0] == field[2][0]
e = field[0][1] == field[1][1] == field[2][1]
f = field[0][2] == field[1][2] == field[2][2]
g = field[0][0] == field[1][1] == field[2][2]
h = field[0][2] == field[1][1] == field[2][0]
bools = [a, b, c, d, e, f, g, h]
results = []
for i in range(8):
    if i <= 2:
        match = bools[i]
        variant = field[i][0] == "O"
        results.append(match * variant + match)
    elif i <= 5:
        match = bools[i]
        variant = field[0][i - 3] == "O"
        results.append(match * variant + match)
    else:
        match = bools[i]
        variant = field[1][1] == "O"
        results.append(match * variant + match)
# print(results)
if math.fabs(input_.count("O") - input_.count("X")) >= 2:
    print("Impossible")
elif results.count(1) == 0 and results.count(2) == 0:
    if "_" in input_:
        print("Game not finished")
    else:
        print("Draw")
elif results.count(1) > 0 and results.count(2) > 0:
    print("Impossible")
else:
    if results.count(1) > 0:
        print("X wins")
    else:
        print("O wins")
