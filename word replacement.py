#word replacement project 
def replacee():
    stat = 'hiee this is my first project, well technically speaking this cant even be called a project but yes i will try to make better ones'
    strrepd = input('enter the word to be replaced :')
    strepct = input('enter the replacement word :')
    swap = stat.replace(strrepd,strepct)
    print(swap)
replacee()