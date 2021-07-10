# Problem 4: Dutch National Flag Problem

def sort_zero_one_two(input_list):
    # We define 4 variables for the low, middle, high, and temporary values
    lo_end = 0
    hi_end = len(input_list) - 1
    mid = 0
    tmp = None
    if len(input_list) <= 0 or input_list[mid] < 0:
        return "The list is either empty or invalid."
    
    while (mid <= hi_end):                 
        
        if input_list[mid] == 0:
            tmp = input_list[lo_end]
            input_list[lo_end] = input_list[mid]
            input_list[mid] = tmp
            lo_end += 1
            mid += 1
            
        elif input_list[mid] == 1:
            mid += 1            
        else:
            tmp = input_list[mid]
            input_list[mid] = input_list[hi_end]
            input_list[hi_end] = tmp
            hi_end -= 1

    return input_list            

# Run some tests
def test_function(test_case):
    sorted_array = sort_zero_one_two(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([1, 0, 2, 0, 1, 0, 2, 1, 0, 2, 2])
test_function([])
test_function([-1])