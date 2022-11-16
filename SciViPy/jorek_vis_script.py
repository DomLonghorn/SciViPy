import argparse
from textwrap import dedent
from pathlib import Path

from paraview.simple import *
from paraview.servermanager import *


def ScalarClip(reader, ScaVal, opacity=0.5, ColourBy="Te"):
    """Once the clip has been applied, this edits the visuals of it"""

    clip = Clip(Input=reader)
    clip.ClipType = "Scalar"
    clip.Scalars = ("points", "D_alpha")
    clip.Value = ScaVal
    clip.Invert = False
    SetDisplayProperties(Opacity=opacity)
    SetDisplayProperties(ColorArrayName=ColourBy)
    display = Show(clip)
    ColorBy(display, ("POINTS", ColourBy))
    display.RescaleTransferFunctionToDataRange(True)

    return display


def StanScreenShot(FilePath, CameraPosition=[12, 0, 0]):
    """Saves the Screenshot by setting up a camera position for the active view"""

    myview = GetActiveView()
    myview.CameraPosition = CameraPosition
    myview.CameraViewUp = [0, 0, 1]

    SaveScreenshot(FilePath + ".png", myview, ImageResolution=[1500, 1500])
    return print("Screenshotted")


def StanSaveState(FilePath):
    """Saves the state file"""
    SaveState(FilePath + ".pvsm")


# Saves the Data from the specific clip #


def StanSaveData(FilePath):
    """Saves the Data from the specific clip"""
    SaveData(
        FilePath + ".vtk",
        proxy=None,
    )


def Stan(Reader, FilePath):
    StanClip(Reader, FilePath)
    StanScreenShot(FilePath)
    StanSaveState(FilePath)
    SaveData(FilePath)


if __name__ == "__main__":
    # Files originally specified in this script
    # mypath = r"C:\Users\FWKCa\OneDrive\Desktop\Internship stuff\Jorek Data\"
    # CAD_path = (
    #     r"C:\Users\FWKCa\OneDrive\Desktop\Internship stuff\Orientated Mast Model.obj"
    # )
    # finalShotPath = r"C:\Users\FWKCa\OneDrive\Desktop\Internship stuff\Screenshot\"

    parser = argparse.ArgumentParser(
        prog="SciViPy.jorek_vis_script",
        description=(
            dedent(
                """\
                Takes already simulated data produced using JOREK code and automates the
                paraview visualisation process. There are parameters within the code
                that can be changed in order to modify the resulting output files.
                """
            )
        ),
    )

    parser.add_argument(
        "data_dir",
        help="Path to directory containing Jorek data.",
        type=Path,
    )

    # TODO Write help text
    parser.add_argument("cad_path", type=Path)

    parser.add_argument(
        "-o",
        "--output",
        help="The directory where you want your stills/frames to be saved.",
        type=Path,
    )

    # Get inputs/outputs from the command line
    args = parser.parse_args()

    # Check that input/output dirs are valid
    if not args.data_dir.is_dir():
        raise NotADirectoryError(args.data_dir)

    if not args.cad_path.is_file():
        raise FileNotFoundError(args.cad_path)

    if args.output is None:
        output = args.data_dir.parent / "Screenshot"
    else:
        output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    # Sorts through your directory to create a list of all of the files
    datapoints = [f.name for f in args.data_dir.iterdir() if f.is_file()]
    datapoints.sort()

    StanScalarVal = 0.0001

    for i in range(150):
        CurrentFile = str(args.data_dir / datapoints[i])
        print("loading file")
        reader = OpenDataFile(CurrentFile)  # This reads the file into the code
        # This processes the data arrays within the vtk file, allowing them to be
        # processed
        reader.GetPointDataInformation()
        print("Loading CAD")

        CADreader = OpenDataFile(str(args.cad_path))
        CADreader.GetPointDataInformation()
        print("Showing CAD")
        Show(CADreader)

        if reader:
            print("success")
        else:
            print("failed")

        display = ScalarClip(reader, StanScalarVal)

        StanScreenShot(str(output / datapoints[i]))
        print("Session finished")

        ResetSession()
