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
    folder_name = currentTime.split()[0]
    if not (os.path.isdir(f"pics_dump/{folder_name}")):
        os.mkdir(f"pics_dump/{folder_name}")
    os.rename("cache/combined.jpg", f"pics_dump/{folder_name}/{currentTime}.jpg")
