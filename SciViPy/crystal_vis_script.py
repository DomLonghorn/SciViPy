"""
Script which takes in large 3D datasets of .CSV type and exports .png frames of them for
further visualisation.

This script, when run in a paraview shell, will take a collection of data points in a
.CSV format and produce a formatted clipped set of visualised frames for each data point
within the file. This script particularly is tailored at materials such as irradiated
zirconium. An example of this, for said zirconium, would be running
FrameCreation(/home/user/Desktop/Data/Max Data/CSVData/,/home/user/Desktop/Data/Max
Data/CSVData/Frames, Temp) Which would produce a set of frames for all the data given in
the directory for which their primary attribute shown is the scalar variable Temp. This
would be seen as the crystal structure with major temperature spots seen within the
crystal and coloured accordingly. (See README image)

Lisence: MPL-2.0

"""

from paraview.simple import *

# Must include this module when loading vtk files!
from paraview.servermanager import *

import argparse
from pathlib import Path
from textwrap import dedent

# 100 frames takes ~18 mins to process for the Max converted data set (85.3 Mbs each)

# Defines the standard clip used to show "extreme" or interesting parts of the data


def MaxClip(
    MyData,
    ScaVal,
    ScalarName,
    ColourRange,
    opacity=0.05,
):
    """
    Sets the data to the correct view, with opacity and viewing only the scalar value
    wanted.

    Sets the dataset imported to having the correct opacity as well as clipping the data
    to only show the specified scarlar variable and only from the Scalar value specified
    and up. This also sets an average colour array on to it to colour it specified based
    on the variable values given

    Parameters
    ==========
    MyData
        The data which has been imported in, usually in paraview documentation under the
        name reader.
    ScaVal: float
        The value for which you would like to clip from for your scalar
    ScarlarName: str
        The name of the variable you would like clip with e.g "Temp"
    ColourRange: Tuple[float, float]
        The range over which the colour scale will be set. E.g ColourRange = (0,0.2)
    Opacity: float, default is 0.05
        The opacity wanted for the clipped data. Default value = 0.05

    Returns
    =======
    The clipped view within paraview with set colours and set opacity
    """

    SetDisplayProperties(Opacity=opacity)
    clip = Clip(Input=MyData)

    clip.ClipType = "Scalar"
    clip.Scalars = ("POINTS", ScalarName)
    clip.Value = ScaVal
    clip.Invert = False

    display = Show(clip)

    ColourMap = GetColorTransferFunction(ScalarName)
    SetDisplayProperties(ColorArrayName=ScalarName)
    ColorBy(display, ("POINTS", ScalarName))
    ColourMap.RescaleTransferFunction(ColourRange)


# Turns the .CSV to actual points to be seen


def PointsView(Data):
    """
    Creates 3D data points from .csv file

    This performs the table to points function in paraview which converts the table of
    .csv values into actual datapoints in paraview which means that they can be acted
    upon by paraview functions.

    Sets the data in actual viewable points in the paraview instance as well as printing
    to the console that it has finished the process.

    Parameters
    ==========
    Data
        This is the read in data which you are actually converting from .csv to
        datapoints

    Returns
    =======
    None
    """
    TableToPoints(
        Input=Data, XColumn="X Position", YColumn="Y Position", ZColumn="Z Position"
    )

    print("Interpolated to points")


# Colours the points based on a set range


def MaxColour(points, ScalarName, Range=(0, 0.2), Preset="Inferno (matplotlib)"):
    """
    Colours the data within the paraview view.

    This function takes the datapoints within the paraview client and colours them
    accordingly based on parameters below. This is a more specific colouring tool than
    within the clipping function.

    This sets the points coloured in the paraview view to the specifications given as
    well as a printed statement confirming it's finished. (primarily a debugging tool)

    Parameters
    ==========
    points
        The datapoints imported in the paraview client you want to colour
    ScalarName: str
        The name of the variable you would like clip with e.g "Temp"
    Range: Tuple[float, float]
        The range over which the colour scale will be set. E.g ColourRange = (0,0.2)
    Preset: str, default is "Inferno (matplotlib)"
        The name of a colour preset palette in Paraview.

    Returns
    =======
    None
    """
    SetDisplayProperties(ColorArrayName=ScalarName)
    display = Show(points)

    ColorBy(display, ("POINTS", ScalarName))

    ColourMap = GetColorTransferFunction(ScalarName)
    ColourMap.RescaleTransferFunction(Range)
    # You can change colour preset here ###
    ColourMap.ApplyPreset(Preset, True)
    print("Coloured data")


# A function to saved the clipped data if you want to use it later on


def savedata(filepath):
    """
    Saves the data

    Performs the SaveData function within paraview, saving the data currently in the
    active view to the desired filepath, and prints a statement saying the data had been
    saved (Mostly a debugging tool).

    Parameters
    ==========
    filepath: str
        The filepath you would like to save the data too

    Returns
    =======
    None
    """
    SaveData(filepath)
    print("Saved Data")


# Saves the screenshot of the current view


