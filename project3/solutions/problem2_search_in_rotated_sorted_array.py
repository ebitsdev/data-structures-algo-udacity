# Project 3: Problems vs Algorithms
# Problem 2: Search in a Rotated Sorted Array

# We will use few utility functions to conduct the array

def p_element(lst, btm, top):
    # Search for the p element's index in the array and return it
    if top < btm:
        return -1
    if top == btm:
        return btm
    else:
        m_idx = (btm + top) // 2
        if m_idx < top and lst[m_idx] > lst[m_idx + 1]:
            return m_idx
        if m_idx > btm and lst[m_idx - 1] > lst[m_idx]:
            return m_idx - 1
        if lst[btm] >= lst[m_idx]:
            return p_element(lst, btm, m_idx - 1)
        # Use recurvise call
        return p_element(lst, m_idx + 1, top)


def bin_srch(lst, btm, top, num):
    #This utility helps to find the positon of the searched number. If it does find it then we return -1
    if btm > top:
        return -1
    m_idx = (btm + top) // 2

    if lst[m_idx] == num:
        return m_idx
    elif lst[m_idx] > num:
        return bin_srch(lst, btm, m_idx - 1, num)
    # We use recursion to find the searched integer

    return bin_srch(lst, m_idx + 1, top, num)

# Conduct the search in the rotated array

def rotated_array_search(input_list, number):
    if input_list == [] or number is None:
        return -1
    # Setup some variables
    lst = input_list
    btm = 0
    top = len(input_list) - 1
    num = number
    p_el_idx = p_element(lst, btm, top)
    # Check if the array is rotated or not.
    if p_el_idx == - 1:
        return bin_srch(lst, btm, top, num)
    else:
        if lst[p_el_idx] == num:            
            return p_el_idx
        if num >= lst[0]:
            return bin_srch(lst, 0, p_el_idx - 1, num)
    """
    if the middle element of the array is less than the first element, we search the right side of the array
    """
    return bin_srch(lst, p_el_idx + 1, top, num)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[11111], 88997])
test_function([[], 10000])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[], None])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

        


