# Word dictionary 

from Pydictionary import Pydictionary

dictionary = Pydictionary()

while True:
    if word =='':
        break
    else:
        word = input('Enter the word : ')
        print(dictionary.meaning(word))



# We can give the input directly into the dictionary and we cant get the meanings by using 'get.meaning function

# Note : we have to install the PyDictionary library first in order to proceed