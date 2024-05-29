import pyautogui
from PIL import ImageGrab

def clamp(num, upper, lower):
    return num if num >= lower and num <= upper else lower if num <= upper else upper

mousePosition = [pyautogui.size()[0]/2, pyautogui.size()[1]/2]

dimensions = [512, 256]
images = []
easedMousePostion = mousePosition
smoothing = 0.1

def setSmoothing(factor):
    global smoothing
    smoothing = factor

def setDimensions(x, y):
    global dimensions
    dimensions = [x, y]

def takeSS():
    global mousePosition
    global easedMousePostion
    global images

    supposed = pyautogui.position()
    mousePosition = [
        clamp(supposed[0], pyautogui.size()[0] - dimensions[0], dimensions[0]),
        clamp(supposed[1], pyautogui.size()[1] - dimensions[1], dimensions[1])
    ]
    easedMousePostion = [easedMousePostion[0] + (mousePosition[0] - easedMousePostion[0])*smoothing, easedMousePostion[1] + (mousePosition[1] - easedMousePostion[1])*smoothing]

    im2 = ImageGrab.grab(bbox =(round(easedMousePostion[0]) - dimensions[0], round(easedMousePostion[1]) - dimensions[1], round(easedMousePostion[0]) + dimensions[0], round(easedMousePostion[1]) + dimensions[1]))
    images.append(im2)

recording = True
def start():
    global easedMousePostion
    global images

    recording = True

    images = []

    easedMousePostion = [pyautogui.position()[0], pyautogui.position()[1]]
    while recording:
        takeSS()

stoppedImages = []
def stop():
    global recording
    global stoppedImages
    recording = False
    stoppedImages = images[0:]

def save(fileName, fps):
    frame_one = stoppedImages[0]
    frame_one.save(fileName, format="GIF", append_images=stoppedImages,
                save_all=True, loop=0, duration=round(len(stoppedImages)*fps))