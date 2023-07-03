#word replacement project 
def replacee():
    stat = input('enter a string :')
    strrepd = input('enter the word to be replaced :')
    strepct = input('enter the replacement word :')
    swap = stat.replace(strrepd,strepct)
    print(swap)
replacee()
