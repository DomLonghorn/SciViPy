
from paraview.simple import *
from paraview.servermanager import * #MAKE SURE TO INCLUDE THIS MODULE WHEN LOADING VTK FILES!!!!!!!!!!!!
import vtk
from os import listdir
from os.path import isfile, join


mypath = "C:\\Users\\FWKCa\\OneDrive\\Desktop\\Internship stuff\\Jorek Data\\"

datapoints = [f for f in listdir(mypath) if isfile(join(mypath, f))] #Sorts through your directory to create a list of all of the files
datapoints.sort()

finalShotPath = "C:\\Users\\FWKCa\\OneDrive\\Desktop\\Internship stuff\\Screenshot\\" # The directory where you want your Stills/Frames to be saved

NoOfFrames = len(datapoints)

ScalarToClip = "D_alpha"
ScalarToColourBy = "Te"


StanScalarVal = 0.0001

datapoints = []

def ScalarClip(reader,ScaVal,opacity=0.5,ColourBy = 'Te'):
    clip=Clip(Input=reader)  
    clip.ClipType = 'Scalar'    
    clip.Scalars =('points','D_alpha')
    clip.Value = ScaVal
    clip.Invert = False

    #Once the clip has been applied, this edits the visuals of it
    SetDisplayProperties(Opacity=opacity)
    SetDisplayProperties(ColorArrayName=ColourBy) 
    display = Show(clip)
    ColorBy(display, ('POINTS', ColourBy))
    display.RescaleTransferFunctionToDataRange(True)

    return print("Clipped")

#Saves the Screenshot by setting up a camera position for the active view
def StanScreenShot(FilePath,CameraPosition = [12,0,0]):
    myview = GetActiveView()
    myview.CameraPosition = CameraPosition
    myview.CameraViewUp = [0, 0, 1]    

    SaveScreenshot(FilePath+".png", myview, ImageResolution=[1500, 1500])
    return print("Screenshotted")
def StanSaveState(FilePath):    
   # Saves the state file #
   SaveState(FilePath+".pvsm")

#Saves the Data from the specific clip #
def StanSaveData(FilePath):
    SaveData(FilePath+ ".vtk", proxy=None,)

def Stan(Reader,FilePath):
    StanClip(Reader,FilePath)
    StanScreenShot(FilePath)
    StanSaveState(FilePath)
    SaveData(FilePath)

for i in range(0,3):
    CurrentFile = mypath + datapoints[i] 
    
    reader = OpenDataFile(Currentfile) #This reads the file into the code
    reader.GetPointDataInformation() #This processes the data arrays within the vtk file, allowing them to be processed

    if reader:
        print("success")
    else:
        print("failed")

    StanClip(reader,StanScalarVal)

    StanSaveData(StanScalarVal,StringVal)

    ResetSession()
textfile.close()