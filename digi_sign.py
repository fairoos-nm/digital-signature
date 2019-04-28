from PIL import Image, ImageDraw, ImageFont


# def take_image():
#     """ load image initialise the drawing context"""
#     image = Image.open("123.jpg")
#     return image

# def digi_signature(image):
#     """sign in your image"""
#     draw = ImageDraw.Draw(image)
#     (x, y) = (1000, 700)
#     sign = "Demo sign"
#     color = "rgb(0, 0, 0)"
#     font = ImageFont.truetype("Roboto-Bold.ttf", size=45)
#     draw.text((x, y), sign, fill=color, font=font)
#     file_name_to_save = input("enter a file name you want to save : ")
#     image.save(file_name_to_save)

# def main():
#     image = take_image()
#     digi_signature(image)

# if __name__ == "__main__":
#     main()


class digi_signature(object):
    def __init__(self, image, sign):
        self.image = image
        self.sign = sign

    def take_image(self):
        """ load image initialise the drawing context"""
        image = Image.open(self.image)
        return image

    def digi_sign(self):
        """sign in your image"""
        image = self.take_image()
        draw = ImageDraw.Draw(image)
        (x, y) = (1000, 700)
        color = "rgb(0, 0, 0)"
        font = ImageFont.truetype("Roboto-Bold.ttf", size=45)
        draw.text((x, y), self.sign, fill=color, font=font)
        file_name_to_save = input("enter a file name you want to save : ")
        image.save(file_name_to_save)

first_image = digi_signature("123.jpg", "Demo sign")
second_image = digi_signature("123.jpg", "Hello world")
first_image.digi_sign()
second_image.digi_sign()

