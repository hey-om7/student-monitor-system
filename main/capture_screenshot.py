import pyautogui as pya


def captureScreenshot(name):
    image = pya.screenshot()
    image.save(name)
