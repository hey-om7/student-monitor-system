import cv2

camera_port = 1
ramp_frames = 10
camera = cv2.VideoCapture(camera_port)


def get_image():
    retval, im = camera.read()
    return im


for i in range(ramp_frames):
    temp = camera.read()

camera_capture = get_image()
filename = "img_webcam.jpg"
cv2.imwrite(filename, camera_capture)
del camera
