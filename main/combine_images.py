from PIL import Image


def combineNow(name1: str, name2: str, filename: str):
    img1 = Image.open(name1)
    img2 = Image.open(name2)

    def concatImg(img1, img2):
        new_img = Image.new(
            "RGB",
            (img1.width + img2.width, max(img1.height, img2.height)),
        )
        new_img.paste(
            img1,
            (
                0,
                int(
                    max(img1.height, img2.height) / 2
                    - min(img1.height, img2.height) / 2
                ),
            ),
        )
        new_img.paste(img2, (img1.width, 0))
        return new_img

    concatImg(img1, img2).save(filename)
