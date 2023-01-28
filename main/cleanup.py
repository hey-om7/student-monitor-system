import os


def cleanup(currentTime: str):
    try:
        os.remove("cache/img_screenshot.png")
    except:
        pass
    try:
        os.remove("cache/img_webcam.jpg")
    except:
        pass

    os.rename("cache/combined.jpg", f"pics_dump/{currentTime}.jpg")
