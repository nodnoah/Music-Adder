Video Music Adder

Video Music Adder is a Python script that allows you to add background music to a video. You can select a video file and an audio file, adjust the volume of the music, and the script will create a new video file with the original audio and the new background audio.

Requirements

To use this script, you need to have the following installed:

    Python 3.x
    tkinter module (usually included in Python)
    moviepy module (can be installed using pip)

How to use

    Clone this repository or download the Musicadder.py file.

    Install the required modules using pip:

pip install -r requirements.txt

Open a terminal or command prompt and navigate to the folder containing the py file.

Run the script:

    python Musicadder.py

    Follow the prompts to select a video file, an audio file, and adjust the volume of the music.

    The new video file will be saved in an output folder in the same directory as the script.

Notes

    The script only works with .mp4 video files and .mp3 audio files.
    If the video clip is longer than the audio clip, the script will loop the audio clip to match the duration of the video clip.
    The volume of the music can be adjusted from 1 to 5, with 1 being the lowest and 5 being the highest.
