"""
Script to read in simulated BOUT++ data, performs cartesian interpolation and saves to
.csv file.

Made with help from John Omotani at the UKAEA This script takes advantage of the
pre-exisiting xbout analysis routines to load in a netcdf file and to interpolate from
field-aligned coordinates to cartesian and save the result. This process is very memory
intensive and takes a decent amount of time to complete, so it is reccomended to only
run this script on a high-powered machine/cluster.

Run with the --help option for a description of how to use this script.

Licensed under MPL-2.0
"""

from pathlib import Path
import numpy as np
import xarray as xr
from xbout import open_boutdataset
import argparse

# Defining a function to create string arrays from coordinates to write to the file
# easily


def StringMake(inputvar):
    """
    Changes type of a variable from numerical to string.

    Runs through the entire array for the given variable and stores each individual item
    as a string element as opposed to some form of numerical value. This is done for
    later ease when saving the file.

    Parameters
    ==========
    inputvar: List[str]
        Variable which you want to convert from a numerical list into a list of strings.

    Returns
    =======
    List[str]
        An list of strings which in content match the inputvar but with a change of
        type.
    """
    FinalString = []
    for i in range(len(inputvar)):
        ListAddition = str(inputvar[i])

        ListStrip = ListAddition.split("(")
        ListStrip2 = ListStrip[2].split(")")

        FinalString.append(ListStrip2[0])
    return FinalString


def bout_cartesian_convert(boutdataset, gridfilepath, outfile):
    ds = open_boutdataset(
        boutdataset,
        gridfilepath=gridfilepath,
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
    for i in range(1, 4):
        n_copies[i]["zeta"] = n_copies[i]["zeta"] + i * np.pi / 2

    n = xr.concat(n_copies, "zeta")
    del n_copies

    # Interpolate onto cylindrical coordinates
    ##########################################

    print("making cylindrical coordinates output")

    # Create arrays with desired output values
    R_out = np.linspace(n["R"].min(), n["R"].max(), 1000)
    Z_out = np.linspace(n["Z"].min(), n["Z"].max(), 1000)

    # FIXME What is this used for?
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

    # Saving Coord values into individual Arrays

    X = n_Cartesian["X"]
    Y = n_Cartesian["Y"]
    Z = n_Cartesian["Z"]

    print("opening files")

    # Opening files to written into

    Path(outfile).parent.mkdir(parents=True, exist_ok=True)
    file = open(outfile, "w")

    print("making strings")

    # Creating the arrays for the stringed coords

    StringX = StringMake(X)
    StringY = StringMake(Y)
    StringZ = StringMake(Z)

    print("doing results")

    # Creating a long array of the density results

    StringNan = np.ravel(n_Cartesian_results)
    print(StringNan)

    # Turning each of the results from Nan -> 0 which means paraview can read it

    StringNan[np.isnan(StringNan)] = int(0)
    print("writing positions")

    Row = []

    count = 0

    file.write(
        "X Position" + "," + "Y Position" + "," + "Z Position" + " , " + "N" + "\n"
    )
    for i in range(len(StringX)):
        for j in range(len(StringY)):
            for k in range(len(StringZ)):
                Row = (
                    StringX[i]
                    + " , "
                    + StringY[j]
                    + " , "
                    + StringZ[k]
                    + " , "
                    + str(StringNan[count])
                    + "\n"
                )
                if StringNan[count] != 0:
                    file.write(Row)
                count += 1

    file.close()


if __name__ == "__main__":
    # Files originally specified in this script:
    # boutdataset="BOUT.dmp.nc"
    # gridfilepath="21712_260_96_next.grd.nc"
    # outfile="/home/user/Desktop/Data/BOUT++ Data/John Data/Saved data(Cartesian).csv"

    # Define command line interface for this script
    parser = argparse.ArgumentParser(
        prog="SciViPy.bout_cartesian_convert",
        description=(
            "Script to read in simulated BOUT++ data, performs cartesian interpolation "
            "and saves to .csv file."
        ),
    )

    parser.add_argument(
        "boutdataset",
        help="Path to BOUT data, as a netCDF4 file.",
        type=Path,
    )

    parser.add_argument(
        "gridfilepath",
        help=(
            "Path to a grid file, containing variaibles needed to specify a toroidal "
            "geometry."
        ),
        type=Path,
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Name of output CSV file.",
        default="bout_cartesian_convert_out.csv",
        type=Path,
    )

    # Get inputs/outputs from the command line
    args = parser.parse_args()

    # Check that files are valid
    if not args.boutdataset.is_file():
        raise FileNotFoundError(args.boutdataset)
    if not args.gridfilepath.is_file():
        raise FileNotFoundError(args.gridfilepath)

    # Run
    bout_cartesian_convert(
        args.boutdataset,
        args.gridfilepath,
        outfile=args.output,
    )
