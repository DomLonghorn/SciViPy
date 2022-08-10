import numpy as np


Data = open("/home/user/Desktop/Data/Max Data/w_220_cascade.00500.voxels.xyz","r")
#Data = open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\w_220_cascade.00500.voxels.xyz","r")

# DataFile = open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\DataTXT.txt","w")
# InfoFile = open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\InfoTXT.txt","w")
DataFile = open("/home/user/Desktop/Data/Max Data/DataTXT.txt","w")
InfoFile = open("/home/user/Desktop/Data/Max Data/InfoTXT.txt","w")




noofdatapoints = 10
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

print(dataLines[0])

X_Positions = []
Y_Positions = []
Z_Positions = []

DataLength = len(dataLines)

F1 = np.zeros((3,DataLength))
F2 = np.zeros((3,DataLength))
F3 = np.zeros((3,DataLength))

for i in range(DataLength):
    position = dataLines[i]
    Xposition = float(position[4:14])
    Yposition = float(position[14:24])
    Zposition = float(position[24:34])
    X_Positions.append(Xposition)
    Y_Positions.append(Yposition)
    Z_Positions.append(Zposition)

    f11 =   float(position[44:54])
    F1[0,i] = f11
    f12 = float(position[54:64])
    F1[1,i] = f12
    f13 = float(position[64:74])
    F1[2,i] = f13
    f21 = float(position[74:84])
    F2[0,i] = f21
    f22 = float(position[84:94])
    F2[1,i] = f22
    f23 = float(position[94:104])
    F2[2,i] = f23
    f31 = float(position[104:114])
    F3[0,i] = f31
    f32 = float(position[114:124])
    F3[1,i] = f32
    f33 = float(position[124:134])
    F3[2,i] = f33
print(F1)
