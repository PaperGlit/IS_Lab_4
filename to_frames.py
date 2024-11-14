from remove_temp import remove_temp
import ffmpeg


def to_frames(video_name):
    remove_temp()

    print("Outputting frames...")
    (ffmpeg.input(video_name).output("temp/%d.png").run(quiet=True, overwrite_output=True))
    print("Done!")