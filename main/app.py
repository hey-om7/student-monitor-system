# appversion:v1.0

from capture_screenshot import captureScreenshot

from capture_webcam import captureWebcam

from combine_images import combineNow
from cleanup import cleanup
import time

while 1:
    captureScreenshot("cache/img_screenshot.png")
    captureWebcam("cache/img_webcam.jpg")
    combineNow("cache/img_webcam.jpg", "cache/img_screenshot.png", "cache/combined.jpg")
    cleanup()
    time.sleep(60)
