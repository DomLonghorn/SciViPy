
from paraview.simple import *
# MAKE SURE TO INCLUDE THIS MODULE WHEN LOADING VTK FILES!!!!!!!!!!!!
from paraview.servermanager import *
import vtk
from os import listdir
from os.path import isfile, join


mypath = "C:\\Users\\FWKCa\\OneDrive\\Desktop\\Internship stuff\\Jorek Data\\"

# Sorts through your directory to create a list of all of the files
datapoints = [f for f in listdir(mypath) if isfile(join(mypath, f))]
datapoints.sort()

# The directory where you want your Stills/Frames to be saved
finalShotPath = "C:\\Users\\FWKCa\\OneDrive\\Desktop\\Internship stuff\\Screenshot\\"

NoOfFrames = len(datapoints)

ScalarToClip = "D_alpha"
ScalarToColourBy = "Te"


StanScalarVal = 0.0001


def ScalarClip(reader, ScaVal, opacity=0.5, ColourBy='Te'):
    "#Once the clip has been applied, this edits the visuals of it"

    clip = Clip(Input=reader)
    clip.ClipType = 'Scalar'
    clip.Scalars = ('points', 'D_alpha')
    clip.Value = ScaVal
    clip.Invert = False
    SetDisplayProperties(Opacity=opacity)
    SetDisplayProperties(ColorArrayName=ColourBy)
    display = Show(clip)
    ColorBy(display, ('POINTS', ColourBy))
    display.RescaleTransferFunctionToDataRange(True)

    return print("Clipped")


def StanScreenShot(FilePath, CameraPosition=[12, 0, 0]):
    "Saves the Screenshot by setting up a camera position for the active view"

    myview = GetActiveView()
    myview.CameraPosition = CameraPosition
    myview.CameraViewUp = [0, 0, 1]

    SaveScreenshot(FilePath+".png", myview, ImageResolution=[1500, 1500])
    return print("Screenshotted")


def StanSaveState(FilePath):
    "Saves the state file"
    SaveState(FilePath+".pvsm")

#Saves the Data from the specific clip #


def StanSaveData(FilePath):
    "Saves the Data from the specific clip"
    SaveData(FilePath + ".vtk", proxy=None,)


def Stan(Reader, FilePath):
    StanClip(Reader, FilePath)
    StanScreenShot(FilePath)
    StanSaveState(FilePath)
    SaveData(FilePath)


for i in range(1, 5):
    CurrentFile = mypath + datapoints[i]

    reader = OpenDataFile(CurrentFile)  # This reads the file into the code
    # This processes the data arrays within the vtk file, allowing them to be processed
    reader.GetPointDataInformation()

    CADreader = OpenDataFile(
        "C:\\Users\\FWKCa\\OneDrive\\Desktop\\Internship stuff\\Orientated Mast Model.obj")
    CADreader.GetPointDataInformation()
    display = Show(CADreader)
    if reader:
        print("success")
    else:
        print("failed")

    ScalarClip(reader, StanScalarVal)

    StanScreenShot(finalShotPath+datapoints[i])

    print("Session finished")

    ResetSession()
