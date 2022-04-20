import graphic
import os
import random
import time


def clear():
    """ Clears the console in Pycharm """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def winner(player, row1, row2, row3, nest):
    """ Checks if there is a winner combination """
    #column
    for n in range(len(nest)):
        if player in row1[n] and player in row2[n] and player in row3[n]:
            return f"{player} wins with full column"
    #row
    for item in nest:
        if player in item[0] and player in item[1] and player in item[2]:
            return f"{player} wins with full row"
    #bias
    if player in row1[0] and player in row2[1] and player in row3[2] \
            or player in row1[2] and player in row2[1] and player in row3[0]:
        return f"{player} wins with bias row"


def play_game():
    """ The functionality of the game. Human player versus a randomised computer player. """
    print(graphic.logo)
    # Playing board as a nested list
    row1 = ["⬜️", "⬜️", "⬜️"]
    row2 = ["⬜️", "⬜️", "⬜️"]
    row3 = ["⬜️", "⬜️", "⬜️"]
    full_board = [row1, row2, row3]
    board = f"\n {row1[0]} | {row1[1]} | {row1[2]} \n-----------\n {row2[0]} | {row2[1]} | {row2[2]} \n-----------\n {row3[0]} | {row3[1]} | {row3[2]} \n"
    print(board)

    # Choose which player you want to be - X or O
    player_1 = input("Hi player 1!\nDo you want to be O or X? ").upper()
    if player_1 == "O":
        player_2 = "X"
    else:
        player_2 = "O"
    print(f"Player 1: {player_1} - Player 2: {player_2}")

    game_is_on = True
    while game_is_on:
        # Player 1 turn
        p1_move = input(f"Player 1 where do you wanna put your {player_1}?")
        column = int(p1_move[0])-1
        row = int(p1_move[1])-1
        #If the place is already taken prompt the player.
        if full_board[row][column] == "⬜️":
            full_board[row][column] = player_1
            board = f"\n {row1[0]} | {row1[1]} | {row1[2]} \n-----------\n {row2[0]} | {row2[1]} | {row2[2]} \n-----------\n {row3[0]} | {row3[1]} | {row3[2]} \n"
            clear()
            print(board)
            # Check if player 1 wins. Else player 2 can try.
            if winner(player_1, row1, row2, row3, full_board):
                print(winner(player_1, row1, row2, row3, full_board))
                game_is_on = False
            else:
                # Player 2 turn: Randomised computer player.
                # Note it is only necessary to check for free spots with player 2,because player 1 allways starts and there are 9 spots.
                if "⬜️" in row1 or "⬜️" in row2 or "⬜️" in row3:
                    rand_column = random.randint(0, 2)
                    rand_row = random.randint(0, 2)
                    while full_board[rand_row][rand_column] != "⬜️":
                        rand_column = random.randint(0, 2)
                        rand_row = random.randint(0, 2)
                    full_board[rand_row][rand_column] = player_2
                    board = f"\n {row1[0]} | {row1[1]} | {row1[2]} \n-----------\n {row2[0]} | {row2[1]} | {row2[2]} \n-----------\n {row3[0]} | {row3[1]} | {row3[2]} \n"
                    time.sleep(1)
                    clear()
                    print(board)
                    if winner(player_2, row1, row2, row3, full_board):
                        print(winner(player_2, row1, row2, row3, full_board))
                        game_is_on = False
                else:
                    print("Game ended without a winner")
                    game_is_on = False
        else:
            print("This spot has already been taken, select a free spot")


# As long as the player replies y the game runs again. Old game is cleared.
while input("Do you wanna play? Press Y or N ").upper() == "Y":
    clear()
    play_game()
