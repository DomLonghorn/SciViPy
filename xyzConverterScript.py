#Data = open("/home/user/Desktop/Data/Max data/w_220_cascade.00500.voxels.xyz","r")
noofdatapoints = 10
count = 0
convertedFile = open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\Testxyz.txt","w")
Dimensions = []

# with open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\w_220_cascade.00500.voxels.xyz","r") as Data:
#     datapoints = Data.readlines()[1:(noofdatapoints+2)]
#     print(Data.readline())
#     Dimensions.append(Data.readlines()[2])
Data = open("C:\\Users\\FWKCa\\OneDrive\\Desktop\\Max Data\\w_220_cascade.00500.voxels.xyz","r")

for x in Data range(1:(noofpoints+2)):
    datapoints = x 




#print(Dimensions)




for i in range(0, noofdatapoints):
    convertedFile.write(datapoints[i])
    

