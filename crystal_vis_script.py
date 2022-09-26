from paraview.simple import *
# MAKE SURE TO INCLUDE THIS MODULE WHEN LOADING VTK FILES!!!!!!!!!!!!
from paraview.servermanager import *
from os import listdir
from os.path import isfile, join


# The directory you want to create stills from
mypath = "/home/user/Desktop/Data/Max Data/ConvertedData/"
# Sorts through your directory to create a list of all of the files
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.sort()
# The directory where you want your Stills/Frames to be saved
finalShotPath = "/home/user/Desktop/Data/Max Data/ConvertedData/DataAndScreenshots/Screenshots/"

# This is the name of the scalar you would like to see in your .CSV file
ScalarName = "Strain Scaling Factor"

# The value you would like to do the scalar clip from. i.e Only values above this value will be shown.
MaxScalarVal = 0.15

# Number of frames you would like. This default does all of them in the directory, in order
NoOfFrames = len(onlyfiles)
### Creating empty lists ###
filepaths = []
datapoints = []
finalDataPath = []
finalStatePath = []
finalFilePath = []
imagesList = []

### Defines the standard clip used to show "extreme" or interesting parts of the data###


def MaxClip(reader, ScaVal, ScalarName, opacity=0.05, Range=(0, 0.2)):

    SetDisplayProperties(Opacity=opacity)
    clip = Clip(Input=reader)

    clip.ClipType = 'Scalar'
    clip.Scalars = ("POINTS", ScalarName)
    clip.Value = ScaVal
    clip.Invert = False

    display = Show(clip)

    ColourMap = GetColorTransferFunction(ScalarName)
    SetDisplayProperties(ColorArrayName=ScalarName)
    ColorBy(display, ('POINTS', ScalarName))
    ColourMap.RescaleTransferFunction(Range)

    return clip
### Turns the .CSV to actual points to be seen ###


def PointsView(reader):
    TableToPoints(Input=reader, XColumn="X Position",
                  YColumn="Y Position", ZColumn="Z Position")

    return print("Interpolated to points")

### Colours the points based on a set range ###
#                       ###


def MaxColour(points, ScalarName, Range=(0, 0.2)):
    SetDisplayProperties(ColorArrayName=ScalarName)
    display = Show(points)

    ColorBy(display, ('POINTS', ScalarName))

    ColourMap = GetColorTransferFunction(ScalarName)
    ColourMap.RescaleTransferFunction(Range)
    # You can change colour preset here ###
    ColourMap.ApplyPreset("Inferno (matplotlib)", True)
    return print("Coloured data")

### A function to saved the clipped data if you want to use it later on ###


def savedata(filepath):
    SaveData(filepath)

    return print("Saved Data")


### Saves the screenshot of the current view ###
def ScreenShot(filepath):
    myview = GetActiveView()
    myview.CameraPosition = [1000, 800, 800]
    myview.CameraViewUp = [0, 0, 1]

    SaveScreenshot(filepath+".png", myview, ImageResolution=[1500, 1500])

    return print("Saved Screenshot")


### Connects all the other functions into one ###
def CrystalVis(reader, ShotPath, ScalarName, opacity=0.05):
    points = PointsView(reader)
    print()
    MaxColour(points, ScalarName)
    print()
    MaxClip(points, MaxScalarVal, ScalarName, opacity)

    ScreenShot(ShotPath)

### Adds all the files in the directory into a list and sorts it so it appears in numerical order ###


# A final function to create an amount of frames specified
def FrameCreation(, File, FilePathForScreenshot, ScalarName,NoOfFrames=len(onlyfiles), opacity=0.05):
    for i in range(NoOfFrames):  # This shows how many
        print(File[i])
        # This reads the file into the code
        reader = OpenDataFile(mypath + File[i])
        # This processes the data arrays within the vtk file, allowing them to be processed
        reader.GetPointDataInformation()
        print(FilePathForScreenshot)
        # This is a compound function that takes all of the mini functions and processes it all here
        CrystalVis(reader, FilePathForScreenshot+File[i], ScalarName, opacity)

        ResetSession()
        ### 100 frames takes about 18 mins to process for the Max converted data set (85.3 Mbs each) ###


FrameCreation((NoOfFrames), (onlyfiles), finalShotPath, ScalarName)
