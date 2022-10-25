"""Script which takes a series of genereated images and arranges them sequentially into a gif.

This project, including this file, is licensed under MPL-2.0. It is important to note that  
the only accepted filetype is .png, although this is planned to be expanded in later updates
"""

# import required module
import glob
import os
import imageio
from tkinter import Tk
from tkinter.filedialog import askdirectory


def Gif_make():
    """Main function to execute the gif making procedure. Currently only accepts .png files.


    Returns:
        A gif made up of the .png files found in the target directory saved in the target directory
    """
    folder_dir = askdirectory(
        title="Select Folder"
    )  # shows dialog box and return the path
    print(folder_dir)

    # iterate over files in
    # that directory
    imagesList = []
    for images in glob.iglob(f"{folder_dir}/*"):

        # check if the image ends with png
        if images.endswith(".png"):
            imagesList.append(images)
            print(images)
    imagesList.sort()

    with imageio.get_writer(folder_dir + "/Jorek.gif", mode="I") as writer:
        for filename in imagesList:
            image = imageio.imread(filename)
            writer.append_data(image)
