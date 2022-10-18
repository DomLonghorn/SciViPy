# import required module
from ast import Assert
import glob
import imageio.v2 as imageio
from pathlib import Path

from tkinter import Tk
from tkinter.filedialog import askdirectory
from gif_maker import Gif_Maker

filepath = "C:\\Users\FWKCa\OneDrive\Desktop\SciViPy\Testing\Test Images\\"


def Test_GIF(filename):
    """
    This function, takes a file name and then creates a GIF

    It then test's whether the correct file path is created by the GIF function

    And should return an assertion error if not.

    No way of checking if the GIF created is the correct GIF, known issue - currently working on it

    """
    Gif_Maker(filename)

    filepath = Path(filename + "TEST_GIF.gif")
    print(filepath.exists())
    assert filepath.exists()


Test_GIF(filepath)
