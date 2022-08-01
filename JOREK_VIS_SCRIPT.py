from paraview.simple import *
from paraview.servermanager import * #MAKE SURE TO INCLUDE THIS MODULE WHEN LOADING VTK FILES!!!!!!!!!!!!
import vtk


InitialVal = 10000 #Initial numerical value for data entry


for i in range(10):
    additive = i * 10 #All files are an addition of 10 on the previous file
    CurrentVal = InitialVal + additive
    StringVal = str(CurrentVal) #Converted to a string to allow file reading
    
    Currentfile = "/home/user/Desktop/JOREK_data/MAST-U_processed_v2/jorek"+StringVal+".vtk"    
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
    clip.Invert = False


    #Once the clip has been applied, this edits the visuals of it
    SetDisplayProperties(Opacity=0.5)
    SetDisplayProperties(ColorArrayName='Te') 
    display = Show(clip)
    ColorBy(display, ('POINTS', 'Te'))
    display.RescaleTransferFunctionToDataRange(True)

    #Saves the file
    
    SaveState("jorek"+StringVal+".pvsm")
    ResetSession()