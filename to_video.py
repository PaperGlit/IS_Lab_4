import cv2
import os


def to_video():
    path = "temp/"
    frames = []
    for f in os.listdir(path):
        if f.endswith(".png"):
            file = os.path.join(path, f)
            image = cv2.imread(file)
            height, width, layers = image.shape
            size = (width, height)
            frames.append(image)

    output = cv2.VideoWriter("result.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 60, size)

    for image in frames:
        output.write(image)

    output.release()
