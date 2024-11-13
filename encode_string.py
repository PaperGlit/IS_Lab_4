from remove_temp import remove_temp
from split_string import split_string
from stegano import lsb
import random
import os


def encode_string(input_string):
    # split_string_list = split_string(input_string)

    count = len([f for f in os.listdir("temp") if os.path.isfile(os.path.join("temp", f))])
    frame = random.randint(1, count)
    file_name = f"temp/{frame}.png"
    frame_encoded = lsb.hide(file_name, input_string)
    os.remove(file_name)
    frame_encoded.save(file_name)


    #
    # for i in range(1, len(split_string_list) + 1):
    #     file_name = f"temp/{i}.png"
    #     secret_enc = lsb.hide(file_name, split_string_list[i - 1])
    #     os.remove(file_name)
    #     secret_enc.save(file_name)
    #     print("[INFO] frame {} holds {}".format(file_name, split_string_list[i - 1]))