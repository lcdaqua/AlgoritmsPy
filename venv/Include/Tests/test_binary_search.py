from Include.Classes.BinarySearch import bindary_search

def test_binary_search():
    my_list = [i + 1 for i in range(128)]

    assert bindary_search(my_list) == 0