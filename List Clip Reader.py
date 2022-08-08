from paraview.simple import *
from paraview.servermanager import * #MAKE SURE TO INCLUDE THIS MODULE WHEN LOADING VTK FILES!!!!!!!!!!!!
import vtk



textfile = open("/home/user/Desktop/Data/JOREK_data/150 steps.txt","r")

datapoints = []

ScalarVal = 0.00025



for x in textfile:
    lines = x
    stripnewline = x.rstrip()
    datapoints.append(stripnewline)
print(datapoints) 
noofpoints = len(datapoints)

for i in range(0, 150, 20):
    CurrentVal = datapoints[i]
    StringVal = str(CurrentVal)

    #Currentfile = "/home/user/Desktop/Data/JOREK_data/jorek0"+StringVal+".vtk"    
    Currentfile = "/media/user/Storage1/JOREK_data/jorek0"+StringVal+".vtk"   
    print(Currentfile)
    reader = OpenDataFile(Currentfile) #This reads the file into the code
    reader.GetPointDataInformation() #This processes the data arrays within the vtk file, allowing them to be processed

    if reader:
        
        print("success, current iteration is "+str(i)) #Ensures file has been read successfully 
    else:
        print("failed")
    #Applies the scalar clip #
     
    clip=Clip(Input=reader)
    # print(clip.ListProperties)
    clip.ClipType = 'Scalar'    
    clip.Scalars =('POINTS','D_alpha')
    clip.Value = ScalarVal
    clip.Invert = False


    #Once the clip has been applied, this edits the visuals of it
    SetDisplayProperties(Opacity=0.5)
    SetDisplayProperties(ColorArrayName='Te') 
    display = Show(clip)
    ColorBy(display, ('POINTS', 'Te'))
    display.RescaleTransferFunctionToDataRange(True)

    #Saves the Screenshot by setting up a camera position for the active view
    # myview = GetActiveView()
    # myview.CameraPosition = [12, 0, 0]
    # myview.CameraViewUp = [0, 0, 1]    

    # SaveScreenshot("JOREK_"+StringVal+".png", myview,
    #     ImageResolution=[1500, 1500])
    
    # Saves the state file #

    # SaveState("jorek"+StringVal+".pvsm")

    # Saves the Data from the specific clip #

    SaveData("/home/user/Desktop/Data/JOREK_DATA 2.0/jorek "+str(ScalarVal)+" " + StringVal  + ".vtk", proxy=clip,)

    ResetSession()


textfile.close()