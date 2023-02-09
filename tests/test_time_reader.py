from pathlib import Path

import numpy as np
import pytest

from SciViPy import time_reader


@pytest.fixture(scope="module")
def time_reader_dir():
    return Path(__file__).parent / "test_data" / "time_reader"


def test_time_reader(time_reader_dir):
    input_file = time_reader_dir / "input.txt"
    expected_file = time_reader_dir / "expected.txt"
    results = time_reader(input_file, num_points=150, end_index=607)
    # Ensure results and expected.txt match
    expected = np.loadtxt(expected_file, dtype=int)
    np.testing.assert_array_equal(expected, results["index"])
