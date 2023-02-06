from Scripts.time_reader import time_reader


# test for time_reader:
def test_time_reader_output_file():
    import os

    file_name = "\\testText.txt"
    path = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(path + file_name):
        os.remove(path + file_name)
    time_reader(
        filename="\jorek_times.txt", noofpoints=150, start=4000, Range=607, Testing=True
    )

    # Get the path of the file
    assert os.path.exists(path + file_name)
    # Check if file exists


test_time_reader_output_file()
