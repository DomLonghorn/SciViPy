Data = open("/home/user/Desktop/Data/Max data/w_220_cascade.00500.voxels.xyz","r")

ConvertedFile = open("/home/user/Desktop/Testxyz","w")
ConvertedFile.write("Cowabunga dudes \n")

count = 0
for x in Data:
    if count<10:
        ReadLine = x
        ConvertedFile.write(ReadLine)
        count+=1
