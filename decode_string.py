import os
from stegano import lsb


def decode_string():
    secret = []
    directory = "temp/"
    for i in range(1, len(os.listdir(directory)) + 1):
        f_name = f"{directory}{i}.png"
        try:
            secret_dec = lsb.reveal(f_name)
        except IndexError as e:
            print(f"No data was not found in {f_name}")
            secret_dec = ""
        secret.append(secret_dec)
    print(''.join([i for i in secret]))