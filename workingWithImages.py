from PIL import Image 
mac = Image.open('example.jpg')
#to print the image out on preview for mac users
#mac.show()
print(mac.size)
print(mac.filename)
print(mac.format_description)

#cropping images
# x is horizontal /pointing to the right
# y is vertical /pointing down
# height is vertical 
# width is horizontal
# start at very top left corner 

crop_area = (0,0,100,100)
cropped_image = mac.crop(crop_area)
#cropped_image.show()

pencils = Image.open('pencils.jpg')
print(pencils.size)
x =0 
y = 0
width = 1950/3 
height = 1300/10
cropped_area_pencils = (x,y,width,height)
cropped_image_pencils = pencils.crop(cropped_area_pencils)
#cropped_image_pencils.show()

#copy and paste the mac image to top left hand corner 
print(mac.size)
halfway = 1993/2 
x = halfway -200
w = halfway+200
y = 800 
h = 1257
cropped_area_mac = (x,y,w,h)
cropped_mac_image = mac.crop(cropped_area_mac)
mac.paste(im= cropped_mac_image, box=(0,0))
#mac.show()


#mac.resize((3,000,500))
#mac.rotate(90)

#color transparency 
#RDBA- Red,Green,Blue,Alpha
red = Image.open('red_color.jpg')
# red.show()
red.putalpha(128)
red.show()



# # Replace 'your_image.png' with the name of your PNG file
# try:
#     image = Image.open('blue_color.png')
#     image.show()
# except FileNotFoundError:
#     print("The file was not found. Please check the file name and path.")
# except IOError:
#     print("An error occurred while opening the image. Please make sure the file is a valid PNG image.")

# #paste an image on top 
# blue.paste(im = red,box=(0,0),mask = red)
# blue.show()
# blue.save("purple.png")
# purple = Image.open("purple.png")
# purple.show()