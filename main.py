# Import the required module
from PIL import Image

def main():
    '''Repeating the image on the background'''

    # load the background image
    background = Image.open('Background.jpg')
    background.resize((int(background.size[0] / 2),int(background.size[1] / 2)))

    width , height = background.size

    # copy background
    back_copy = background.copy()

    # load the repeted image
    img = Image.open('python.png')
    img = img.resize((int(img.size[0] / 2),int(img.size[1] / 2)))
    
    img_width , img_height = img.size

    

    for left in range(0,width,img_width):
        for top in range(0,height,img_height):
            print(left,top) # points

            back_copy.paste(img,(left,top))
    back_copy.save("Result.png")

if __name__ == "__main__":

    main()
    print('Code Completed 🔥')