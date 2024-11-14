from remove_temp import remove_temp
from to_frames import to_frames
from stegano import lsb
from rsa import RSA
import os


def decode():
    video_name = input("Enter the name of the video to be decoded (including the extension): ")
    n = input("Enter the RSA private key (n): ")
    d = input("Enter the RSA private key (d): ")
    private_key = (int(n), int(d))

    to_frames(video_name)

    print("Decoding message from the frames...")
    secret = []
    for i in range(1, len(os.listdir("temp/")) + 1):
        f_name = f"temp/{i}.png"
        try:
            secret_dec = lsb.reveal(f_name)
        except IndexError:
            break
        secret.append(secret_dec)
    remove_temp()
    print("Done!")

    encoded_array = []
    number_array = []
    for i in secret:
        if i != " ":
            number_array.append(i)
        else:
            encoded_array.append(int("".join(number_array)))
            number_array = []
    encoded_array.append(int("".join(number_array)))
    decoded_message = RSA.decrypt(private_key, encoded_array)
    print("Decoded message:", decoded_message)