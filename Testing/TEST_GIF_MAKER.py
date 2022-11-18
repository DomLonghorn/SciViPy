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
    """ """
    Gif_Maker(filename)

    filepath = Path(filename + "TEST_GIF.gif")
    print(filepath.exists())
    assert filepath.exists()


Test_GIF(filepath)
