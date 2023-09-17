import pyautogui
from PIL import ImageGrab

def clamp(num, upper, lower):
    return num if num >= lower and num <= upper else lower if num <= upper else upper

mousePosition = [pyautogui.size()[0]/2, pyautogui.size()[1]/2]

dimensions = [512, 256]
images = []
easedMousePostion = mousePosition

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
    easedMousePostion = [easedMousePostion[0] + (mousePosition[0] - easedMousePostion[0])*0.9, easedMousePostion[1] + (mousePosition[1] - easedMousePostion[1])*0.9]

    im2 = ImageGrab.grab(bbox =(round(easedMousePostion[0]) - dimensions[0], round(easedMousePostion[1]) - dimensions[1], round(easedMousePostion[0]) + dimensions[0], round(easedMousePostion[1]) + dimensions[1]))
    images.append(im2)

recording = True
def start():
    while recording:
        takeSS()

def stop():
    global recording
    recording = False
    images = []

def save(fileName, fps):
    frame_one = images[0]
    frame_one.save(fileName, format="GIF", append_images=images,
                save_all=True, loop=0, duration=round(len(images)*fps))