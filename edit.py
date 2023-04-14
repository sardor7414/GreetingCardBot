from PIL import Image, ImageDraw, ImageFont
import io

def oneImg(word):
    img = Image.open('images/1.jpeg')
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('styles/FreeMonospacedBoldOblique.ttf', 150)
    d1.text((150, 700), word, font=myFont, fill=(0, 102, 0))
    buffer = io.BytesIO()
    img.save(buffer, format='PNG', quality=100)
    return buffer.getbuffer()


def secondImg(word):
    img = Image.open('images/2.jpg')
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('styles/FreeMonospacedOblique.ttf', 100)
    d1.text((1000, 0), f"Happy New Year \n{word}", font=myFont, fill=(153, 76, 0))
    buffer = io.BytesIO()
    img.save(buffer, format='PNG', quality=100)
    return buffer.getbuffer()

def threeImg(word):
    img = Image.open('images/3.jpg')
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('styles/FreeMonospacedBoldOblique.ttf', 25)
    d1.text((50, 100), f"Happy New Year \n{word}", font=myFont, fill=(51, 0, 0))
    buffer = io.BytesIO()
    img.save(buffer, format='PNG', quality=100)
    return buffer.getbuffer()
