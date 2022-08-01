import numpy as np
import time

count = 0


myList = [2,15,4,66,2345,7,0.8]


myNumber = 54

print(min(myList, key=lambda x:abs(x-myNumber)))



# File = open("/home/user/Desktop/JOREK_CLEANED/jorek_times.txt", 'r')
# for x in File:
#     print(x)
#     print(count)
#     count+=1



# with open("/home/user/Desktop/JOREK_CLEANED/jorek_times.txt") as file:
#     for x in file:
#         print(count)
#         FullString = file.readlines()
#         print(FullString)
#         StringToCut = FullString[0:14]
#         #print(StringToCut)
#         FinalString = FullString[count].replace(StringToCut, "")
#         #print(FinalString)     
#         SigFigString = FinalString[0:8]
#         #print(SigFigString)
#         StringToConvert = SigFigString.strip()
#         #print(StringToConvert)
#         count+=1

