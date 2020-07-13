# write your code here
import random

rows = list()
columns = []
diags = []
game_board = []
x_winner = "XXX"
o_winner = "OOO"
x_wins = 0
o_wins = 0
x_s = 0
o_s = 0
spaces = 0
row_1 = []
row_2 = []
row_3 = []
init_matrix = "_________"
current_state = ""
current_player = "X"
game_loop = True
menu_loop = True
ai_loop = True
move_loop = True
new_x = 0
new_y = 0
text_in = ""


num_matrix = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]


def create_init_state():

    global init_matrix
    global row_1
    global row_2
    global row_3
    global current_player

    # init_matrix = input("Enter cells: ")
    row_1 = [init_matrix[0], init_matrix[1], init_matrix[2]]
    row_2 = [init_matrix[3], init_matrix[4], init_matrix[5]]
    row_3 = [init_matrix[6], init_matrix[7], init_matrix[8]]


def create_rows():
    global row_1
    global row_2
    global row_3
    global rows
    rows.append(row_1)
    rows.append(row_2)
    rows.append(row_3)


def print_gameboard():
    global rows

    print("---------")
    print(f"| {rows[0][0]} {rows[0][1]} {rows[0][2]} |")
    print(f"| {rows[1][0]} {rows[1][1]} {rows[1][2]} |")
    print(f"| {rows[2][0]} {rows[2][1]} {rows[2][2]} |")
    print("---------")


def create_columns():
    global rows
    global columns
    columns = [
        [rows[0][0], rows[1][0], rows[2][0]],
        [rows[0][1], rows[1][1], rows[2][1]],
        [rows[0][2], rows[1][2], rows[2][2]]
    ]


def create_diags():
    global rows
    global diags
    diags = [[rows[0][0], rows[1][1], rows[2][2]],
             [rows[2][0], rows[1][1], rows[0][2]]]


def create_gameboard():
    global game_board
    global rows
    global columns
    global diags
    game_board = [rows] + [columns] + [diags]


def count_winners():
    global row_1
    global row_2
    global row_3
    global x_winner
    global o_winner
    global x_wins
    global o_wins
    global spaces
    global x_s
    global o_s

    x_wins = "".join(row_1).count(x_winner) + "".join(row_2).count(x_winner) \
             + "".join(row_3).count(x_winner) + "".join(columns[0]).count(x_winner) \
             + "".join(columns[1]).count(x_winner) + "".join(columns[2]).count(x_winner) \
             + "".join(diags[0]).count(x_winner) + "".join(diags[1]).count(x_winner)

    o_wins = "".join(row_1).count(o_winner) + "".join(row_2).count(o_winner) \
             + "".join(row_3).count(o_winner) + "".join(columns[0]).count(o_winner) \
             + "".join(columns[1]).count(o_winner) + "".join(columns[2]).count(o_winner) \
             + "".join(diags[0]).count(o_winner) + "".join(diags[1]).count(o_winner)

    spaces = row_1.count("_") + row_2.count("_") + row_3.count("_")
    x_s = row_1.count("X") + row_2.count("X") + row_3.count("X")
    o_s = row_1.count("O") + row_2.count("O") + row_3.count("O")


def check_game_state():
    global x_wins
    global o_wins
    global spaces
    global x_s
    global o_s
    global current_state

    if x_wins == 1 and o_wins == 0:
        current_state = "X wins"

    elif o_wins == 1 and x_wins == 0:
        current_state = "O wins"

    elif spaces > 0 and o_wins == 0 and x_wins == 0:
        current_state = "Game not finished"

    elif x_wins > 0 and o_wins > 0:
        current_state = "Impossible"

    elif (x_s > o_s + 1) or (o_s > x_s + 1):
        current_state = "Impossible"

    elif x_wins == 0 and o_wins == 0 and spaces == 0:
        current_state = "Draw"

    return current_state

def is_two_digits(some_text):
    if some_text.replace(" ", "").isdigit() and len(some_text.replace(" ", "")) == 2:
        return True
    else:
        return False

def is_in_coords(some_text):
    if 1 <= int(some_text.replace(" ", "")[0]) <= 3 \
            and 1 <= int(some_text.replace(" ", "")[1]) <= 3:
        return True
    else:
        return False


