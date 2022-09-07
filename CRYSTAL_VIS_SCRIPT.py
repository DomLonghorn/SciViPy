from paraview.simple import *
from paraview.servermanager import * #MAKE SURE TO INCLUDE THIS MODULE WHEN LOADING VTK FILES!!!!!!!!!!!!
from os import listdir
from os.path import isfile, join


mypath = "/home/user/Desktop/Data/Max Data/ConvertedData/"    #The directory you want to create stills from

finalShotPath = "/home/user/Desktop/Data/Max Data/ConvertedData/DataAndScreenshots/Screenshots/" # The directory where you want your Stills/Frames to be saved


MaxScalarVal = 0.15 #The value you would like to do the scalar clip from. i.e Only values above this value will be shown.

### Creating empty lists ###
filepaths = []
datapoints = []
finalDataPath = []
finalStatePath = []
finalFilePath = []
imagesList = []

### Defines the standard clip used to show "extreme" or interesting parts of the data###


def MaxClip(reader, ScaVal, opacity=0.05, Range = (0, 0.2)):
    
    SetDisplayProperties(Opacity=opacity)
    clip=Clip(Input=reader)
        
    clip.ClipType = 'Scalar'    
    clip.Scalars =("POINTS",'Strain Scaling Factor')
    clip.Value = ScaVal
    clip.Invert = False

    display = Show(clip)

    ColourMap = GetColorTransferFunction('Strain Scaling Factor')
    SetDisplayProperties(ColorArrayName='Strain Scaling Factor') 
    ColorBy(display, ('POINTS', 'Strain Scaling Factor'))
    ColourMap.RescaleTransferFunction(Range)

    return clip
### Turns the .CSV to actual points to be seen ###   
def PointsView(reader):    
    TableToPoints(Input=reader,XColumn="X Position",YColumn="Y Position",ZColumn="Z Position")
    
    return print("Interpolated to points")

### Colours the points based on a set range ###

def MaxColour(points, Range = (0, 0.2)):
    LoadPalette("Black-Body Radiation")
    SetDisplayProperties(ColorArrayName='Strain Scaling Factor') 
    display = Show(points)
    
    ColorBy(display, ('POINTS', 'Strain Scaling Factor'))

    ColourMap = GetColorTransferFunction('Strain Scaling Factor')
    ColourMap.RescaleTransferFunction(Range)
    ColourMap.ApplyPreset("Inferno (matplotlib)",True)
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
    
    SaveScreenshot(filepath+".png", myview,ImageResolution=[1500, 1500])
    

    return print("Saved Screenshot")


### Connects all the other functions into one ###
def CrystalVis(reader,ShotPath,opacity=0.05):
    points = PointsView(reader)
    print()
    MaxColour(points)
    print()
    MaxClip(points,MaxScalarVal,opacity)

    ScreenShot(ShotPath)

### Adds all the files in the directory into a list and sorts it so it appears in numerical order ###
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.sort()


### A final function to create an amount of frames specified
def FrameCreation(NoOfFrames,File,FilePathForScreenshot,opacity=0.05):
    for i in range(NoOfFrames): #This shows how many 
        #print("Current iteration and file:"+str([i])+" - " + File[i])
        print(File[i])
        reader = OpenDataFile(mypath + File[i]) #This reads the file into the code
        reader.GetPointDataInformation() #This processes the data arrays within the vtk file, allowing them to be processed
        print(FilePathForScreenshot)
        CrystalVis(reader,FilePathForScreenshot+File[i],opacity) # This is a compound function that takes all of the mini functions and processes it all here

        ResetSession()
        ### 100 frames takes about 18 mins to process for the Max converted data set (85.3 Mbs each) ###


FrameCreation((3),(onlyfiles),finalShotPath,opacity=0.05)


