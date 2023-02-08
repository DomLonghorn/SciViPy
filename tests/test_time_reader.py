from pathlib import Path
import shutil
import difflib

import pytest

from SciViPy import time_reader


@pytest.fixture(scope="module")
def time_reader_dir(tmp_path_factory):
    """
    Copies test_data/time_reader to a new temp directory, returns the path.
    """
    data_dir = Path(__file__).parent / "test_data" / "time_reader"
    tmp_dir = tmp_path_factory.mktemp("time_reader")
    for filename in data_dir.rglob("*.txt"):
        shutil.copy(filename, tmp_dir)
    return tmp_dir


def test_time_reader(time_reader_dir):
    input_file = time_reader_dir / "input.txt"
    expected_file = time_reader_dir / "expected.txt"
    results_file = time_reader_dir / "results.txt"
    time_reader(input_file, results_file, num_points=150, start=4000, end_index=607)
    # Ensure results.txt has been created
    assert results_file.exists()
    # Ensure results.txt and expected.txt match
    with open(expected_file) as f:
        expected = f.readlines()
    with open(results_file) as f:
        results = f.readlines()
    diff = list(difflib.context_diff(expected, results))
    assert not diff, "".join(diff)
