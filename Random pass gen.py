import random
import string

characters = list(string.ascii_letters + string.digits + string.punctuation)

def passwordgen():

    pass_length = int(input('How long would you like your password to be ? : '))
    
    random.shuffle(characters)

    password = []
    for j in range(pass_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input('Do you want to generate a random password ? Enter y or n : ')

if option == 'y' or option =='Y' :
    passwordgen()
elif option =='n' or option == 'N' :
    print("Quitting program")
    quit()
else :
    print('Invalid option , please enter a valid option ')