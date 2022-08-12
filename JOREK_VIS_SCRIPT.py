from paraview.simple import *
from paraview.servermanager import * #MAKE SURE TO INCLUDE THIS MODULE WHEN LOADING VTK FILES!!!!!!!!!!!!
import vtk



textfile = open("/home/user/Desktop/Data/JOREK_data/150 steps.txt","r")

datapoints = []

StanScalarVal = 0.00025
MaxScalarVal = -0.02



def StanClip(reader,ScaVal):
        clip=Clip(Input=reader)
        
        clip.ClipType = 'Scalar'    
        clip.Scalars =('POINTS','D_alpha')
        clip.Value = ScaVal
        clip.Invert = False


        #Once the clip has been applied, this edits the visuals of it
        SetDisplayProperties(Opacity=0.5)
        SetDisplayProperties(ColorArrayName='Te') 
        display = Show(clip)
        ColorBy(display, ('POINTS', 'Te'))
        display.RescaleTransferFunctionToDataRange(True)



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
def SaveData(StrVal,ScaVal):
    SaveData("/home/user/Desktop/Data/JOREK_DATA 2.0/jorek "+str(ScaVal)+" " + StrVal  + ".vtk", proxy=clip,)


def Stan(Reader,ScaVal,StrVal):
    StanClip(Reader,StrVal)
    ScreenShot(StrVal)
    SaveState(StrVal)
    SaveData(StrVal,ScaVal)


# for x in textfile:
#     lines = x
#     stripnewline = x.rstrip()
#     datapoints.append(stripnewline)
# print(datapoints) 
# noofpoints = len(datapoints)

# for i in range(0, 150, 20):
#     CurrentVal = datapoints[i]
#     StringVal = str(CurrentVal)
#     #Currentfile = "/media/user/Storage1/JOREK_data/jorek0"+StringVal+".vtk"   
    
    
    
Currentfile = "/home/user/Desktop/Data/Max Data/ConvertedData.csv"
   
print(Currentfile)
reader = OpenDataFile(Currentfile) #This reads the file into the code
reader.GetPointDataInformation() #This processes the data arrays within the vtk file, allowing them to be processed

if reader:
        
    # print("success, current iteration is "+str(i)) #Ensures file has been read successfully 
    print("success")
else:
    print("failed")
MaxClip(reader,MaxScalarVal)
     
    #Stan(reader,StanScalarVal,StringVal)

    #ResetSession()

textfile.close()