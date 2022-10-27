"""Script which takes a series of genereated images and arranges them sequentially into a gif.

This project, including this file, is licensed under MPL-2.0. It is important to note that  
the only accepted filetype is .png, although this is planned to be expanded in later updates
"""

# import required module
import glob
import os

import imageio.v2 as imageio

# get the path/directory


from tkinter import Tk
from tkinter.filedialog import askdirectory

folder_dir = askdirectory(
    title="Select Folder"
)  # shows dialog box and returns the path
print(folder_dir)


def Gif_Maker(filename, Duration=2, GIF_Name="/Jorek.gif"):
    """Creates a gif based off a set of given .pngs

    This functions takes a directory and turns all .pngs within it into a gif with a set duration per slide.

    Args:
        filename:   This is the filepath for the directory which should contain .pngs to be created.
        Duration:   This will set the duration for each frame within the gif. Default value is set to be 2.
        GIF_name:   This is the name of the gif to be added to the directory witht the images.

    Returns:
        This function returns the created GIF in the directory specified for the images.

    """
    imagesList = []
    for images in glob.iglob(f"{filename}/*"):

        # check if the image ends with png
        if images.endswith(".png"):
            imagesList.append(images)
    imagesList.sort()

    with imageio.get_writer(filename + GIF_NAME, mode="I", duration=Duration) as writer:
        for filename in imagesList:
            image = imageio.imread(filename)
            writer.append_data(image)


Gif_Maker(folder_dir)