def ScreenShot(filepath, Position=None, Resolution=None):
    """
    Saves a frame displaying the current data.

    Takes the current active data/view within the paraview client and frames it from a
    position and then saves the screenshot to the desired filepath with a given
    resolution. Prints that the screenshot has been saved.

    Parameters
    ==========
    filepath: str
        The filepath you would like to save the screenshot to.
    Position: Optional[List[int]]
        The position within the space in x,y,z coordinates to take the screenshot from
        within the paraview view space. If not set, the default position will be
        [1000,800,800].
    Resolution: Optional[List[int]]
        The wanted resolution of the saved image. If not set, the default resolution
        will be [1500,1500].

    Returns
    =======
    None
    """
    if Position is None:
        Position = [1000, 800, 800]

    if Resolution is None:
        Resolution = [1500, 1500]

    myview = GetActiveView()
    myview.CameraPosition = Position
    myview.CameraViewUp = [0, 0, 1]

    SaveScreenshot(filepath + ".png", myview, ImageResolution=Resolution)

    print("Saved Screenshot")


# Connects all the other functions into one


def CrystalVis(reader, ShotPath, ScalarName, opacity=0.05, ScalarVal=0.15):
    """
    This is just a combination function

    This function takes in all previous functions and combines them

    Parameters
    ==========
    reader
        This is the data within the paraview client you are acting on. This will have
        been loaded in with a reader.
    ShotPath: str
        This is the filepath you wish to save your screenshots to.
    Scalarname: str
        The name of the scalar you want to clip your data by. (e.g temp, rho)
    Opacity: float, default is 0.05
        The opacity by which you want to show the data at if you wish to stack multiple
        data points together.

    Returns
    =======
    None
    """
    # TODO needs better description in the docs
    points = PointsView(reader)
    print()
    MaxColour(points, ScalarName)
    print()
    MaxClip(points, ScalarVal, ScalarName, opacity)

    ScreenShot(ShotPath)


# A final function to create an amount of frames specified


def FrameCreation(
    data_dir, output_dir, ScalarName, opacity=0.05, ScalarVal=0.15, n_frames=None
):
    """Converts 3D datasets to frames

    Obtains 3D datasets in .CSV format and converts them into frames by putting them
    into a paraview project and outputting frames of the data in PNG format.

    Parameters
    ==========
    data_dir: Path
        Directory containing your data in .CSV format.
    output_dir: Path
        Directory to save screenshots to.
    ScalarName: str
        The scalar you would like to act on to create your frames
    Opacity: float, default is 0.05
        Allows you to set an opacity for your data.
    n_frames: Optional[int]
        Allows you to specifiy how many frames of data you would like to create. If not
        specified, all frames will be used.

    Returns
    =======
    None
    """
    filenames = [f.name for f in data_dir.iterdir() if f.is_file()]
    filenames.sort()

    if n_frames is None:
        n_frames = len(filenames)

    for filename in filenames[:n_frames]:
        print(filename)
        # This reads the file into the code
        reader = OpenDataFile(str(data_dir / filename))
        # This processes the data arrays within the vtk file, allowing them to be
        # processed
        reader.GetPointDataInformation()
        # This is a compound function that takes all of the mini functions and processes
        # it all here
        CrystalVis(
            reader,
            str(output_dir / filename),
            ScalarName,
            opacity=opacity,
            ScalarVal=ScalarVal,
        )

        ResetSession()


if __name__ == "__main__":
    # Files originally specified in this script:
    # mypath = "/home/user/Desktop/Data/Max Data/ConvertedData/"
    # finalShotPath =
    #   "/home/user/Desktop/Data/Max Data/ConvertedData/DataAndScreenshots/Screenshots/"

    # Define command line interface for this script
    parser = argparse.ArgumentParser(
        prog="SciViPy.crystal_vis_script",
        description=(
            dedent(
                """\
                Takes simulated materials data which has been converted to a paraview
                readable format (See xyz_to_csv.py) and performs the relevant
                visualisation methods in order to produce a visualisation of interesting
                properties.
                """
            )
        ),
    )

    parser.add_argument(
        "data_dir",
        help="Path to directory containing .csv",
        type=Path,
    )

    parser.add_argument(
        "-o",
        "--output",
        help="The directory where you want your stills/frames to be saved.",
        type=Path,
    )

    parser.add_argument(
        "--scalar_name",
        help="The name of the scalar you would like to see in your .csv file.",
        type=str,
        default="Strain Scaling Factor",
    )

    parser.add_argument(
        "--scalar_val",
        help=(
            "The value you would like to do the scalar clip from. "
            "Only values above this will be shown."
        ),
        type=float,
        default=0.15,
    )

    parser.add_argument(
        "--n_frames",
        help=(
            "The number of frames you would like. "
            "By default uses all files in data_dir."
        ),
        type=int,
    )

    parser.add_argument(
        "--opacity",
        help="Controls opacity of the plots produced.",
        type=float,
        default=0.05,
    )

    # Get inputs/outputs from the command line
    args = parser.parse_args()

    # Check that input/output dirs are valid
    if not args.data_dir.is_dir():
        raise NotADirectoryError(args.data_dir)

    if args.output is None:
        output = args.data_dir / "DataAndScreenshots" / "Screenshots"
    else:
        output = args.output
    output.mkdir(parents=True, exist_ok=True)

    # Run
    FrameCreation(
        args.data_dir,
        output,
        ScalarName=args.scalar_name,
        ScalarVal=args.scalar_val,
        opacity=args.opacity,
        n_frames=args.n_frames,
    )
