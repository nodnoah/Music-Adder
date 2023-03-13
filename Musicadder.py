import os
import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp
import pyfiglet


def add_music(video_path, audio_path, volume):
    # Load the video clip
    video_clip = mp.VideoFileClip(video_path)

    # Load the audio clip and adjust the volume
    audio_clip = mp.AudioFileClip(audio_path).volumex(float(volume)/5)

    # Trim the audio clip to the length of the video clip
    if audio_clip.duration < video_clip.duration:
        audio_clip = audio_clip.audio_loop(duration=video_clip.duration)
    else:
        audio_clip = audio_clip.set_duration(video_clip.duration)

    # Create a CompositeAudioClip with the original audio and the new background audio
    final_audio = mp.CompositeAudioClip([video_clip.audio, audio_clip])

    # Set the final audio for the video clip
    video_clip = video_clip.set_audio(final_audio)

    # Create an output folder if it doesn't exist
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate the output filename
    output_filename = os.path.join(output_folder, os.path.splitext(os.path.basename(video_path))[0] + '_music.mp4')

    # Write the video with the new audio to the output file
    video_clip.write_videofile(output_filename)

    # Close the clips
    video_clip.close()
    audio_clip.close()


# Create a Tkinter window for selecting files
root = tk.Tk()
root.withdraw()

# Print the program title in ASCII art
ascii_title = pyfiglet.figlet_format("Video Music Adder")
print(f"\033[2J\033[1;1H{ascii_title}\n")

# Prompt the user to select a video file
print("Please select your Video file")
video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])

# Prompt the user to select an audio file
print("Please select your Audio file")
audio_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3")])

# Prompt the user for the music volume
while True:
    try:
        volume = int(input("Enter the volume of the music (1-5): "))
        if 1 <= volume <= 5:
            break
        else:
            print("Volume must be between 1 and 5")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5")

if video_path and audio_path:
    add_music(video_path, audio_path, volume)
else:
    print("No file found. Please try again.")
