from remove_temp import remove_temp
import ffmpeg


def to_frames(video_name):
    if not video_name.endswith('.mp4'):
        video_name = video_name + '.mp4'

    remove_temp("temp/")

    print("Outputting frames...")
    (ffmpeg.input(video_name).output("temp/%d.png").run(quiet=True, overwrite_output=True))
    print("Done!")