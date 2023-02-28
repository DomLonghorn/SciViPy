"""
This project, including this file, is licensed under MPL-2.0.
"""

from pathlib import Path

import imageio.v2 as imageio
from tkinter.filedialog import askdirectory


def make_gif(dirname: Path, duration: int = 2, gif_name: str = "Jorek.gif"):
    """
    Creates a gif based off a set of given .pngs.  It is important to note that the only
    accepted filetype is .png, although this is planned to be expanded in later updates.

    This functions takes a directory and turns all .pngs within it into a gif with a set
    duration per slide.

    Creates a GIF in the same directory specified for the images.

    Args
    ----
    dirname: Path
        This is the path for the directory which should contain .pngs to be created.
    duration: int, default 2
        This will set the duration for each frame within the gif, in seconds.
    gif_name: str, default "Jorek.gif"
        This is the name of the gif to be added to the directory with the images.

    Returns
    -------
    Path
        Path to the created Gif.

    Raises
    ------
    NotADirectoryError
        If dirname is not a valid directory
    RuntimeError
        If no png files are found.

    """
    dirname = Path(dirname)
    if not dirname.is_dir():
        raise NotADirectoryError(dirname)

    images = sorted(dirname.rglob("*.png"))
    if not images:
        raise RuntimeError(f"No png files found in: {dirname}")

    output = dirname / gif_name

    with imageio.get_writer(output, mode="I", duration=duration) as writer:
        for filename in images:
            image = imageio.imread(filename)
            writer.append_data(image)

    return output


def main():
    """
    Scripting interface for make_gif. Opens a window asking the user to choose a
    directory, and runs make_gif on that directory.
    """
    png_dir = askdirectory(title="Select Folder")
    make_gif(png_dir)


if __name__ == "__main__":
    main()
