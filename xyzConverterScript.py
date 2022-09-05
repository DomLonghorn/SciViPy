
import numpy as np
import csv

Data = open("/home/user/Desktop/Data/Max Data/Max data set 2 (Big boy time)/large_cascade6400eV.0.vox64.xyz","r")

DataFile = open("/home/user/Desktop/Data/Max Data/DataTXT.txt","w")
InfoFile = open("/home/user/Desktop/Data/Max Data/InfoTXT.txt","w")



for count, line in enumerate(Data):
        pass
print('Total Lines', count + 1)

noofdatapoints = 100

count = 0
print(count)
Dimensions = []

infoLines = []
dataLines = []





for x in Data:
    lines = Data.readline(x)
    print(lines)
    if count <= 1:
        infoLines.append(lines)
        count+=1 
        print(infoLines)
    elif count <= noofdatapoints:
        dataLines.append(lines)
        count+=1
        print(dataLines)
    else: pass


#Don't think I need this anymore

for i in range(0, noofdatapoints-2):
    DataFile.write(dataLines[i])
for x in range(2):
    InfoFile.write(infoLines[x])




DataLength = len(dataLines)
print(DataLength)

LineCount = 0

F1 = np.zeros((3,DataLength))
F2 = np.zeros((3,DataLength))
F3 = np.zeros((3,DataLength))

X_Positions = []
Y_Positions = []
Z_Positions = []
ScalarStrainFactor = []

positionSplit = []

for i in range(DataLength):
    print(dataLines[i])
    position = dataLines[i]
    x = 2

    positionSplit = position.split(" ")

    print(positionSplit)
    print(positionSplit)
    Xposition = positionSplit[x]
    Yposition = positionSplit[x+2]
    Zposition = positionSplit[x+4]

    X_Positions.append(Xposition)
    print(X_Positions[i])
    print(len(X_Positions))
    Y_Positions.append(Yposition)
    Z_Positions.append(Zposition)


    for x in positionSplit:
        if len(x)<4:
            positionSplit.remove(x)

    

    # f11Value = 4
    # f22Value = 8
    # f33Value = 12
    # f11 = float(positionSplit[f11Value])
    # f22 = float(positionSplit[f22Value])
    # f33 = float(positionSplit[f33Value])

    # StrainFactor = f11 + f22 + f33
    # ScalarStrainFactor.append(StrainFactor-3)
    
    # LineCount += 1
    # F1[0,i] = f11
    # F2[1,i] = f22
    # F3[2,i] = f33


    # ScalarStrainFactor = float(positionSplit[])
ConvertedFile = open("/home/user/Desktop/Data/Max Data/ConvertedData2.csv","w")
writer = csv.writer(ConvertedFile)
Row = []
ConvertedFile.write("X Position" + "," + "Y Position" + "," + "Z Position" + "," + "Strain Scaling Factor" + "\n")
for i in range(DataLength):
    Row = str(X_Positions[i]) + "," + str(Y_Positions[i]) + "," + str(Z_Positions[i]) + "," + str(ScalarStrainFactor[i])  + "\n"
    print(i)
    print(Row)
    
    ConvertedFile.write(Row)

    
ConvertedFile.close()