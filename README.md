# SciViPy

Covered under the Mozilla Public License 2.0

Compilation of scripts to be used for data visualisation produced by Freddie Carlisle
and Dom Longhorn with a focus on file conversion and paraview visualisation

## Installation

SciViPy depends on the `paraview` Python package. This may be installed from source, but
can be more easily obtained using Anaconda:

```bash
$ # Create and activate new conda environment
$ conda create --name SciViPy python=3.8
$ conda activate SciViPy
$ # Install Paraview
$ conda install -c conda-forge paraview
```

SciViPy can then be installed using `pip`:

```bash
$ python3 -m pip install --upgrade pip
$ python3 -m pip install .
```

Note that you should NOT have `vtk` installed in your Python environment, as this will
interfere with the version packaged with Paraview.

Testing dependencies can be installed using:

```bash
$ python3 -m pip install -e .[tests]
```

Tests can then be run using `pytest`

```bash
$ python3 -m pytest tests
```

Similarly, to build the docs:

```bash
$ python3 -m pip install -e .[docs]
$ cd docs
$ make html
```

Docs can then be viewed by opening
`file:///path/to/your/workspace/SciViPy/docs/build/html/index.html` in a web browser.

## Features

### bout_cartesian_convert 

Made in collaboration with the XBOUT project and John Omotani (UKAEA).

This script will take a BOUT++ dataset and will use pre-existing xbout interpolation
routines to convert data into a cartesian format so that it can be read into software
such as paraview. The current output is to a `.csv` file and can be modified to extract
different variables as required. This process is VERY memory intensive however so ensure
the script is ran on a machine with enough RAM.

![Clip of XBout](https://user-images.githubusercontent.com/64920607/191275860-8a3a2c59-a197-4296-9c45-fcc3e119485e.png)

### crystal_vis_script

Takes simulated materials data which has been converted to a paraview readable format
(See `xyz_to_csv.py`) and performs the relevant visualisation methods in order to
produce a visualisation of interesting properties. As with `jorek_vis_script.py`, the
parameters can be modified to achieve desired outputs.

![CrystalVis](https://user-images.githubusercontent.com/64920607/191737728-f1614f16-05b6-4342-a626-0589d4fa47a5.png)


### make_gif

Takes a series of generated screenshots and outputs them into a GIF for easy
visualisation of temporal data.

### jorek_vis_script

Takes already simulated data produced using JOREK code and automates the paraview
visualisation process. There are parameters within the code that can be changed in order
to modify the resulting output files.

![Screenshot (58)](https://user-images.githubusercontent.com/110162827/191276969-16926ce2-cdf6-45c2-8770-bf94929f8870.png)

### time_reader

Takes in a `.txt` file containing a list of timesteps for a given data set and ensures
that they are linearly replaced so that smooth animations can be produced with ease
using paraview.

### xyz_to_csv

Reads data from the `.xyz` file format (commonly used for ovito data) and outputs to a
`.csv` filetype for use elsewhere 
