from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def superimpose_text(namefile: str, written_text: str):
    img = Image.open(namefile)
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype("Arial.ttf", 100)
    I1.text((10, img.height - 125), written_text, font=myFont, fill=(255, 0, 0))
    img.save(namefile)
