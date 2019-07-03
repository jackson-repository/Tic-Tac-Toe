def set_players():
    # Who wants to be X , the other one is O
    Player1 = input("Player 1: Do you want to be X or O ?").upper()
    if Player1 == "X":
        print("Player 1 will go first")
    elif Player1 == "O":
        print("Player 2 will go first")
    else:
        print("Please Enter X or O")
        Player1 = input("Player 1: Do you want to be X or O ?").upper()
    if Player1 == "X":Player2 = "O"
    elif Player1 == "O":Player2 = "X"
    players = {Player1 : "Player 1",Player2 : "Player 2"}
    return players

def play(player, players):
    player_position = int(input(f"{players[player]} Choose your next position (1-9)")) # gets player choose
    while player_position not in range(1,10): # if it is not in range of 1 to 9, it keeps running and running
        print("Please Enter number between 1 and 9")
        player_position = int(input(f"{players[player]} Choose your next position (1-9)"))
    while player_position == '': # if it (the position) is empty, it keeps running and running
        print("Please Enter number between 1 and 9. Print something.")
        player_position = int(input(f"{players[player]} Choose your next position (1-9)"))
    while True:
        if maze[player_position - 1] in ["X", "O"]:
            print("Chosen position is already reserved and full. Choose another one")
            player_position = int(input(f"{players[player]} Choose your next position (1-9)"))
            while player_position not in range(1,10):
                print("Please Enter number between 1 and 9")
                player_position = int(input(f"{players[player]} Choose your next position (1-9)"))
        else:
            maze[player_position - 1] = player
            break


def check(maze, players):
    # checks if anyone won
    if maze[0] == maze[1] == maze[2] and maze[0] != ' ':
        return [True, f'Congratulations! {players[maze[0]]} won this game.']
    elif maze[3] == maze[4] == maze[5] and maze[3] != ' ':
        return [True, f'Congratulations! {players[maze[3]]} won this game.']
    elif maze[6] == maze[7] == maze[8] and maze[6] != ' ':
        return [True, f'Congratulations! {players[maze[6]]} won this game.']
    elif maze[0] == maze[3] == maze[6] and maze[0] != ' ':
        return [True, f'Congratulations! {players[maze[0]]} won this game.']
    elif maze[1] == maze[4] == maze[7] and maze[1] != ' ':
        return [True, f'Congratulations! {players[maze[1]]} won this game.']
    elif maze[2] == maze[5] == maze[8] and maze[2] != ' ':
        return [True, f'Congratulations! {players[maze[2]]} won this game.']
    elif maze[0] == maze[4] == maze[8] and maze[0] != ' ':
        return [True, f'Congratulations! {players[maze[0]]} won this game.']
    elif maze[2] == maze[4] == maze[6] and maze[2] != ' ':
        return [True, f'Congratulations! {players[maze[2]]} won this game.']
    else:
        return [False]        

def printer(maze):
    # Prints changes
    print(" {0[6]} | {0[7]} | {0[8]} ".format(maze))
    print("-----------")
    print(" {0[3]} | {0[4]} | {0[5]} ".format(maze))
    print("-----------")
    print(" {0[0]} | {0[1]} | {0[2]} ".format(maze))

def check_full(maze):
    # checks if maze (the board i don't know why i chose this name) if full
    for item in maze:
        if not item in ["X", "O"]:
            return False
    return True

def replay():
    choice = input("Do you wanna play again? Yes or No?").lower()
    return choice == 'yes'

def restart():
    global maze
    maze = [' '] * 9
    global won
    won = False

restart()

while True:
    players = set_players()
    while not won:
        printer(maze)
        play("X", players)
        check_win = check(maze, players)
        if check_win[0]:
            print(check_win[1])
            printer(maze)
            break
        if check_full(maze):
            print("Nobody won!")
            printer(maze)
            break
        printer(maze)
        play("O", players)
        check(maze, players)
        check_win = check(maze, players)
        if check_win[0]:
            print(check_win[1])
            printer(maze)
            break
        if check_full(maze):
            print("Nobody won!")
            printer(maze)
            break
    if replay():
        restart()
    else:
        break
