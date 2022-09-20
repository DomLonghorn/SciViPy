from paraview.simple import *
from paraview.servermanager import * #MAKE SURE TO INCLUDE THIS MODULE WHEN LOADING VTK FILES!!!!!!!!!!!!
import vtk



textfile = open("/home/user/Desktop/Data/JOREK_data/150 steps.txt","r")

datapoints = []

StanScalarVal = 0.0001
MaxScalarVal = -0.02



def StanClip(reader,ScaVal):
    clip=Clip(Input=reader)
        
    clip.ClipType = 'Scalar'    
    clip.Scalars =('points','D_alpha')
    clip.Value = ScaVal
    clip.Invert = False


    #Once the clip has been applied, this edits the visuals of it
    SetDisplayProperties(Opacity=0.5)
    SetDisplayProperties(ColorArrayName='Te') 
    display = Show(clip)
    ColorBy(display, ('POINTS', 'Te'))
    display.RescaleTransferFunctionToDataRange(True)



#Saves the Screenshot by setting up a camera position for the active view
def StanScreenShot(StrVal):
    
    myview = GetActiveView()
    myview.CameraPosition = [12, 0, 0]
    myview.CameraViewUp = [0, 0, 1]    

    SaveScreenshot("JOREK_"+StrVal+".png", myview,
        ImageResolution=[1500, 1500])
def StanSaveState(StrVal):    
   # Saves the state file #

    SaveState("jorek"+StrVal+".pvsm")

#Saves the Data from the specific clip #
def StanSaveData(ScaVal,StringVal):
    SaveData("/home/user/Desktop/Data/JOREK_DATA 2.0/Mos 2.0/jorek"+str(ScaVal)+"" + StringVal  + ".vtk", proxy=None,)


def Stan(Reader,ScaVal,StrVal):
    StanClip(Reader,StrVal)
    StanScreenShot(StrVal)
    StanSaveState(StrVal)
    SaveData(StrVal,ScaVal)


def FindDataPoints(textfile):
    for x in textfile:
        stripnewline = x.rstrip()
        datapoints.append(stripnewline)
    return datapoints
    
FindDataPoints(textfile)


noofpoints = len(datapoints)
print(noofpoints)
for i in range(0,150,10):
    CurrentVal = datapoints[i]
    StringVal = str(CurrentVal)
    Currentfile = "/media/user/Storage1/JOREK_data/jorek0"+StringVal+".vtk"   
 
    
    
    # print(Currentfile)
    reader = OpenDataFile(Currentfile) #This reads the file into the code
    reader.GetPointDataInformation() #This processes the data arrays within the vtk file, allowing them to be processed

    if reader:
        print("success")
    else:
        print("failed")

    StanClip(reader,StanScalarVal)
    # StanScreenShot(StringVal)
    # StanSaveState(StringVal)
    # print(StanScalarVal,StringVal)

    StanSaveData(StanScalarVal,StringVal)
    
    #Stan(reader,StanScalarVal,StringVal)

    ResetSession()
    

    

textfile.close()
