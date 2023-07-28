#email slicer


def slicer():
    print('Welcome to email slicer ')
    input_email = input('Enter your email id here :')

    (user_name, domain) = input_email.split('@')         
    (domain, extensions) = domain.split('.')

    print('Username :' , user_name)
    print('Domain : ', domain)
    print('Extension : ', extensions)

slicer()



#split , Return a list of the words in the string, by seperating them by the given parameter , here its is @ and .
# username , domain and extension are variables 
#username - Name of user 
# domain - The part of an email address that comes after the "@" symbol, and it functions like a virtual street name that lets your email get delivered to the right address
# extension - top level domain