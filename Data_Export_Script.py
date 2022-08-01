from paraview.simple import *
from paraview.servermanager import * #MAKE SURE TO INCLUDE THIS MODULE WHEN LOADING VTK FILES!!!!!!!!!!!!
import vtk


InitialVal = 5030 #Initial numerical value for data entry


for i in range(1):
    additive = i * 10 #All files are an addition of 10 on the previous file
    CurrentVal = InitialVal + additive
    StringVal = str(CurrentVal) #Converted to a string to allow file reading
    Currentfile = "C:\\Users\\FWKCa\\OneDrive\\Desktop\\Test VTK Folder\\jorek07910.pvsm"
    #Currentfile = "/home/user/Desktop/JOREK_data/MAST-U_processed_v2/jorek0"+StringVal+".pvsm"    
    #reader = OpenDataFile(Currentfile) #This reads the file into the code
    #reader.GetPointDataInformation() #This processes the data arrays within the vtk file, allowing them to be processed
    reader = LoadState(Currentfile)
    #if reader:
        #print("success, current iteration is "+str(i)) #Ensures file has been read successfully 
    #else:
        #print("failed")
    #SaveData("/home/user/Desktop/JOREK_data/MAST-U_processed_v2/TESTjorek0"+StringVal+".vtk",proxy=None)
    SaveData("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Test VTK Folder\\jorel07910 - TestCopy.vtk")   
    
    #writer = CreateWriter("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Test VTK Folder\\TestSave2.vtk", reader)
    #writer.WriteAllTimeSteps = 1
    #writer.FieldAssociation = "Points"
    writer.UpdatePipeline()
    ResetSession()