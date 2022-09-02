# from paraview.simple import *
# from paraview.servermanager import * #MAKE SURE TO INCLUDE THIS MODULE WHEN LOADING VTK FILES!!!!!!!!!!!!
from os import listdir
from os.path import isfile, join



mypath = "/home/user/Desktop/Data/Max Data/ConvertedData/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

filepaths = []

for i in range(len(onlyfiles)):
    filepaths.append(onlyfiles[i][0:-4])
print(filepaths)
    


datapoints = []

MaxScalarVal = -0.02


def MaxClip(reader, ScaVal):
    points=TableToPoints(Input=reader,XColumn="X Position",YColumn="Y Position",ZColumn="Z Position")
    SetDisplayProperties(Opacity=0.01)
    clip=Clip(Input=points)
        
    clip.ClipType = 'Scalar'    
    clip.Scalars =("POINTS",'Strain Scaling Factor')
    clip.Value = ScaVal
    clip.Invert = True

    SetDisplayProperties(ColorArrayName='Strain Scaling Factor') 
    display = Show(clip)
    ColorBy(display, ('POINTS', 'Strain Scaling Factor'))
    display.RescaleTransferFunctionToDataRange(True)
    return clip


def savedata(filepath):
    SaveData(filepath)

def ScreenShot(filepath):
    
    myview = GetActiveView()
    myview.CameraPosition = [12, 0, 0]
    myview.CameraViewUp = [0, 0, 1]    

    SaveScreenshot(filepath+".png", myview,ImageResolution=[1500, 1500])


# def Maxsavestate(filepath):   
#     SaveState(filepath+".pvsm")


finalFilePath = []
for i in range(len(filepaths)):
    finalFilePath.append(mypath + "/DataAndScreenshots/"+filepaths[i])



for i in range(1):   
    Currentfile = mypath + onlyfiles[i]
    print(Currentfile)
    reader = OpenDataFile(Currentfile) #This reads the file into the code
    reader.GetPointDataInformation() #This processes the data arrays within the vtk file, allowing them to be processed

    MaxClip(reader,MaxScalarVal)
    savedata(finalFilePath[i]+".csv")
    ScreenShot(finalFilePath[i])
    # SaveState(finalFilePath[i]+".pvsm")
    # ResetSession()


