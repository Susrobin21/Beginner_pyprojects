#dice rolling simulator

import random

def diceroll():

    dice_drawing = {
        1: (
            "---------",
            "|        |",
            "|   O    |",
            "|        |",
            "---------",
        ),
        2: (
            "---------",
            "|O       |",
            "|        |",
            "|      O |",
            "---------",
        ),
        3: (
            "---------",
            "|O       |",
            "|  O     |",
            "|    O   |",
            "---------",
        ),
        4: (
            "---------",
           "| O    O |",
           "|        |",
           "| O    O |",
            "---------",
        ),
        5: (
            "---------",
            "| O    O |",
            "|    O   |",
            "| O    O |",
            "---------",
        ),
        6: (
            "---------",
            "| O    O |",
            "| O    O |",
            "| O    O |",
            "---------",
        ),

    }
    roll = input('Do you want to roll the dice? (Yes/No): ')

    while roll.lower() == 'yes':
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)

        print('Dice is rolled: {} and {}'.format(first_dice, second_dice))

        print('\n'.join(dice_drawing[first_dice]))
        print('\n'.join(dice_drawing[second_dice]))

        roll = input('Do you want to roll the dice again? (Yes/No): ')


        if roll.lower() not in ['yes', 'no']:
            print("Invalid input. Please enter 'Yes' or 'No' ")
            roll = input('Do you want to roll the dice again? (Yes/No): ')

    print('Thank you for playing !')

diceroll()
