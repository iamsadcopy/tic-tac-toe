str_cells = "          "
first_row = list(str_cells[0:3])
second_row = list(str_cells[3:6])
third_row = list(str_cells[6:9])
cells = [first_row, second_row, third_row]
numbers = [str(x) for x in range(10)]

def print_cells():
    print("---------")
    print("| " + cells[0][0] + " " + cells[0][1] + " " + cells[0][2] + " |")
    print("| " + cells[1][0] + " " + cells[1][1] + " " + cells[1][2] + " |")
    print("| " + cells[2][0] + " " + cells[2][1] + " " + cells[2][2] + " |")
    print("---------")

print_cells()

turn = "O"
count = 0
def game():
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    mn = input("Enter the coordinates:")
    mn = mn.split()
    if mn[0] in numbers and mn[1] in numbers:
        if 0 < int(mn[0]) < 4 and 0 < int(mn[0]) < 4:
            if cells[int(mn[0]) - 1][int(mn[1]) - 1] == " ":
                cells[int(mn[0]) - 1][int(mn[1]) - 1] = turn
                global count
                count += 1
                print_cells()
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")

while True:
    game()
    
    if count == 9:
        print("Draw")
        break
    elif cells[0][0] == cells[0][1] == cells[0][2] and cells[0][0] == turn:
        print(turn + " wins")
        break
    elif cells[0][0] == cells[1][1] == cells[2][2] and cells[0][0] == turn:
        print(turn + " wins")
        break
    elif cells[1][0] == cells[1][1] == cells[1][2] and cells[1][0] == turn:
        print(turn + " wins")
        break
    elif cells[2][0] == cells[1][1] == cells[0][2] and cells[2][0] == turn:
        print(turn + " wins")
        break
    elif cells[2][0] == cells[2][1] == cells[2][2] and cells[2][0] == turn:
        print(turn + " wins")
        break
    elif cells[0][1] == cells[1][1] == cells[2][1] and cells[0][1] == turn:
        print(turn + " wins")
        break
    elif cells[0][2] == cells[1][2] == cells[2][2] and cells[0][2] == turn:
        print(turn + " wins")
        break
    elif cells[0][0] == cells[1][0] == cells[2][0] and cells[0][0] == turn:
        print(turn + " wins")
        break
    else:
        continue