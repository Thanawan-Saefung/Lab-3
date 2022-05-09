import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 100, 110, 120]
    test_arr = [11, 12, 22, 25, 34, 64, 90, 100, 110, 120]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)


def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 100, 110, 120]
    test_arr = [120, 110, 100, 90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)


def test_bubble_sort_excess_element():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 100, 110, 120, 130]
    test_arr = 1

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)


def test_bubble_sort_insufficient_element():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = 2

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)


def test_bubble_sort_no_element():
    result = []
    input_arr = []
    test_arr = 0

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)


def test_bubble_sort_not_int():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 100, 110, 'a']
    test_arr = 3

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)