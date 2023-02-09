from textwrap import dedent
from pathlib import Path
import argparse

import numpy as np
import pandas as pd


def time_reader(path, num_points=150, end_index=607):
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
    # Read data file
    data = pd.read_fwf(
        path,
        names=("index", "time"),
        nrows=end_index + 1,
        infer_nrows=end_index + 1,
    )

    # Get new evenly spaced timesteps
    # TODO This starts at the second index and doesn't include the final one.
    #      Is this intentional? If not, the following should fix it
    # t = np.linspace(data["time"].iloc[0], data["time"].iloc[-1], num_points)
    t_start = data["time"].iloc[1]
    t_end = data["time"].iloc[-1]
    t_step = (t_end - t_start) / num_points
    t = np.arange(t_start, t_end, t_step)

    # Get 2D array of differences between original times and new ones
    diff = np.abs(data["time"].values - t[:, np.newaxis])

    # Find the indices at which diff is minimum
    closest = np.argmin(diff, axis=1)

    # Match the closest indices with the new time steps and return
    return pd.DataFrame({"index": data["index"].values[closest], "time": t})


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
    results = time_reader(
        args.path,
        end_index=args.range,
        num_points=args.num_points,
    )
    # Write to file
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(args.output)
