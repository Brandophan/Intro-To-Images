from PIL import Image 
# working with 
# word_matrix.png 
# mask.png 
# The word_matrix is a .png image that contains a spreadsheet of words with a hidden message in it.

# The task is to use the mask.png image to reveal the hidden message inside the word_matrix.png. Keep in mind, you may need to resize the mask.png in order for this to work.



# Replace 'your_image.png' with the name of your PNG file
try:
    words = Image.open('word_matrix.png')
    words.show()
except FileNotFoundError:
    print("The file was not found. Please check the file name and path.")
except IOError:
    print("An error occurred while opening the image. Please make sure the file is a valid PNG image.")



# Replace 'your_image.png' with the name of your PNG file
try:
    mask = Image.open('mask.png')
    mask.show()
except FileNotFoundError:
    print("The file was not found. Please check the file name and path.")
except IOError:
    print("An error occurred while opening the image. Please make sure the file is a valid PNG image.")


#Resize images to match
print(mask.size)
print(words.size)
mask = mask.resize((1015,559))
print(mask.size)

#add in alpha parameter 
mask.putalpha(200)
mask.show()

words.paste(mask,(0,0),mask)
words.show()