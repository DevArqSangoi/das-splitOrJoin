# das-splitOrJoin

This Python script allows you to split a video into several smaller parts and then join those parts back together. It uses the `moviepy` library to handle the video operations and `tkinter` for the user interface.

The main motivation for creating this script was to facilitate the use of Topaz Video AI. Topaz Video AI is a powerful tool for enhancing video quality, but it doesn't allow pausing and resuming a task. By splitting the video into smaller parts, each part can be enhanced separately. After all parts are enhanced, they can be joined back together.

## Dependencies

The script uses the following Python libraries:

- `os`
- `tkinter`
- `moviepy`

You only need to install moviepy, `os` and `tkinter` are part of the standard Python library:

- `pip install moviepy`

Note: `os` and `tkinter` are part of the Python Standard Library and should be available by default.

## How to Use

1. Run the script using Python 3.

- `python split_join.py`

2. The script will ask you whether you want to split or join videos. Enter '1' to split a video, or '2' to join videos.

3. If you choose to split a video:
   - The script will ask you how many parts you want to split the video into.
   - A file dialog will open for you to select the video to split.
   - A directory dialog will open for you to select where to save the split videos.
   - The script will then split the video into the specified number of parts.

4. If you choose to join videos:
   - The script will ask you to select at least two videos to join together.
   - After selecting the first two videos, the script will ask you whether you want to add another video. You can keep adding videos as long as you answer 'y'.
   - Once you answer 'n', a file dialog will open for you to select where to save the final joined video.
   - The script will then join all selected videos into a single video.

Enjoy your video processing!
