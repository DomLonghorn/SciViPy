#Data = open("/home/user/Desktop/Data/Max data/w_220_cascade.00500.voxels.xyz","r")
from re import X


noofdatapoints = 10
count = 0
DataFile = open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\DataTXT.txt","w")
InfoFile = open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\InfoTXT.txt","w")


Dimensions = []

# with open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\w_220_cascade.00500.voxels.xyz","r") as Data:
#     ExtraInfo = Data.readlines()[0:2]
#     datapoints = Data.readlines()[2:(noofdatapoints+2)]
#     #Dimensions.append(Data.readlines())
# #print(datapoints)
# print(ExtraInfo)
# print(datapoints)

infoLines = []
dataLines = []
Data = open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\w_220_cascade.00500.voxels.xyz","r")

for lines in range(noofdatapoints):
    lines = Data.readline()
    if count <= 1:
        infoLines.append(lines)
        count+=1 
    elif count <= noofdatapoints:
        dataLines.append(lines)
        count+=1
    else: pass
#print(infoLines)
print(dataLines)

for i in range(0, noofdatapoints-2):
    DataFile.write(dataLines[i])
for x in range(2):
    InfoFile.write(infoLines[x])