def initial_setup():
    create_init_state()
    create_rows()


def setup_game():
    create_columns()
    create_diags()
    create_gameboard()


def get_coords(text):
    global new_x
    global new_y
    global num_matrix
    x, y = text.split()
    x = int(x)
    y = int(y)
    cell = (x - 1) + (9 - (3 * y))
    new_xy = num_matrix[cell]
    new_x = int(new_xy[0])
    new_y = int(new_xy[1])


def end_game():
    global menu_loop
    global game_loop
    if check_game_state() in ("X wins", "O wins", "Impossible", "Draw"):
        print(current_state)
        game_loop = False
        menu_loop = False


def switch_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def get_user_move():
    global text_in
    while True:
        text_in = input("Enter the coordinates: ")

        if not is_two_digits(text_in):
            print("You should enter numbers!")

        elif not is_in_coords(text_in):
            print("Coordinates should be from 1 to 3!")

        elif is_two_digits(text_in) and is_in_coords(text_in):
            get_coords(text_in)
            break


def play_move():
    global new_x
    global new_y
    global move_loop
    global game_loop
    global menu_loop

    if rows[new_x][new_y] != "_":
        print("This cell is occupied! Choose another one!")
    elif rows[new_x][new_y] == "_":
        rows[new_x][new_y] = current_player
        setup_game()
        print_gameboard()
        count_winners()
        end_game()
        move_loop = False


def generate_ai_move():
    global num_matrix
    global new_x
    global new_y
    print('Making move level "easy"')
    ox = random.randint(1, 3)
    oy = random.randint(1, 3)
    cello = (ox - 1) + (9 - (3 * oy))
    new_xy = num_matrix[cello]
    new_x = int(new_xy[0])
    new_y = int(new_xy[1])


while menu_loop:
    initial_setup()
    setup_game()

    print("Input command:")
    commands = input().split()
    # print_gameboard()
    if commands[0] == "exit" and len(commands) == 1:
        menu_loop = False
    elif commands[0] == "start" and len(commands) != 3:
        print("Bad parameters")
    elif commands[0] != "start" and commands[0] != "exit":
        print("Bad parameters")
    elif commands[0] == "start" and len(commands) == 3:
        if commands[1] == "user" and commands[2] == "easy":
            # simple game starting with user first
            print_gameboard()
            while game_loop:
                while move_loop:
                    get_user_move()
                    play_move()
                    if not move_loop:
                        switch_player()
                        move_loop = True
                        break
                if not game_loop:
                    break

                while move_loop:
                    generate_ai_move()
                    play_move()
                    if not move_loop:
                        switch_player()
                        move_loop = True
                        break
                if not game_loop:
                    break

        elif commands[1] == "user" and commands[2] == "user":
            # simple game with two users
            print_gameboard()
            while game_loop:
                while move_loop:
                    get_user_move()
                    play_move()
                    if not move_loop:
                        switch_player()
                        break
                if not game_loop:
                    break
                move_loop = True

                while move_loop:
                    get_user_move()
                    play_move()
                    if not move_loop:
                        switch_player()
                        break
                move_loop = True
                if not game_loop:
                    break

        elif commands[1] == "easy" and commands[2] == "user":
            # simple game starting with AI first
            print_gameboard()
            while game_loop:
                while move_loop:
                    generate_ai_move()
                    play_move()
                    if not move_loop:
                        switch_player()
                        move_loop = True
                        break
                if not game_loop:
                    break

                while move_loop:
                    get_user_move()
                    play_move()
                    if not move_loop:
                        switch_player()
                        move_loop = True
                        break
                if not game_loop:
                    break
        elif commands[1] == "easy" and commands[2] == "easy":
            # easy game with two AI's
            print_gameboard()
            while game_loop:
                while move_loop:
                    generate_ai_move()
                    play_move()
                    if not move_loop:
                        switch_player()
                        move_loop = True
                        break
                if not game_loop:
                    break

                while move_loop:
                    generate_ai_move()
                    play_move()
                    if not move_loop:
                        switch_player()
                        move_loop = True
                        break
                if not game_loop:
                    break
