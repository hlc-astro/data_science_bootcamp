import imageio
import os
input_folder="/Users/capelo/Desktop/constructor/portfolio/data_science_bootcamp/Project1/assets/data_challenge_intro"
output_file="challenge_animaition"

'''
def merge_gifs(input_folder, output_file):
    gif_files = [file for file in os.listdir(input_folder) if file.endswith('.gif')]
    frames = []
    for file_name in gif_files:
        file_path = os.path.join(input_folder, file_name)
        frames.append(imageio.imread(file_path))
    imageio.mimsave(output_file, frames, 'GIF')

# Replace 'input_folder' with the directory containing your GIF files
#input_folder = '/path/to/gifs'
# Replace 'output_file' with the desired name for the output GIF
#output_file = 'merged.gif'

merge_gifs(input_folder, output_file)
'''


import imageio
import os

def merge_gifs(input_folder, output_file, frame_duration):
    gif_files = [file for file in os.listdir(input_folder) if file.endswith('.gif')]
    frames = []
    for file_name in gif_files:
        file_path = os.path.join(input_folder, file_name)
        frames.append(imageio.imread(file_path))
    imageio.mimsave(output_file, frames, 'GIF', duration=frame_duration)


# Replace 'frame_duration' with the desired duration for each frame (in seconds)
frame_duration = 2.5

merge_gifs(input_folder, output_file, frame_duration)
