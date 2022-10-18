# import required module
import glob
import imageio.v2 as imageio
import pathlib

# get the path/directory


from tkinter import Tk
from tkinter.filedialog import askdirectory

# folder_dir = askdirectory(title="Select Folder")  # shows dialog box and return the path
# folder_dir = '/home/user/Desktop/Data/Max Data/ConvertedData/DataAndScreenshots/Screenshots/small gif'

# iterate over files in
# that directory


def Test_GIF(filename):

    imagesList = []
    for images in glob.iglob(f"{filename}/*"):

        # check if the image ends with png
        if images.endswith(".png"):
            imagesList.append(images)
    imagesList.sort()

    with imageio.get_writer(filename + "/TEST_GIF.gif", mode="I") as writer:
        for filename in imagesList:
            image = imageio.imread(filename)
            writer.append_data(image)


Test_GIF(".../Test Images")
assert pathlib.Path.exists("Test Images" + "TEST_GIF.gif")
