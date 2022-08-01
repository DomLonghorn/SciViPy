import netCDF4 as nc
import pyvista as pv
 


ds = nc.Dataset("/home/user/Desktop/BOUT++ Data/results.nc")
 
# take this info from BOUT.inp :
 
nx = 256
ny = 1
nz = 132
NOUT = 50
scalarField = "T"
 
# convert
 
# save single dataset with all arrays
img = pv.UniformGrid([nx, ny, nz])
for t in range(NOUT):
    img[scalarField+str(t).zfill(3)] = ds[scalarField][t].ravel()
img.save("result.vti")
 
# save time series
for t in range(NOUT):
    img = pv.UniformGrid([nx, ny, nz])
    img[scalarField] = ds[scalarField][t].ravel()
    img.save("mesh"+str(t)+".vti")