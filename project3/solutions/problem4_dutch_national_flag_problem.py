# Problem 4: Dutch National Flag Problem

def sort_012(input_list):
    # Handle edge cases
    if input_list is None:
        return "The list is either empty or invalid."
    lst_0 = []
    lst_1 = []
    lst_2 = []
    output = []
    for element in input_list:
        
        if element == 0:
            lst_0.append(0)
        elif element == 1:
            lst_1.append(1)
        else:
            lst_2.append(2)
        
    output += lst_0
    output += lst_1
    output += lst_2

    return output

# Run some tests
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([1, 0, 2, 0, 1, 0, 2, 1, 0, 2, 2])
