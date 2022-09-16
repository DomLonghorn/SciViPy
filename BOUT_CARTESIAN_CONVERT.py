#!/usr/bin/env python3
#Test
from tkinter import W, Y
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

# Interpolate onto Cartesian coordinates
########################################

print("making Cartesian coordinates output")

nX = 600
nY = 600
nZ = 600

# Note, this method defaults to single-precision output, to reduce memory usage
# and computation time. This should be fine for visualisation.
n_Cartesian = n.bout.interpolate_to_cartesian(nX, nY, nZ)


n_Cartesian_results = n_Cartesian.values
print(n_Cartesian_results)

#Saving Coord values into individual Arrays

X = n_Cartesian["X"]
Y = n_Cartesian["Y"]
Z = n_Cartesian["Z"]


print("opening files")

#Opening files to written into

file = open("/home/user/Desktop/Data/BOUT++ Data/John Data/Saved data(Cartesian).csv","w")        
writer = csv.writer(file)

#Defining a function to create string arrays from coordinates to write to the file easily

def StringMake(String):
    FinalString = []
    for i in range(len(String)):
        ListAddition = str(String[i])

        ListStrip = ListAddition.split("(")
        ListStrip2 = ListStrip[2].split(")")

        FinalString.append(ListStrip2[0])
    return FinalString

print("making strings")

#Creating the arrays for the stringed coords

StringX = StringMake(X)
StringY = StringMake(Y)
StringZ = StringMake(Z)




print("doing results")

#Creating a long array of the density results

StringNan = np.ravel(n_Cartesian_results)
print(StringNan)

#Turning each of the results from Nan -> 0 which means paraview can read it

StringNan[np.isnan(StringNan)] = int(0)
print("writing positions")


Row = []

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




