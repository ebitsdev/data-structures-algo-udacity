def get_min_max(ints):
    # Let us setup initial variables for the minimum and maximum values
    minval = ints[0]
    maxval = ints[0]

    for intnum in ints:
        if intnum < minval:
            minval = intnum
        elif intnum > maxval:
            maxval = intnum
    return minval, maxval

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
l2 = [225, 0, 5, 7, 99]
l3 = [3600, 11, 6, 55, 8970]
l4 = [8888, 5, 9, 1, 1500]
l5 = [0, 0]
random.shuffle(l)
# Test case 1
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Test case 2
print ("Pass" if ((0, 225) == get_min_max(l2)) else "Fail")
# Test case 3
print ("Pass" if ((6, 8970) == get_min_max(l3)) else "Fail")
# Test case 4
print ("Pass" if ((1, 8888) == get_min_max(l4)) else "Fail")
# Test case 5
print ("Pass" if ((0, -1) == get_min_max(l5)) else "Fail") # This will fail