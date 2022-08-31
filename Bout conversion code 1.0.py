#!/usr/bin/env python3

from tkinter import Y
from matplotlib import pyplot as plt
import numpy as np
import xarray as xr
from xbout import open_boutdataset
import csv
import math

ds = open_boutdataset(
    "BOUT.dmp.nc",
    gridfilepath="21712_260_96_next.grd.nc",
    chunks={"t": 1},
    keep_xboundaries=False,
    keep_yboundaries=False,
    geometry="toroidal",
)

print("------")



# Work with density (it's expensive to interpolate all the variables...)
n = ds["n"]


# Select a single time point (to save memory)
n = n.isel(t=0)

# Parallel interpolation to increase resolution using field-aligned structure
# of data.
# Increases parallel resolution by a factor of `n`.


print("doing parallel interpolation")
n = n.bout.interpolate_parallel(n=8)

# Simulation only covered 1/4 of the full torus, so use 4 copies of data to
# fill the full toroidal angle
n_copies = [n.copy() for _ in range(4)]

# Fix the toroidal angle coordinates...
for i in range(1,4):
    n_copies[i]["zeta"] = n_copies[i]["zeta"] + i * np.pi/2

n = xr.concat(n_copies, "zeta")
del n_copies


# Interpolate onto cylindrical coordinates
##########################################

print("making cylindrical coordinates output")

# Create arrays with desired output values
R_out = np.linspace(n["R"].min(), n["R"].max(), 1000)
Z_out = np.linspace(n["Z"].min(), n["Z"].max(), 1000)

n_cylindrical = n.bout.interpolate_from_unstructured(R=R_out, Z=Z_out)
#print(n_cylindrical)

# Make some plot as a sanity check
# plt.figure()
# n_cylindrical.isel(zeta=12).plot()
# plt.savefig("n_cylindrical_check.pdf")



# Interpolate onto Cartesian coordinates
########################################

print("making Cartesian coordinates output")

nX = 600
nY = 600
nZ = 600

# Note, this method defaults to single-precision output, to reduce memory usage
# and computation time. This should be fine for visualisation.
n_Cartesian = n.bout.interpolate_to_cartesian(nX, nY, nZ)
#print(n_Cartesian)


n_Cartesian_results = n_Cartesian.values
print(n_Cartesian_results)



X = n_Cartesian["X"]
Y = n_Cartesian["Y"]
Z = n_Cartesian["Z"]


print("opening files")

file = open("/home/user/Desktop/Data/BOUT++ Data/John Data/Saved data(Cartesian).csv","w")
file2 = open("/home/user/Desktop/Data/BOUT++ Data/John Data/Saved data 2.csv","w")
writer = csv.writer(file)
writer2 = csv.writer(file2)




# Make some plot as a sanity check
# Interpolation artifacts (?) can cause negative densities so set vmin=0.0 to
# get sensible color scale.



# plt.figure()
# n_Cartesian.isel(Z=nZ).plot()
# # plt.savefig("n_Cartesian_check_XY.pdf")
# plt.show()

# plt.figure()
# n_Cartesian.isel(Y=nY // 2).plot()
# plt.savefig("n_Cartesian_check_XZ.pdf")


# plt.figure()
# n_Cartesian.isel(X=nX // 2).plot()
# # # plt.savefig("n_Cartesian_check_YZ.pdf")
# # # plt.show()

# print(n)



def StringMake(String):
    FinalString = []
    for i in range(len(String)):
        ListAddition = str(String[i])

        ListStrip = ListAddition.split("(")
        ListStrip2 = ListStrip[2].split(")")

        FinalString.append(ListStrip2[0])
    return FinalString

print("making strings")

StringX = StringMake(X)
StringY = StringMake(Y)
StringZ = StringMake(Z)

Coords=[]







# for i in range(len(X)):
#     ListAdditionX = str(X[i]) 
#     ListAdditionY = str(Y[i]) 
#     ListAdditionZ = str(Z[i]) 

#     ListStripX = ListAdditionX.split("(")
#     ListStripX2 = ListStripX[2].split(")")
    
#     ListStripY = ListAdditionY.split("(")
#     ListStripY2 = ListStripY[2].split(")")

#     ListStripZ = ListAdditionZ.split("(")
#     ListStripZ2 = ListStripZ[2].split(")")

#     StringX.append(ListStripX2[0])
#     StringY.append(ListStripY2[0])
#     StringZ.append(ListStripZ2[0])





# count = 0
# for i in range(len(StringX)):
#     if StringX[i] == StringY[i]:
#         print(str(i) + "- Same")
#         count +=1
#     else:
#         pass
# print(count)


print("Writing files")

Row = []
ResultsRow = []

print("doing results")

print(n_Cartesian_results[0,0])

StringNan = np.ravel(n_Cartesian_results)
print(StringNan)

StringNan[np.isnan(StringNan)] = int(0)
print("writing positions")

print(len(StringNan))

XLength = len(StringX)
YLength = len(StringY)
ZLength = len(StringZ)
# NLength = len(String0)

def FirstFileLength(StringX):
    Boundary = (len(StringX)/2)
    Step = math.floor(Boundary)
    return Step



count = 0

file.write("X Position" + "," + "Y Position" + "," + "Z Position" + " , " + "N" + "\n")
for i in range(len(StringX)):
    for j in range(len(StringY)):
        for k in range(len(StringZ)):
            
            Row = StringX[i] + " , " + StringY[j] + " , " + StringZ[k] + " , " + str(StringNan[count])  + "\n"
            if StringNan[count] != 0:
                file.write(Row)
            count += 1
file.close()
# file2.write("X Position" + "," + "Y Position" + "," + "Z Position" + " , " + "N" + "\n")
# for i in range(FirstFileLength(StringX),len(StringX)):
#     for j in range(FirstFileLength(StringY),len(StringY)):
#         for k in range(FirstFileLength(StringZ),len(StringZ)):
#             Row = StringX[i] + " , " + StringY[j] + " , " + StringZ[k] + " , " + str(Test[k]) + "\n"
#             file2.write(Row)
# file2.close()




