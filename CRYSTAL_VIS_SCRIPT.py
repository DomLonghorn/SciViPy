from paraview.simple import *
from paraview.servermanager import * #MAKE SURE TO INCLUDE THIS MODULE WHEN LOADING VTK FILES!!!!!!!!!!!!
from os import listdir
from os.path import isfile, join
import glob
# import imageio ###Figure out how to get paraview to recognise ImageIO so it can make GIFs all in one code ###

mypath = "/home/user/Desktop/Data/Max Data/ConvertedData/"
MaxScalarVal = 0.15


filepaths = []
datapoints = []
finalDataPath = []
finalShotPath = []
finalStatePath = []
finalFilePath = []
imagesList = []


def MaxClip(reader, ScaVal):
    
    SetDisplayProperties(Opacity=0.011)
    clip=Clip(Input=reader)
        
    clip.ClipType = 'Scalar'    
    clip.Scalars =("POINTS",'Strain Scaling Factor')
    clip.Value = ScaVal
    clip.Invert = False

    display = Show(clip)

    ColourMap = GetColorTransferFunction('Strain Scaling Factor')
    SetDisplayProperties(ColorArrayName='Strain Scaling Factor') 
    ColorBy(display, ('POINTS', 'Strain Scaling Factor'))
    ColourMap.RescaleTransferFunction(0, 0.2)

    return clip
    
def PointsView(reader):    
    TableToPoints(Input=reader,XColumn="X Position",YColumn="Y Position",ZColumn="Z Position")
    
    return print("Interpolated to points")

def MaxColour(points):
    LoadPalette("Black-Body Radiation")
    SetDisplayProperties(ColorArrayName='Strain Scaling Factor') 
    display = Show(points)
    
    ColorBy(display, ('POINTS', 'Strain Scaling Factor'))

    ColourMap = GetColorTransferFunction('Strain Scaling Factor')
    ColourMap.RescaleTransferFunction(0, 0.2)
    ColourMap.ApplyPreset("Inferno (matplotlib)",True)
    return print("Coloured data")
    
def savedata(filepath):
    SaveData(filepath+"Data/")

    return print("Saved Data")

def ScreenShot(filepath):
    myview = GetActiveView()
    myview.CameraPosition = [1000, 800, 800]
    myview.CameraViewUp = [0, 0, 1]    
    
    SaveScreenshot(filepath+".png", myview,ImageResolution=[1500, 1500])
    

    return print("Saved Screenshot")

# def Maxsavestate(filepath):   
#     SaveState(filepath+".pvsm")

def CrystalVis(reader,DataPath,ShotPath):
    points = PointsView(reader)
    MaxColour(points)
    MaxClip(points,MaxScalarVal)
    #savedata(DataPath[i]+".csv")
    ScreenShot(ShotPath[i])


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.sort()

for i in range(len(onlyfiles)):
    filepaths.append(onlyfiles[i][0:-4])



for i in range(len(filepaths)):
    finalFilePath.append(mypath + "/DataAndScreenshots/"+onlyfiles[i])
    finalDataPath.append(mypath + "/DataAndScreenshots/Data/"+onlyfiles[i])
    finalShotPath.append(mypath + "/DataAndScreenshots/Screenshots/"+onlyfiles[i])
    finalStatePath.append(mypath + "/DataAndScreenshots/States/"+onlyfiles[i])

# len(onlyfiles)
for i in range(len(onlyfiles)):
    Currentfile = mypath + onlyfiles[i]
    print("Current iteration and file:"+str([i])+" - " + Currentfile)
    reader = OpenDataFile(Currentfile) #This reads the file into the code
    reader.GetPointDataInformation() #This processes the data arrays within the vtk file, allowing them to be processed
    
    CrystalVis(reader,finalDataPath,finalShotPath) # This is a compound function that takes all of the mini functions and processes it all here

    ResetSession()
    ### 100 frames takes about 18 mins to process for the Max converted data set (85.3 Mbs each) ###


PNG_dir = mypath + "/DataAndScreenshots/Screenshots"
 

# for images in glob.iglob(f'{folder_dir}/*'):
   
#     # check if the image ends with png
#     if (images.endswith(".png")):
#         imagesList.append(images)
#         print(images)
# imagesList.sort()

# with imageio.get_writer(PNG_dir + '/CrystalGif.gif', mode='I') as writer:
#     for filename in imagesList:
#         image = imageio.imread(filename)
#         writer.append_data(image)
