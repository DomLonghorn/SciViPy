import shutil
from pathlib import Path

import pytest

from SciViPy import make_gif


@pytest.fixture(scope="module")
def make_gif_dir(tmp_path_factory):
    """
    Copies test_data/make_gif_data to a new temp directory and returns the new path.

    As make_gif writes to the same directory it reads data from, we can't use the
    directory test_data/make_gif directly, as after the first run
    """
    data_dir = Path(__file__).parent / "test_data" / "make_gif"
    tmp_dir = tmp_path_factory.mktemp("make_gif")
    for filename in data_dir.rglob("*.png"):
        shutil.copy(filename, tmp_dir)
    return tmp_dir


def test_make_gif(make_gif_dir):
    gif = make_gif(make_gif_dir)
    assert gif.exists()
    assert gif.suffix == ".gif"
