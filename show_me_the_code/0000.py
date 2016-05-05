from PIL import Image, ImageDraw, ImageFont 
import random 
import os

def write_num():
    num = str(random.randint(1, 99))
    NumColor = (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
    basedir = os.path.abspath(os.path.dirname(__file__))


    img = Image.open(os.path.join(basedir,'img', '0000_img.jpg'))
    w, h = img.size
    wDraw = 0.8 * w
    hDraw = 0.08 * h
    fontdir = os.path.join(basedir, 'img', 'arial.ttf')
    font = ImageFont.truetype(fontdir, 30)
    draw = ImageDraw.Draw(img)
    draw.text((wDraw, hDraw), num,font = font, fill = NumColor)
    img.save(os.path.join(basedir, 'img', '0000.png'), 'png')

if __name__ == '__main__':
    write_num()