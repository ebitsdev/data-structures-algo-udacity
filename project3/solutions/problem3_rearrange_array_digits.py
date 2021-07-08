# We create 2 utility functions to merge and sort the list elements
# And use the second utility to merge the right and left sides of the provided list
def m_sort_nums(n_lst):
    # Check if the list is empty or only has one element.
    if len(n_lst) <= 1:
        return n_lst
    half = len(n_lst) // 2
    l_side = n_lst[:half]
    r_side = n_lst[half:]

    l_side = m_sort_nums(l_side)
    r_side = m_sort_nums(r_side)

    return merge_nums(l_side, r_side)

def merge_nums(l_side, r_side):
    m_numbers = []
    r_idx = 0
    l_idx = 0

    while l_idx < len(l_side) and r_idx < len(r_side):
        if l_side[l_idx] > r_side[r_idx]:
            m_numbers.append(r_side[r_idx])
            r_idx += 1
        else:
            m_numbers.append(l_side[l_idx])
            l_idx += 1
    m_numbers += l_side[l_idx:]
    m_numbers += r_side[r_idx:]

    return m_numbers

def rearrange_digits(input_list):
    input_list = m_sort_nums(input_list)
    length = len(input_list)
    # Handle cases where the list contains only 1 digit
    if length <= 1:
        return [-1, -1]
    idx = length - 1
    first_output = ""
    second_output = ""

    while idx >= 0:
        #Check if the index is an even number
        if idx % 2 == 0:
            first_output += str(input_list[idx])
        else:
            second_output += str(input_list[idx])
        idx -= 1

    if first_output > second_output:
        return list(map(int, [first_output, second_output]))
    return list(map(int, [second_output, first_output]))


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[1, 0, 8], [80, 1]])
test_function([[9, 0, 3, 5, 2, 1], [931, 520]])
test_function([[1, 6, 3, 2, 5], [631, 52]])
test_function([[1, 3, 2], [-1, -1]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
