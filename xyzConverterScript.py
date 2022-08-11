
import numpy as np
import csv

Data = open("/home/user/Desktop/Data/Max Data/w_220_cascade.00500.voxels.xyz","r")
#Data = open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\w_220_cascade.00500.voxels.xyz","r")

# DataFile = open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\DataTXT.txt","w")
# InfoFile = open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\InfoTXT.txt","w")
DataFile = open("/home/user/Desktop/Data/Max Data/DataTXT.txt","w")
InfoFile = open("/home/user/Desktop/Data/Max Data/InfoTXT.txt","w")




noofdatapoints = 5000000
count = 0
Dimensions = []

infoLines = []
dataLines = []

for lines in range(noofdatapoints):
    lines = Data.readline()
    if count <= 1:
        infoLines.append(lines)
        count+=1 
    elif count <= noofdatapoints:
        dataLines.append(lines)
        count+=1
    else: pass


for i in range(0, noofdatapoints-2):
    DataFile.write(dataLines[i])
for x in range(2):
    InfoFile.write(infoLines[x])




DataLength = len(dataLines)


# class Tensor:

#     def __init__(self, DataLength):
#         F1 = np.zeros((3,DataLength))
#         F2 = np.zeros((3,DataLength))
#         F3 = np.zeros((3,DataLength))
#         X_Positions = []
#         Y_Positions = []
#         Z_Positions = []
#         ScalarStrainFactor = []



#     def position_components (dataLines):
#         for i in range(DataLength):
#             position = dataLines[i]
#             Xposition = float(position[4:14])
#             Yposition = float(position[14:24])
#             Zposition = float(position[24:34])
#             X_Positions.append(Xposition)
#             Y_Positions.append(Yposition)
#             Z_Positions.append(Zposition)

#     def Components(pos):
#         count = 1
#         for i in range(44,124,10):
          



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
    #print(LineCount)
    position = dataLines[i]
    x = 2

    positionSplit = position.split(" ")

    Xposition = positionSplit[x]
    
    Yposition = positionSplit[x+2]
    Zposition = positionSplit[x+4]
    #print(Xposition,Yposition,Zposition)
    # Xposition = float(position[4:14])
    # Yposition = float(position[14:24])
    # Zposition = float(position[24:34])
    X_Positions.append(Xposition)
    Y_Positions.append(Yposition)
    Z_Positions.append(Zposition)
    #print(position)
    #print(positionSplit)

    for x in positionSplit:
        if len(x)<4:
            positionSplit.remove(x)
    #print(positionSplit)

    f11Value = 4
    f22Value = 8
    f33Value = 12
    f11 = float(positionSplit[f11Value])
    f22 = float(positionSplit[f22Value])
    f33 = float(positionSplit[f33Value])

    StrainFactor = f11 + f22 + f33
    ScalarStrainFactor.append(StrainFactor-3)
    
    LineCount += 1
    F1[0,i] = f11
    F2[1,i] = f22
    F3[2,i] = f33

# print(F1)
#print(ScalarStrainFactor)
ConvertedFile = open("/home/user/Desktop/Data/Max Data/ConvertedData.csv","w")
writer = csv.writer(ConvertedFile)
Row = []
ConvertedFile.write("X Postition" + "," + "Y Position" + "," + "Z Position" + "," + "Strain Scaling Factor" + "\n")
for i in range(DataLength):
    Row = str(X_Positions[i]) + "," + str(Y_Positions[i]) + "," + str(Z_Positions[i]) + "," + str(ScalarStrainFactor[i])  + "\n"
    # ConvertedFile.writelines([str(X_Positions[i]) + "," + str(Y_Positions[i]) + "," + str(Z_Positions[i]) + "," + str(ScalarStrainFactor[i])])
    print(i)
    print(Row)
    
    ConvertedFile.write(Row)
    #writer.writerow(Row)

    
ConvertedFile.close()