import os
import ffmpeg
from rsa import RSA
from stegano import lsb
from to_frames import to_frames
from remove_temp import remove_temp
from split_string import split_string
from moviepy.editor import VideoFileClip


def encode():
    video_name = input("Enter the name of the video to be encoded (including the extension): ")
    result_name = input("Enter the name of the encoded file (excluding the extension): ")
    input_string = input("Enter the message to be encoded: ")

    to_frames(video_name)

    rsa = RSA()
    with open(result_name + "_key.txt", 'w') as file:
        file.write(f"n:  + {rsa.private_key[0]}\n"
                   f"d:  + {rsa.private_key[1]}\n"
                   f"e:  + {rsa.public_key[1]}\n")
    print("The RSA encoding key has been exported to", result_name + "_key.txt")

    print("Encoding message into frames...")
    message = " ".join(map(str, rsa.encrypt(input_string)))
    split_string_list = split_string(message)
    for i in range(1, len(split_string_list) + 1):
        file_name = f"temp/{i}.png"
        secret_enc = lsb.hide(file_name, split_string_list[i - 1])
        os.remove(file_name)
        secret_enc.save(file_name)
    print("Done!")

    print("Encoding video...")
    clip = VideoFileClip(video_name)
    fps = clip.fps
    video = ffmpeg.input("temp/%d.png", framerate=fps).video
    audio = ffmpeg.input(video_name).audio
    (ffmpeg.output(audio, video, result_name + ".avi", acodec="copy", vcodec="copy").run(quiet=True, overwrite_output=True))
    remove_temp()
    print("Encoding finished!")