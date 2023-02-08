from textwrap import dedent
from pathlib import Path
import argparse

import numpy as np
from fortranformat import FortranRecordReader


def time_reader(path, output, num_points=150, end_index=607):
    """
    Function which will read a file and return equidistant readings from values within
    the file.

    The main purpose of this is to extract temporal data when equidistant time steps

    from formatformat import FortranRecordReader
    weren't initally recorded or were recorded in a nonlinear fashion.

    Take in an input file and a number of points to record and will return a text file
    with the specified number of points split equitemporally. This is useful when trying
    to create gifs from some simulated JOREK data.
    """
    indices = []
    times = []
    fortran_reader = FortranRecordReader("(I12, ES24.15)")
    with open(path) as f:
        for line in f:
            line_data = fortran_reader.read(line)
            indices.append(line_data[0])
            times.append(line_data[1])
    times = np.array(times)

    # TODO why start at 1 here? Should it be 0 to end_index-1?
    startval = times[1]
    endval = times[end_index]

    # Get an equitemporal time step over a given number of points
    timestep = (endval - startval) / num_points

    # Finds the value that's closest in the file to the given timestep and gives its val
    output_indices = []
    for i in range(num_points):
        time = startval + timestep * i
        closest_idx = np.argmin(np.abs(times - time))
        output_indices.append(indices[closest_idx])

    # Create and write to output file
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w") as f:
        np.savetxt(f, output_indices, fmt="%d")
    return output


if __name__ == "__main__":
    # Files originally specified in this script:
    # "C:\\Users\\FWKCa\\OneDrive\\Desktop\\Internship stuff\\jorek_times.txt"
    # "/home/user/Desktop/TEST DATA FOR SCRIPTS/TestText.txt"

    description = dedent(
        """\
        Takes in a .txt file containing a list of timesteps for a given data set and
        ensures that they are linearly replaced so that smooth animations can be
        produced with ease using paraview.
        """
    )

    # Define command line interface for this script
    parser = argparse.ArgumentParser(
        prog="SciViPy.time_reader",
        description=description,
    )

    parser.add_argument(
        "path",
        help="Path to .txt file.",
        type=Path,
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output file path.",
        type=Path,
        default="time_reader_out.txt",
    )

    parser.add_argument(
        "--num_points",
        help="The number of points to write to the output file.",
        type=int,
        default=150,
    )

    parser.add_argument(
        "--range",
        help="The number of time steps to read from the input file.",
        type=int,
        default=607,
    )

    # Get inputs/outputs from the command line
    args = parser.parse_args()

    # Check that input/output dirs are valid
    if not args.path.is_file():
        raise FileNotFoundError(args.path)

    # Run
    time_reader(
        args.path,
        args.output,
        end_index=args.range,
        num_points=args.num_points,
    )
