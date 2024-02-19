import tictactoe.print_board as pb
import tictactoe.winner as w
import random


def take_input(turn, val_li, x_values, o_values):
    if not turn:
        ip = random.randint(1, 10)
    else:
        ip = int(input())
    while ip < 0 or ip > 10 or ip in val_li:
        print("Please provide valid index: ", "x" if turn else "o", "'s turn: ")
        if not turn:
            ip = random.randint(1, 10)
        else:
            ip = int(input())
    val_li.append(ip)
    if turn:
        x_values.append(ip)
    else:
        o_values.append(ip)
    return ip


def whos_turn(turn, arr, val_li, x_values, o_values):
    if turn:
        user = "X"
    else:
        user = "O"
    print(f"{user}'s turn:", end=" ")
    val = take_input(turn, val_li, x_values, o_values)
    arr[val - 1] = user
    return not turn


def gap(n):
    for i in range(n):
        print()


play = True
while play:
    arr = [" "] * 10
    val_li = list()
    x_values = list()
    o_values = list()
    turn = True
    win = " "
    count = 1

    while count != 10 and win == " ":
        gap(10)
        if count == 1:
            print("Welcome to Soumyadeep's Tic Tac Toe game")
        pb.game_board(arr)
        turn = whos_turn(turn, arr, val_li, x_values, o_values)
        win = w.check_winner(x_values, o_values)
        count += 1
    gap(15)
    pb.game_board(arr)
    if win == "x":
        print("***--------------X is the winner---------------***")
    elif win == "o":
        print("***--------------O is the winner---------------***")
    else:
        print("***--------------  It's a draw  ---------------***")

    print("Do you want to play again? Yes/No")
    play_again = input().lower()
    play = (play_again == "yes")

print("Thankyou for playing :)")
