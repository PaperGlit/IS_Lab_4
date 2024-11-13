import ffmpeg
import cv2
from stegano import lsb
from to_frames import to_frames
from encode_string import split_string
from rsa import RSA
from encode_string import  encode_string
from decode_string import decode_string
import os
from to_video import to_video

# vidcap = cv2.VideoCapture("video.mp4")
# count=0
# while True:
#         success, image = vidcap.read()
#         if not success:
#             break
#         cv2.imwrite(os.path.join("temp/", "{:d}.png".format(count)), image)
#         count += 1
#
#

to_frames("video")
rsa = RSA()

value = rsa.encrypt("Hello world!", rsa.public_key)
print(value)
value_string = " ".join(map(str, value))
encode_string(value_string)


video = ffmpeg.input("temp/%d.png", framerate=60).video
audio = ffmpeg.input("video.mp4").audio
(ffmpeg.output(audio, video, "result.mp4", preset="ultrafast").run(quiet=True, overwrite_output=True))
# # to_video()
to_frames("result")
decode_string()