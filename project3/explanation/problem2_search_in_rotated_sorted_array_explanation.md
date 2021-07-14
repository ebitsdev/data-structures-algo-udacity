# Project 3: Problems vs Algorithms

## Problem 2 explanation

To solve the problem at hand, we make use of utility functions to conduct a binary search. The p_element method finds the index of the pivot element of the rotated array.

The search helps to split the array into 2 arrays as left and right.
The binary search is used to search the index of the pivot element of the selected side of the rotated array.

The space complexity is O(n) based on the size of the array that we are handling.
The time complexity is O(log(n)).