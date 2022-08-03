from paraview.simple import *
from paraview.servermanager import * #MAKE SURE TO INCLUDE THIS MODULE WHEN LOADING VTK FILES!!!!!!!!!!!!
import vtk



textfile = open("/home/user/Desktop/TEST DATA FOR SCRIPTS/TestText.txt","r")

datapoints = []

for x in textfile:
    lines = x
    stripnewline = x.rstrip()
    datapoints.append(stripnewline)
#print(datapoints) 
noofpoints = len(datapoints)

for i in range(1):
    CurrentVal = datapoints[i]
    StringVal = str(CurrentVal)   
    
    Currentfile = "/home/user/Desktop/JOREK_CLEANED 2.0/jorek"+StringVal+".pvsm"

    LoadState(Currentfile)
    

    data = GetActiveView()

    SaveData("/home/user/Desktop/JOREK_DATA 2.0/jorek"+StringVal+".vtk", proxy=data, FileType='vtk')    








    #ResetSession()

