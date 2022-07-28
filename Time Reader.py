from tokenize import String
import numpy as np
import time

from numpy import Infinity

File = open("/home/user/Desktop/JOREK_CLEANED/jorek_times.txt", 'r')
with open(r"/home/user/Desktop/JOREK_CLEANED/jorek_times.txt", 'r') as fp:
# for i in File:
#     print(i)

    FLength = len(fp.readlines())

    CleanedOutputs = []
    FileID = []
# print(len(CleanedOutputs)) 
Range = 607

count=0
start = 4000
for x in File:
    FullString = x
   # print(count)

    StringToCut = FullString[0:14]
    FinalString = FullString.replace(StringToCut, "")  #Trims the data into a floating point format to be used in numerical calculations
    SigFigString = FinalString[0:8]
    StringToConvert = SigFigString.strip()
    NumString = float(StringToConvert)

    if count>=553:
        NumString = NumString * 10

    CleanedOutputs.append(NumString)

    FileID.append(start+(count*10))

    


    #print(CleanedOutputs[count])
    count+=1
        
File.close()
#print(CleanedOutputs)
DifferencesList = []
    
for i in range(len(CleanedOutputs)-1):
    Difference = CleanedOutputs[i+1] - CleanedOutputs[i]
    DifferencesList.append(Difference)
        #print(DifferencesList[i])


startval = CleanedOutputs[1]

endindex = 607
endval = CleanedOutputs[endindex]
noofpoints = 10

initialtimestep = (endval - startval)/noofpoints
listofpoints = []

#print(CleanedOutputs)
print(initialtimestep)

listOfTimesteps = []
listofnumbers = []

for i in range(noofpoints): #Creates a temporary timestep that then gets added to an array which is added to the initial value
    DummyTimestep = initialtimestep*i
    listOfTimesteps.append(DummyTimestep)
    
    listofnumbers.append(startval+listOfTimesteps[i])

print(listOfTimesteps)



for i in range(len(listOfTimesteps)): #Finds the value that's closest in the file to the given timestep
    
    closestval = min(CleanedOutputs, key=lambda x:abs(x-(listofnumbers[i])))
    print(closestval)
    #print(CleanedOutputs.index(closest)

# for i in range (5):
#     closestval = 99999999999999
#     timestep = initialtimestep*i
#     #print(timestep)
#     valuetoadd = CleanedOutputs[0]

#     for j in range (endindex):
#         currentdifference = abs(CleanedOutputs[j]-timestep)
#         #print(currentdifference)
#         if currentdifference <+ closestval:
#             valuetoadd = CleanedOutputs[j]
#             closestval = currentdifference

#     listofpoints.append(valuetoadd)
    
    
# print(listofpoints)

#print(listofpoints)
# while ID <= 607:
#     ID = closest(CleanedOutputs,CurrentVal)
#     print(FileID[ID])

#     print(ID)
#     CurrentVal += 0.009
