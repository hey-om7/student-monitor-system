import os
import datetime


def cleanup():
    try:
        os.remove("cache/img_screenshot.png")
    except:
        pass
    try:
        os.remove("cache/img_webcam.jpg")
    except:
        pass
    ct = datetime.datetime.now()
    currentTime = str(ct).split(".")[0]
    os.rename("cache/combined.jpg", f"pics_dump/{currentTime}.jpg")
