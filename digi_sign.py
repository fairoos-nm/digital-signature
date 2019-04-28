from PIL import Image, ImageDraw, ImageFont


def take_image():
    """ load image initialise the drawing context"""
    image = Image.open("123.jpg")
    return image

def digi_signature(image):
    """sign in your image"""
    draw = ImageDraw.Draw(image)
    (x, y) = (1000, 700)
    sign = "Demo sign"
    color = "rgb(0, 0, 0)"
    font = ImageFont.truetype("Roboto-Bold.ttf", size=45)
    draw.text((x, y), sign, fill=color, font=font)
    file_name_to_save = input("enter a file name you want to save : ")
    image.save(file_name_to_save)

def main():
    image = take_image()
    digi_signature(image)

if __name__ == "__main__":
    main()
