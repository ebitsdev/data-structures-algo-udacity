#Complete this function

def floorSqrt(num): 
    # lowest boundary
    lnum = 1
    # highest boundary
    hnum = num
    fl_floorSqrt = -1
    while(lnum <= hnum):
        mnum = (lnum + hnum) // 2
        sqroot = mnum * mnum
        if (sqroot == num):
            return mnum
        elif(sqroot < num):
            fl_floorSqrt = mnum
            lnum = mnum + 1
        else:
            hnum = mnum - 1
    return fl_floorSqrt
# Call the function and print output the result to test for different cases
print ("Pass" if  (3 == floorSqrt(9)) else "Fail")
print ("Pass" if  (0 == floorSqrt(0)) else "Fail")
print ("Pass" if  (4 == floorSqrt(16)) else "Fail")
print ("Pass" if  (1 == floorSqrt(1)) else "Fail")
print ("Pass" if  (5 == floorSqrt(27)) else "Fail")
print ("Pass" if  (6 == floorSqrt(38)) else "Fail")
print ("Pass" if  (2 == floorSqrt(1)) else "Fail")