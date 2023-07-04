#simple calculator 
def add(r,s):
    w = r + s
    print(str(r) + "+" +str(s)+ "=" +str(w))
def sub(r,s):
    x = r - s
    print(str(r) + "-" +str(s)+ "=" +str(x))
def mul(r,s):
    y = r * s
    print(str(r) + "*" +str(s)+ "=" +str(y))
def div(r,s):
    z = r / s
    print(str(r) + "/" +str(s)+ "=" +str(z))
while True :
    print('Choose any : \n a - addition \n b - subtraction \n c - multipliction \n d - division \n e - exit  ')
    option = input('Your option :')
    if option == 'a' or option =='A' :
        print('addition')
        r = int(input('enter the number :'))
        s = int(input('enter the number :'))
        add(r,s)
    elif option =='b' or option =='B' :
        print('subtraction')
        r = int(input('enter the number :'))
        s = int(input('enter the number :'))
        sub(r,s)
    elif option == 'c' or option == 'C' :
        print('multiplication')
        r = int(input('enter the number :'))
        s = int(input('enter the number :'))
        mul(r,s)
    elif option == 'd' or option == 'D' :
        print('division')
        r = int(input('enter the number :'))
        s = int(input('enter the number :'))
        div(r,s)
    elif option == 'e' or option == 'E' :
        print('program completed')
        quit()
