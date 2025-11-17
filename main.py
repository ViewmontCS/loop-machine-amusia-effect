import os
from random import randint
from time import sleep

def clear():
  os.system('cls')

score = 100
cost = 5
low_win = 30
mid_win = 60
high_win = 90
diagonal_win = 50

print("Welcome fellow gambler!")
decide = input("What will it be today? Play or Leave? ")

if decide.lower() == "play":
    while score >= 1:
        print("Spin the slots!")
        score -= 5
        for i in range(20):
            top_left = randint(1,9)
            top_middle = randint(1,9)
            top_right = randint(1,9)
            middle_left = randint(1,9)
            middle = randint(1,9)
            middle_right = randint(1,9)
            bottom_left = randint(1,9)
            bottom_middle = randint(1,9)
            bottom_right = randint(1,9)
            clear()
            print(f"|{top_left}|{top_middle}|{top_right}|\n"
                  f"|{middle_left}|{middle}|{middle_right}|\n"
                  f"|{bottom_left}|{bottom_middle}|{bottom_right}|")
            sleep(.1)

        if top_left == 1 and top_middle == 1 and top_right == 1:
            score += low_win
        if top_left == 2 and top_middle == 2 and top_right == 2:
            score += low_win
        if top_left == 3 and top_middle == 3 and top_right == 3:
            score += low_win
        if top_left == 4 and top_middle == 4 and top_right == 4:
            score += mid_win
        if top_left == 5 and top_middle == 5 and top_right == 5:
            score += mid_win
        if top_left == 6 and top_middle == 6 and top_right == 6:
            score += mid_win
        if top_left == 7 and top_middle == 7 and top_right == 7:
            score += high_win
        if top_left == 8 and top_middle == 8 and top_right == 8:
            score += high_win
        if top_left == 9 and top_middle == 9 and top_right == 9:
            score += high_win

        if middle_left == 1 and middle == 1 and middle_right == 1:
            score += low_win
        if middle_left == 2 and middle == 2 and middle_right == 2:
            score += low_win
        if middle_left == 3 and middle == 3 and middle_right == 3:
            score += low_win
        if middle_left == 4 and middle == 4 and middle_right == 4:
            score += mid_win
        if middle_left == 5 and middle == 5 and middle_right == 5:
            score += mid_win
        if middle_left == 6 and middle == 6 and middle_right == 6:
            score += mid_win
        if middle_left == 7 and middle == 7 and middle_right == 7:
            score += high_win
        if middle_left == 8 and middle == 8 and middle_right == 8:
            score += high_win
        if middle_left == 9 and middle == 9 and middle_right == 9:
            score += high_win

        if bottom_left == 1 and bottom_middle == 1 and bottom_right == 1:
            score += low_win
        if bottom_left == 2 and bottom_middle == 2 and bottom_right == 2:
            score += low_win
        if bottom_left == 3 and bottom_middle == 3 and bottom_right == 3:
            score += low_win
        if bottom_left == 4 and bottom_middle == 4 and bottom_right == 4:
            score += mid_win
        if bottom_left == 5 and bottom_middle == 5 and bottom_right == 5:
            score += mid_win
        if bottom_left == 6 and bottom_middle == 6 and bottom_right == 6:
            score += mid_win
        if bottom_left == 7 and bottom_middle == 7 and bottom_right == 7:
            score += high_win
        if bottom_left == 8 and bottom_middle == 8 and bottom_right == 8:
            score += high_win
        if bottom_left == 9 and bottom_middle == 9 and bottom_right == 9:
            score += high_win

        if top_left == 1 and middle == 1 and bottom_right == 1:
            score += diagonal_win
        if top_left == 2 and middle == 2 and bottom_right == 2:
            score += diagonal_win
        if top_left == 3 and middle == 3 and bottom_right == 3:
            score += diagonal_win
        if top_left == 4 and middle == 4 and bottom_right == 4:
            score += diagonal_win
        if top_left == 5 and middle == 5 and bottom_right == 5:
            score += diagonal_win
        if top_left == 6 and middle == 6 and bottom_right == 6:
            score += diagonal_win
        if top_left == 7 and middle == 7 and bottom_right == 7:
            score += diagonal_win
        if top_left == 8 and middle == 8 and bottom_right == 8:
            score += diagonal_win
        if top_left == 9 and middle == 9 and bottom_right == 9:
            score += diagonal_win
            
        if bottom_left == 1 and middle == 1 and top_right == 1:
            score += diagonal_win
        if bottom_left == 2 and middle == 2 and top_right == 2:
            score += diagonal_win
        if bottom_left == 3 and middle == 3 and top_right == 3:
            score += diagonal_win
        if bottom_left == 4 and middle == 4 and top_right == 4:
            score += diagonal_win
        if bottom_left == 5 and middle == 5 and top_right == 5:
            score += diagonal_win
        if bottom_left == 6 and middle == 6 and top_right == 6:
            score += diagonal_win
        if bottom_left == 7 and middle == 7 and top_right == 7:
            score += diagonal_win
        if bottom_left == 8 and middle == 8 and top_right == 8:
            score += diagonal_win
        if bottom_left == 9 and middle == 9 and top_right == 9:
            score += diagonal_win

        again = input(f"\nYour score is currently {score}, would you like to play again? ")

        if again.lower() == "yes":
            continue
        else:
            print("Have a nice day.")
            break

    if score < 1:
        print("Im sorry, but you have ran out of score so you cannot play again.")
elif decide.lower() == "leave":
    print("Well then, see you soon!")
else:
    print("What?")