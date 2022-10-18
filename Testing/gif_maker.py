# import required module
import glob
import os

import imageio

# get the path/directory


from tkinter import Tk
from tkinter.filedialog import askdirectory

folder_dir = askdirectory(
    title="Select Folder"
)  # shows dialog box and returns the path
print(folder_dir)


def Gif_Maker(filename, Duration=0.5, GIF_NAME="/Jorek.gif"):
    """
    This function takes a single file path for your directory with collection of .pngs

    And then sorts them and then creates a GIF with duration equal to parameter given with default, 0.5 second duration.

    It then outputs the gif in the same directory

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
