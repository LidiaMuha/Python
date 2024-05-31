import pytest


@pytest.fixture(autouse=True)
def clean_text_file():
    with open('testfile_copy_of_prodfile.txt', "w"):
        pass