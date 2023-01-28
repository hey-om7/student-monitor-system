# appversion:v1.1

from capture_screenshot import captureScreenshot
from capture_webcam import captureWebcam
from combine_images import combineNow
from cleanup import cleanup
from superimpose_text import superimpose_text
import time
import datetime

while 1:
    captureScreenshot("cache/img_screenshot.png")
    captureWebcam("cache/img_webcam.jpg")
    combineNow("cache/img_webcam.jpg", "cache/img_screenshot.png", "cache/combined.jpg")
    ct = datetime.datetime.now()
    currentTime = str(ct).split(".")[0]
    superimpose_text("cache/combined.jpg", currentTime)
    cleanup(currentTime)
    time.sleep(60)
