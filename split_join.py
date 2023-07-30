import os
from tkinter import filedialog
from tkinter import Tk
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import concatenate_videoclips


def split_video(n):
    print("Requesting video file for division...")
    video_file = filedialog.askopenfilename(title="Select the video to split")
    print("Selected video:", video_file)
    print("Requesting output directory...")
    output_dir = filedialog.askdirectory(title="Select where to save the split videos")
    print("Selected directory:", output_dir)
    print("Opening video with MoviePy...")
    clip = VideoFileClip(video_file)
    duration = clip.duration
    part_duration = duration / n
    for i in range(n):
        start_time = i * part_duration
        end_time = (i + 1) * part_duration
        if i == n - 1:  # if it's the last part, ensure it goes to the end of the video
            end_time = duration
        output_file = os.path.join(output_dir, "part{}.mp4".format(i + 1))
        print("Extracting part {}...".format(i + 1))
        ffmpeg_extract_subclip(video_file, start_time, end_time, targetname=output_file)


def join_videos():
    video_files = []
    for i in range(2):  # to ensure at least two videos are selected
        video_files.append(
            filedialog.askopenfilename(title="Select video {}".format(i + 1))
        )
    while True:
        print("\nOrder of the videos:")
        for i, file in enumerate(video_files, start=1):
            print("{}. {}".format(i, file))
        add_more = input("\nDo you want to add another video? (y/n): ")
        if add_more.lower() == "y":
            video_files.append(
                filedialog.askopenfilename(
                    title="Select video {}".format(len(video_files) + 1)
                )
            )
        else:
            break
    output_file = filedialog.asksaveasfilename(
        defaultextension=".mp4", title="Select where to save the final video"
    )
    clips = [VideoFileClip(video) for video in video_files]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_file)


def convert_to_mp4():
    print("Requesting video file for conversion...")
    video_file = filedialog.askopenfilename(title="Select the video to convert")
    print("Selected video:", video_file)
    print("Requesting output directory...")
    output_dir = filedialog.askdirectory(
        title="Select where to save the converted video"
    )
    output_file = os.path.join(output_dir, "converted.mp4")
    clip = VideoFileClip(video_file)
    clip.write_videofile(output_file)


def main():
    try:
        print("1. Split videos")
        print("2. Join videos")
        print("3. Convert video to MP4")
        choice = int(input("Choose an option (1, 2 or 3): "))
        root = Tk()
        root.withdraw()  # hide the extra window
        if choice == 1:
            n = int(input("Split into how many parts? "))
            split_video(n)
        elif choice == 2:
            join_videos()
        elif choice == 3:
            convert_to_mp4()
        else:
            print("Invalid option!")
    except KeyboardInterrupt:
        print("\\nOperation interrupted by the user.")


if __name__ == "__main__":
    main()
