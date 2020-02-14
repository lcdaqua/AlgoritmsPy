from Include.Classes.MassiveSum import sum

def test_sum():
    my_list = [i + 1 for i in range(9)]
    assert sum(my_list) == 45