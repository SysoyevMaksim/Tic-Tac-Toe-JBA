import math


def print_field():
    print("---------")
    print("|" + " " + input_[0] + " " + input_[1] + " " + input_[2] + " " + "|")
    print("|" + " " + input_[3] + " " + input_[4] + " " + input_[5] + " " + "|")
    print("|" + " " + input_[6] + " " + input_[7] + " " + input_[8] + " " + "|")
    print("---------")


def test_field():
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


def change_string(string, pos, second_string):
    return string[0: pos] + second_string + string[pos+1: len(string)]


def read_x_and_y():
    global field
    global input_
    x, y = input("Enter the coordinates: ").split()
    if not x.isnumeric() or not y.isnumeric():
        print("You should enter numbers!")
        return read_x_and_y()
    x = int(x)
    y = int(y)
    if not 1 <= x <= 3 or not 1 <= y <= 3:
        print("Coordinates should be from 1 to 3!")
        return read_x_and_y()
    if not field[3 - y][x-1] == "_":
        print("This cell is occupied! Choose another one!")
        return read_x_and_y()
    field[3 - y][x-1] = "X"
    input_ = change_string(input_, x + y + ((2 - y) * 4), "X")


input_ = input("Enter cells: ")
field = [[input_[0], input_[1], input_[2]],
         [input_[3], input_[4], input_[5]],
         [input_[6], input_[7], input_[8]]]
print_field()
read_x_and_y()
print_field()
