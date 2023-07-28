#site connectivity checker 

import urllib.request as urllib                            

def connectcheck(url):

    print("Checking connectivity ")

    check = urllib.urlopen(url)
    
    print('Connected to ',url,'successfully')

    print('The response code was : ' , check.getcode())

print('Welcome to site connectivity checker ')
url_to_check = input('Input the url of the site :')
connectcheck(url_to_check)



# 1) importing urllib module to use certain commands such as urlopen()

# 2) urlopen() Opens the URL url, which can be either a string or a Request object.

# 3) if the response code is 200 then the connection with the site is successful else not 