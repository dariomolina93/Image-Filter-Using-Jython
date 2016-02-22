## Dario Molina
## 2/7/15
## Description:  Create a program that inputs pictures of a statue and a man in a picture, the final product should be of one picture without the man and a clear image of the statue


file1 = pickAFile()
file2 = pickAFile()## inputing files
file3 = pickAFile()
file4 = pickAFile()
file5 = pickAFile()
file6 = pickAFile()
file7 = pickAFile()
file8 = pickAFile()
file9 = pickAFile()

image1 = makePicture(file1)##making files as pictures
image2 = makePicture(file2)
image3 = makePicture(file3)
image4 = makePicture(file4)
image5 = makePicture(file5)
image6 = makePicture(file6)
image7 = makePicture(file7)
image8 = makePicture(file8)
image9 = makePicture(file9)

pictures = [image1, image2, image3, image4, image5, image6, image7, image8, image9]## 9 pictures strored in an array

newPicture = makeEmptyPicture(getWidth(image1), getHeight(image1))## creating a blank image

for i in range(0,getWidth((image1))):## loop that goes through all the pixels horizontally
 for j in range(0,getHeight(image1)):## loop that goes throught all the pixels vertically
  colorRed = []## list that will keep the red values of each pixel
  colorGreen = []##... of green values
  colorBlue = []## ... of blue values

  for k in range(0, 9):## loop that will go through of each picture
    newPixel = getPixel(pictures[k], i , j)## get pixel value at position i, j
    
    emptyPixel = getPixel(newPicture, i, j)## pixel position at i, j
    
    colorRed.append(getRed(newPixel))## add values of appropiate value to each corresponding list
    colorGreen.append(getGreen(newPixel))
    colorBlue.append(getBlue(newPixel))
    
  colorRed.sort()## sort each value from least to greatest
  colorGreen.sort()
  colorBlue.sort()
  
  medianRed = colorRed[4]## get value that is at the middle
  medianGreen = colorGreen[4]
  medianBlue = colorBlue[4]
  
  setRed( emptyPixel, medianRed)## put the median value into the new image in the i, j position
  setGreen(emptyPixel, medianGreen)
  setBlue(emptyPixel, medianBlue)
  

show(newPicture)## after it has gone through each pixel, display the image

    