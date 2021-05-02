from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

img = Image.open("image1.png")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# font = ImageFont.truetype("sans-serif.ttf", 16)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((248,335),"Sample Text written on image",(0,0,0))
img.save('sample-out.png')