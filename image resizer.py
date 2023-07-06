#image resizer 

from PIL import Image

def resizing(length,width):
    
    pic = Image.open('op2.jpg')

    print(f'Current size of the image : {Image.size}')

    resized_image = Image.resize((length,width))

    resized_image.save('op2'+length+'.jpg')

length = int(input('Enter the length : '))
width = int(input('Enter the width : '))
resizing(length,width)

#input of the image's name cant be used because the image's name can't be copied onto the terminal 
#So just change the image's name which needs to be adjusted 
#Only the file's name not the path of the file 
