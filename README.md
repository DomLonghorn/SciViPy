# SciVistaInterns

Compilation of scripts to be used for data visualisation produced by Freddie Carlisle and Dom Longhorn with a focus on file conversion and paraview visualisation

## BOUT_CARTESIAN_CONVERT:
    Made in collaboration with the XBOUT project and John Omotani (UKAEA)
    This script will take a BOUT++ dataset and will use pre-existing xbout interpolation routines to convert data into a cartesian format so that it can be read into software such as paraview. The current output is to a .csv file and can be modified to extract different variables as required. This process is VERY memory intensive however so ensure the script is ran on a machine with enough RAM 
## CRYSTAL_VIS_SCRIPT:
    Takes simulated materials data which has been converted to a paraview readable format (See xyz_to_csv.py) and performs the relevant visualisation methods in order to produce a visualisation of interesting properties. As with the JOREK_VIS_SCRIPT, the parameters can be modified to achieve desired outputs. 
## GIF_MAKER:
    Takes a series of generated screenshots and outputs them into a GIF for easy visualisation of temporal data 
## JOREK_VIS_SCRIPT:
    Takes already simulated data produced using JOREK code and automates the paraview visualisation process. There are parameters within the code that can be changed in order to modify the resulting output files. 
## TIME_READER:
    Takes in a .txt file containing a list of timesteps for a given data set and ensures that they are linearly replaced so that smooth animations can be produced with ease using paraview 
## xyz_to_csv:
    Reads data from the .xyz file format (commonly used for ovito data) and outputs to a .csv filetype for use elsewhere
