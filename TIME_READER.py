import numpy as np
import time
from numpy import Infinity


listofpoints = []
listOfTimesteps = []
listofnumbers = []
CleanedOutputs = []
FileID = []
File = open("/home/user/Desktop/JOREK_CLEANED/jorek_times.txt", 'r')
with open(r"/home/user/Desktop/JOREK_CLEANED/jorek_times.txt", 'r') as fp:


    FLength = len(fp.readlines())

    

Range = 607 #The number of time steps to read from a file
count=0 #Incorporates significanrt figures (see for loop below)
start = 4000 #Initial value to read


for x in File:
    FullString = x

    StringToCut = FullString[0:14]
    FinalString = FullString.replace(StringToCut, "")  #Trims the data into a floating point format to be used in numerical calculations
    SigFigString = FinalString[0:8]
    StringToConvert = SigFigString.strip()
    NumString = float(StringToConvert)

    if count>=553:
        NumString = NumString * 10 #Used to handle the difference in significant figures within the dataset (probably a more general solution)

    CleanedOutputs.append(NumString)
    count+=1
        
File.close() 

startval = CleanedOutputs[1]

endindex = 607
endval = CleanedOutputs[endindex]
noofpoints = 150 

initialtimestep = (endval - startval)/noofpoints #Used to determine the value of an equitemporal time step over a given number of pooints

for i in range(noofpoints): #Creates a temporary timestep that then gets added to an array which is added to the initial value
    DummyTimestep = initialtimestep*i
    listOfTimesteps.append(DummyTimestep)
    
    listofnumbers.append(startval+listOfTimesteps[i])




for i in range(len(listOfTimesteps)): #Finds the value that's closest in the file to the given timestep and gives its val
    closestval = min(enumerate(CleanedOutputs), key=lambda x:abs(x[1]-(listofnumbers[i])))
    FileID.append(4000+(10*closestval[0]))
    
print(FileID)

with open(r'/home/user/Desktop/TEST DATA FOR SCRIPTS/TestText.txt', 'w') as fp:
    for item in FileID:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')

fp.close