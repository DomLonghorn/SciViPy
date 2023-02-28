""" Script which takes in large 3D datasets from Jorek simulations in .VTK format and exports .png frames of them for further visualisation.

    This script, when run in a paraview shell, will take a collection of data points in .VTK format and produce frames of them
    clipped to a certain scalar value (i.e showing only a certain set of values). The script also allows for the customisation of
    colourisation towards a set of scalar values (E.g Temperature) when set at the beginning. Finally, this also allows for the addition of
    a CAD model to the screenshot to be shown alongside.
    (See README image)

    Lisence: MPL-2.0 

"""

from paraview.simple import *
from paraview.servermanager import *
import vtk
from os import listdir
from os.path import isfile, join


mypath = (
    "C:\\Users\\FWKCa\\OneDrive\\Desktop\\Internship stuff\\Jorek Data\\Stan new data\\"
)

CAD_path = (
    "C:\\Users\\FWKCa\\OneDrive\\Desktop\\Internship stuff\\Orientated Mast Model.obj"
)

# Sorts through your directory to create a list of all of the files
datapoints = [f for f in listdir(mypath) if isfile(join(mypath, f))]
datapoints.sort()

# The directory where you want your Stills/Frames to be saved
finalShotPath = "C:\\Users\\FWKCa\\OneDrive\\Desktop\\Internship stuff\\Screenshot\\"

NoOfFrames = len(datapoints)

ScalarToClip = "custom"
ScalarToColourBy = "rho"


StanScalarVal = 1.5916


def ScalarClip(reader, Scalar, ScaVal, ColourBy, opacity=0.5):
    """This performs the clip within the data, deciding how to show the data.

    Loads in the data file and then performs a clip based on the scalar value provided along with a value by which to use
    as its cut off point, displaying only the desired parts of the data. This can also change the colour based on another scarlar value
    as well as change the opacity of the shown data if multiple data points would like to be shown at the same time.

    Args:
        reader: This is the data fed into the function to be clipped and shown
        Scalar: This is the name of the scalar, written as a string, to be clipped by.
        ScaVal: This is the numerical value of the scalar to use as the clipping value, either clipping above or below this value.
        ColourBy:   Name of the scalar to display as a colour map on top of the clipped data.
        Opacity:    Argument to allow the change of the opacity of the final clipped data points.

    Returns:
        This function returns a clipped set of data into the paraview client as the primary focused data.
    """

    clip = Clip(Input=reader)
    clip.ClipType = "Scalar"
    clip.Scalars = ("points", Scalar)
    clip.Value = ScaVal
    clip.Invert = False
    SetDisplayProperties(Opacity=0.5)
    SetDisplayProperties(ColorArrayName=ColourBy)
    display = Show(clip)
    ColorBy(display, ("POINTS", ColourBy))
    display.RescaleTransferFunctionToDataRange(True)

    return display


def StanScreenShot(FilePath, CameraPosition=[20, 0, 0]):
    """Saves the Screenshot by setting up a camera position for the active view

        Takes a screenshot of the current displayed data at a desired postition within the paraview client window ]
        and then saves it to the desired file path specified.

    Args:
        FilePath:   File path to save the screenshot to
        CameraPosition: Position within the paraview client to take the screenshot, forward facing, from. (Default: (-15,0,0) as this was our
        best testing angle. Testing is usually required to find optimum position)

    Returns:
        Returns a saved screenshot of the desired data into the filepath specified.
    """
    myview = GetActiveView()
    myview.CameraPosition = CameraPosition
    myview.CameraViewUp = [0, 0, 1]

    SaveScreenshot(FilePath + ".png", myview, ImageResolution=[1500, 1500])
    return print("Screenshotted")


def StanSaveState(FilePath):
    """Saves the state file

    This function saves the paraview state file to a desired directory. This can then be used to reload the same state if needed later for testing

    Args:
        FilePath:   Desired filepath to save the paraview state to

    """
    SaveState(FilePath + ".pvsm")


# Saves the Data from the specific clip #


def StanSaveData(FilePath):
    """Saves the Data from the specific clip

    Saves the data currently in the active view into a seperate .VTK file. This allows for the manipulation of clipped data in the future which
    may cut down on computing time.

    Args:
        Filepath:   Desired saving location for the data.
    """
    SaveData(
        FilePath + ".vtk",
        proxy=None,
    )


def StanShowCAD(FilePath):
    """Shows a CAD model with

    Saves the data currently in the active view into a seperate .VTK file. This allows for the manipulation of clipped data in the future which
    may cut down on computing time.

    Args:
        Filepath:   Desired saving location for the data.

    Returns:
        A displayed CAD model within the Paraview client display
    """

    CADreader = OpenDataFile(FilePath)
    CADreader.GetPointDataInformation()
    print("Showing CAD")
    Show(CADreader)


def Stan(Reader, FilePath):
    """Combines many functions into one for ease of use"""
    ScalarClip(Reader, FilePath)
    StanScreenShot(FilePath)
    StanSaveState(FilePath)
    StanSaveData(FilePath)


def VisualisationScript(
    filepath, Scalar, ScaVal, ColourBy, ShotPath, Opacity=0.5, Reset=True
):
    """This script combines ScalarClip and StanScreenShot into one combined function

    This script combines ScalarClip and StanScreenShot to combine them into one function which allows for the entire
    Visualisation process in one easy function which is easy to run.

    Args:
        filepath: This is the filepath of the data you would like to visualise
        Scalar: (See ScalarClip)
        ScaVal: (See ScalarClip)
        ColourBy:   (See ScalarClip)
        ShotPath:   (See StanScreenShot documentation)

    Returns:
        A saved screenshot of your data.
    """
    print("loading file")
    reader = OpenDataFile(filepath)
    reader.GetPointDataInformation()
    print("Loading CAD")
    if reader:
        print("success")
    else:
        print("failed")
    display = ScalarClip(reader, Scalar, ScaVal, ColourBy, opacity=Opacity)
    StanScreenShot(ShotPath)
    print("Session finished")
    if Reset == True:
        ResetSession()


for i in range(len(datapoints)):
    Datapath = mypath + datapoints[i]
    ShotPath = finalShotPath + datapoints[i]
    VisualisationScript(
        Datapath, ScalarToClip, StanScalarVal, ScalarToColourBy, ShotPath, Reset=False
    )
