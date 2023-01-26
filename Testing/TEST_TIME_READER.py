def time_reader(filename="/jorek_times.txt", noofpoints=150, start=4000, Range=607):
    import time
    import os

    # Get directory of this file
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # File to read
    file = dir_path + filename

    # File to write
    output = dir_path + "/TestText.txt"

    # Open file
    with open(file, "r") as f:
        # Read lines
        FLines = f.readlines()
        # Get length
        FLength = len(FLines)

    # Create empty lists
    listofpoints = []
    listOfTimesteps = []
    listofnumbers = []
    CleanedOutputs = []
    FileID = []

    # Range
    count = 0

    # Iterate through lines
    for x in FLines:
        FullString = x
        StringToCut = FullString[0:14]
        FinalString = FullString.replace(StringToCut, "")
        SigFigString = FinalString[0:8]
        StringToConvert = SigFigString.strip()
        NumString = float(StringToConvert)
        # print(NumString)

        if count >= 553:
            NumString = (
                NumString * 10
            )  # Used to handle the difference in significant figures within the dataset (probably a more general solution)

        CleanedOutputs.append(NumString)
        count += 1

    # Get start value
    startval = CleanedOutputs[1]

    # Get end index
    endindex = Range

    # Get end value
    endval = CleanedOutputs[endindex]

    # Initial time step
    initialtimestep = (endval - startval) / noofpoints

    # Iterate through points
    for i in range(noofpoints):
        DummyTimestep = initialtimestep * i
        listOfTimesteps.append(DummyTimestep)
        listofnumbers.append(startval + listOfTimesteps[i])

    for i in range(len(listOfTimesteps)):
        # Find the value that's closest in the file to the given timestep and give its val
        closestval = min(
            enumerate(CleanedOutputs), key=lambda x: abs(x[1] - (listofnumbers[i]))
        )
        FileID.append(start + (10 * closestval[0]))

    # Write file
    with open(output, "w") as fp:
        for item in FileID:
            # write each item on a new line
            fp.write("%s\n" % item)
        print("Done")

    fp.close()


# test for time_reader:
def test_time_reader_output_file():
    import os

    time_reader(filename="/jorek_times.txt", noofpoints=150, start=4000, Range=607)

        # Get the path of the file
    file_name = "/TestText.txt"
    path = os.path.dirname(os.path.realpath(__file__))
    assert os.path.exists(path)
    # Check if file exists

test_time_reader_output_file()
