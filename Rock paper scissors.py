# ROCK PAPER SCISSORS 

import random

exit = False
user_points = 0
computer_points = 0

while exit== False:
    options = ['r','p','s','exit']
    #print(' For rock choose r or R\n For scissors choose s or S\n For paper choose p or P\n For exit choose e or E ')
    user_choice = input(' Enter your input rock,paper,scissors or exit :')
    computer_choice = random.choice(options)
    if user_choice=='exit' :
        print('Game over')
        print('You points : ' ,user_points )
        print('Computer points : ',computer_points)
        exit== True
    
    if user_choice == 'r' or user_choice == 'R' :
        if computer_choice == 'r' or computer_choice == 'R':
            print('Your input and the computer input are the same :( ')
            print('Tie it is then !')
        elif computer_choice =='s' or computer_choice == 'S' :
            print('Your input is rock and the computer input is scissor')
            print('You win yay >.< ! ')
            user_points += 1
        elif computer_choice =='P' or computer_choice == 'P' :
            print('Your input is rock and the computer input is paper')
            print('You lose :(, Better luck next time ! ')
            computer_points +=1
    elif user_choice == 's' or user_choice == 'S' :
        if computer_choice == 's' or computer_choice == 'S':
            print('Your input and the computer input are the same :( ')
            print('Tie it is then !')
        elif computer_choice =='r' or computer_choice == 'R' :
            print('Your input is scissor and the computer input is rock')
            print('You lose :( , Better luck next time ! ')
            computer_points += 1
        elif computer_choice =='P' or computer_choice == 'P' :
            print('Your input is scissor and the computer input is paper')
            print('You win yay >.< ! ')
            user_points +=1
    elif user_choice == 'p' or user_choice == 'P' :
        if computer_choice == 's' or computer_choice == 'S':
            print('Your input is paper and the computer input is scissor ')
            print('You lose :(, Better luck next time ! ')
            computer_points += 1
        elif computer_choice =='r' or computer_choice == 'R' :
            print('Your input is paper and the computer input is rock')
            print('You win yay >.< ! ')
            user_points +=1
        elif computer_choice =='P' or computer_choice == 'P' :
            print('Your input and the computer input are the same :( ')
            print('Tie it is then !')

    elif user_choice != 'r' or user_choice != 'R' or user_choice != 'p' or user_choice != 'P' or user_choice != 's' or user_choice != 'S'  or user_choice != 'exit':
        print('Invalid input, please choose out of the below options :')
        print(' For rock choose r or R\n For scissors choose s or S\n For paper choose p or P\n To exit type exit please')


# i still have a few corrections in the code regarding the exit part it's not so effecient but i'm working on it .
