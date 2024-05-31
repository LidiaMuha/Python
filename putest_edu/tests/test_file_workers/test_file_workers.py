from my_funcs.file_workers import read_from_file


def create_test_date(test_data):
    with open("testfile_copy_of_prodfile.txt", "a") as f_o:
        f_o.writelines(test_data)


def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three\n']
    create_test_date(test_data)
    assert test_data == read_from_file("testfile_copy_of_prodfile.txt")


def test_read_from_file_2():
    test_data = ['one\n', 'two\n', 'three\n', 'four\n']
    create_test_date(test_data)
    assert test_data == read_from_file("testfile_copy_of_prodfile.txt")
