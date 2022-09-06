# SciVistaInterns

Compilation of scripts to be used for data visualisation produced by Freddie Carlisle and Dom Longhorn with a particular focus on paraview readability

JOREK_VIS_SCRIPT:
    Takes already simulated data produced using JOREK code and automates the paraview visualisation process. There are parameters within the code that can be changed in order to modify the resulting output files.
Timestep_Calculator:
    Takes in a .txt file containing a list of timesteps for a given data set and ensures that they are linearly replaced so that smooth animations can be produced with ease using paraview
Bout Conversion Code:
    Made in collaboration with the XBOUT project and John Omotani (UKAEA)
    This script will take a BOUT++ dataset and will use pre-existing xbout interpolation routines to convert data into a cartesian format so that it can be read into software such as paraview. The current output is to a .csv file and can be modified to extract different variables as required. This process is VERY memory intensive however so ensure the script is ran on a machine with enough RAM
Bout Conversion Code:
    Made in collaboration with the XBOUT project and John Omotani (UKAEA)
    This script will take a BOUT++ dataset and will use pre-existing xbout interpolation routines to convert data into a cartesian format so that it can be read into software such as paraview. The current output is to a .csv file and can be modified to extract different variables as required. This process is VERY memory intensive however so ensure the script is ran on a machine with enough RAM    
