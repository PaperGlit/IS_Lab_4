from decode import decode
from encode import encode


def main():
    while True:
        prompt = input("1 - Encode a video\n"
                       "2 - Decode a video\n"
                       "Your choice: ")
        match prompt:
            case "1":
                encode()
            case "2":
                decode()
            case _:
                break