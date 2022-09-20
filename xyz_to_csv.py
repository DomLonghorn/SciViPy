
import numpy as np
import csv
from os import rename
from os import listdir
from os.path import isfile, join
#start loop
#open file
#convert to Lose unimportant info
#write to .CSV

#Took 54 mins to run through 415 files for max's data





mypath = "/home/user/Desktop/Data/Max Data/Max data set 2 (Big boy time)"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

namingpaths = []   

for i in range(len(onlyfiles)):
    namingpaths.append(onlyfiles[i].split(".")[1])


for i in range(len(onlyfiles)):
    if len(namingpaths[i]) == 1:
        namingpaths[i] = ("000" + namingpaths[i])
    if len(namingpaths[i]) == 2:
        namingpaths[i] = ("00" + namingpaths[i])
    if len(namingpaths[i]) == 3:
        namingpaths[i] = ("0" + namingpaths[i])

for i in range(len(onlyfiles)):
    print("naming path - "+namingpaths[i]+ "  File path:" + mypath+onlyfiles[i])

for i in range(len(onlyfiles)):
    Data = open("/home/user/Desktop/Data/Max Data/Max data set 2 (Big boy time)/"+onlyfiles[i],"r")
    print("iteration -" + str(i))

    for count, line in enumerate(Data):
            pass
    print('Total Lines', count + 1)
    noofdatapoints = count

    Data.close()

    Dimensions = []

    infoLines = []
    dataLines = []

    Data = open("/home/user/Desktop/Data/Max Data/Max data set 2 (Big boy time)/"+onlyfiles[i],"r")
        
    count = 0 #count reset

    for z in Data:
        Lines = z
        if count<=1:
            infoLines.append(Lines)
            count+=1
        elif count<= noofdatapoints:
            dataLines.append(Lines)
            count+=1
        else:
            pass

    DataLength = len(dataLines)


    X_Positions = []
    Y_Positions = []
    Z_Positions = []
    ScalarStrainFactor = []

    positionSplit = []

    for j in range(DataLength):
        position = dataLines[j]
        x = 2

        positionSplit = position.split(" ")

        Xposition = positionSplit[x]
        Yposition = positionSplit[x+2]
        Zposition = positionSplit[x+4]
        X_Positions.append(Xposition)
        Y_Positions.append(Yposition)
        Z_Positions.append(Zposition)
        
        for x in positionSplit:
            if len(x)<4:
                positionSplit.remove(x)
        
        vonMises = positionSplit[10]
        VonMisesString = vonMises.split("\n")
        ScalarStrainFactor.append(VonMisesString[0])

    ConvertedFile = open("/home/user/Desktop/Data/Max Data/ConvertedData/Converted - "+namingpaths[i]+".csv","x")
    writer = csv.writer(ConvertedFile)
    Row = []
    ConvertedFile.write("X Position" + "," + "Y Position" + "," + "Z Position" + "," + "Strain Scaling Factor" + "\n")

    count = 0

    for x in range(DataLength):
        Row = str(X_Positions[x]) + "," + str(Y_Positions[x]) + "," + str(Z_Positions[x]) + "," + str(ScalarStrainFactor[count])  + "\n"
        count+=1
        ConvertedFile.write(Row)
    
        
    ConvertedFile.close()