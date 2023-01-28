from PIL import Image

img1 = Image.open("img_webcam.jpg")
img2 = Image.open("img_screenshot.png")


def concatImg(img1, img2):
    new_img = Image.new(
        "RGB",
        (
            img1.width + img2.width,
            img1.height if img1.height > img2.height else img2.height,
        ),
    )
    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (img1.width, 0))
    return new_img


concatImg(img1, img2).save("concatted.jpg")
# concatImg(img1, img2).show()
