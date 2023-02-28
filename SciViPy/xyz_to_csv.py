import argparse
from pathlib import Path

# start loop
# open file
# convert to Lose unimportant info
# write to .CSV

# Took 54 mins to run through 415 files for max's data


def xyz_to_csv(data_dir, output_dir):
    # TODO run on just a single file, can loop over this function
    onlyfiles = [f.name for f in data_dir.iterdir() if f.is_file()]
    print(onlyfiles)

    namingpaths = []

    for i in range(len(onlyfiles)):
        namingpaths.append(onlyfiles[i].split(".")[1])

    for i in range(len(onlyfiles)):
        if len(namingpaths[i]) == 1:
            namingpaths[i] = "000" + namingpaths[i]
        if len(namingpaths[i]) == 2:
            namingpaths[i] = "00" + namingpaths[i]
        if len(namingpaths[i]) == 3:
            namingpaths[i] = "0" + namingpaths[i]

    for i in range(len(onlyfiles)):
        print(
            "naming path - "
            + namingpaths[i]
            + "  File path:"
            + str(data_dir)
            + onlyfiles[i]
        )

    for i in range(len(onlyfiles)):
        Data = open(data_dir / onlyfiles[i], "r")
        print("iteration -" + str(i))

        for count, line in enumerate(Data):
            pass
        print("Total Lines", count + 1)
        noofdatapoints = count

        Data.close()

        infoLines = []
        dataLines = []

        Data = open(data_dir / onlyfiles[i], "r")

        count = 0  # count reset

        for z in Data:
            Lines = z
            if count <= 1:
                infoLines.append(Lines)
                count += 1
            elif count <= noofdatapoints:
                dataLines.append(Lines)
                count += 1
            else:
                pass

        DataLength = len(dataLines)

        X_Positions = []
        Y_Positions = []
        Z_Positions = []
        ScalarStrainFactor = []

        positionSplit = []

        for j in range(DataLength):
            position = dataLines[j]
            x = 2

            positionSplit = position.split(" ")

            Xposition = positionSplit[x]
            Yposition = positionSplit[x + 2]
            Zposition = positionSplit[x + 4]
            X_Positions.append(Xposition)
            Y_Positions.append(Yposition)
            Z_Positions.append(Zposition)

            for x in positionSplit:
                if len(x) < 4:
                    positionSplit.remove(x)

            vonMises = positionSplit[10]
            VonMisesString = vonMises.split("\n")
            ScalarStrainFactor.append(VonMisesString[0])

        ConvertedFile = open(
            output_dir / ("Converted - " + namingpaths[i] + ".csv"),
            "x",
        )
        Row = []
        ConvertedFile.write(
            "X Position"
            + ","
            + "Y Position"
            + ","
            + "Z Position"
            + ","
            + "Strain Scaling Factor"
            + "\n"
        )

        count = 0

        for x in range(DataLength):
            Row = (
                str(X_Positions[x])
                + ","
                + str(Y_Positions[x])
                + ","
                + str(Z_Positions[x])
                + ","
                + str(ScalarStrainFactor[count])
                + "\n"
            )
            count += 1
            ConvertedFile.write(Row)

        ConvertedFile.close()


if __name__ == "__main__":
    # Files originally specified in this scriptL
    # data_dir="/home/user/Desktop/Data/Max Data/Max data set 2 (Big boy time)"

    # Define command line interface for this script
    parser = argparse.ArgumentParser(
        prog="SciViPy.xyz_to_csv",
        description=("Convert .xyz format (commonly used for ovito data) to .csv."),
    )

    parser.add_argument(
        "data_dir",
        help="Path to directory containing .xyz",
        type=Path,
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output directory path.",
        type=Path,
    )

    # Get inputs/outputs from the command line
    args = parser.parse_args()

    # Check that input/output dirs are valid
    if not args.data_dir.is_dir():
        raise NotADirectoryError(args.data_dir)

    if args.output is None:
        output = args.data_dir.parent / "ConvertedData"
    else:
        output = args.output
    output.mkdir(parents=True, exist_ok=True)

    # Run
    xyz_to_csv(args.data_dir, output)
