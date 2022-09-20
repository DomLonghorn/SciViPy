# SciViPy

Compilation of scripts to be used for data visualisation produced by Freddie Carlisle and Dom Longhorn with a focus on file conversion and paraview visualisation

**bout_cartesian_convert**: 
    Made in collaboration with the XBOUT project and John Omotani (UKAEA)
    This script will take a BOUT++ dataset and will use pre-existing xbout interpolation routines to convert data into a cartesian format so that it can be read into software such as paraview. The current output is to a .csv file and can be modified to extract different variables as required. This process is VERY memory intensive however so ensure the script is ran on a machine with enough RAM ![Clip of XBout](https://user-images.githubusercontent.com/64920607/191275860-8a3a2c59-a197-4296-9c45-fcc3e119485e.png) \
**crystal_vis_script:**
    Takes simulated materials data which has been converted to a paraview readable format (See xyz_to_csv.py) and performs the relevant visualisation methods in order to produce a visualisation of interesting properties. As with the JOREK_VIS_SCRIPT, the parameters can be modified to achieve desired outputs. \
**gif_maker:**
    Takes a series of generated screenshots and outputs them into a GIF for easy visualisation of temporal data \
**jorek_vis_script:**
    Takes already simulated data produced using JOREK code and automates the paraview visualisation process. There are parameters within the code that can be changed in order to modify the resulting output files. ![Screenshot (58)](https://user-images.githubusercontent.com/110162827/191276969-16926ce2-cdf6-45c2-8770-bf94929f8870.png) \
**time_reader:**
    Takes in a .txt file containing a list of timesteps for a given data set and ensures that they are linearly replaced so that smooth animations can be produced with ease using paraview \
**xyz_to_csv:**
    Reads data from the .xyz file format (commonly used for ovito data) and outputs to a .csv filetype for use elsewhere 
