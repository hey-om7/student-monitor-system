from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open("temp.jpg")

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.truetype("Arial.ttf", 100)

# Add Text to an image
I1.text((10, img.height - 125), "Nice Car", font=myFont, fill=(255, 0, 0))

# Display edited image
img.show()

# Save the edited image
img.save("temp2.jpg")
