import random

b = [["-", "-", "-"],
     ["-", "-", "-"], 
     ["-", "-", "-"]]
n = 0

def board(n, b, player_type):
    if n != 0:
        if n >= 1 and n <= 3 and player_type == "p":
            b[0][n-1] = "x"
        elif n >= 4 and n <= 6 and player_type == "p":
            b[1][n-4] = "x"
        elif n >= 7 and n <= 9 and player_type == "p":
            b[2][n-7] = "x"
        elif n >= 1 and n <= 3 and player_type == "c":
            b[0][n-1] = "o"
        elif n >= 4 and n <= 6 and player_type == "c":
            b[1][n-4] = "o"
        elif n >= 7 and n <= 9 and player_type == "c":
            b[2][n-7] = "o"
    print("\n")
    for row in b:
        for spot in row:
            print(spot, end=" ")
        print()

def check_if_available(n, b):
    if n <= 3:
        if b[0][n-1] != "-": return True
    elif n <= 6:
        if b[1][n-4] != "-": return True
    else:
        if b[2][n-7] != "-": return True

def check_win():
    if b[0][0] == b[0][1] == b[0][2] != "-":
        return True
    elif b[1][0] == b[1][1] == b[1][2] != "-":
        return True
    elif b[2][0] == b[2][1] == b[2][2] != "-":
        return True
    elif b[0][0] == b[1][0] == b[2][0] != "-":
        return True
    elif b[0][1] == b[1][1] == b[2][1] != "-":
        return True
    elif b[0][2] == b[1][2] == b[2][2] != "-":
        return True
    elif b[0][0] == b[1][1] == b[2][2] != "-":
        return True
    elif b[0][2] == b[1][1] == b[2][0] != "-":
        return True
    else:
        return False

def playGame():
    game_over = "no"
    board(0, b, " ")
    count = 0
    print("Player: 'X'; Computer: 'O'")
    
    while game_over == "no":

        if count % 2 == 0:
            each_input = input("\nEnter position from 1 to 9 or 'q' to quit: ")
            player_type = "p"
        else:
            each_input = str(random.randint(1, 10))
            player_type = "c"
        
        if each_input.isnumeric():
            if int(each_input) < 1 or int(each_input) > 9:
                if player_type == "p":
                    print("Number out of bounds!!")
                continue
            else:
                if check_if_available(int(each_input), b):
                    if player_type == "p":
                        print("Position not vacant!!\n")
                    continue
                else:
                    count += 1
                    board(int(each_input), b, player_type)
                    if count == 9:
                        print("\nGame drawn!!! Thanks for Playing!!")
                        game_over = "yes"
        else:
            if each_input.lower() == "q":
                print("\nThanks for Playing!!\n")
                game_over = "yes"
            else:
                print("\nInvalid Input!!")
                continue

        if check_win():
            if player_type == "c":
                print("\n**Computer Wins**\n")
                game_over = "yes"
            else:
                print("\n**Player Wins**\n")
                game_over = "yes"

playGame()
