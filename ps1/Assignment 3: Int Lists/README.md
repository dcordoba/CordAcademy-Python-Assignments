# Summary
In this assignment, you will be working with lists of integers. You will
implement a few common statistical operations using lists of numbers.

# Tasks
You will implement the following operations: min, max, median, mode, floor, and
ceil.

## Min
Implement a function that, given a list, returns the smallest element in the
list. You can assume the list will be a valid list of integers.

## Max
Same as min, but returns the largest integer in the list.

## Median
Returns the median element in the list. If the list has an even amount of
elements, return either of the two median elements.

## Mode
Returns the most common element in the list. If there is a tie, return either of
the tied elements.

## Floor
Given a number and a list, returns a the next smallest number in the list. If
the given number is in the list, return that number.

Ex.
```
get_floor([5, 10, 12, 7, 2], 8) returns 7
get_floor([1, 2, 3], 2) returns 2
```

## Ceil
Given a number and a list, returns a the next largest number in the list. If
the given number is in the list, return that number.

Ex.
```
get_ceil([5, 10, 12, 7, 2], 8) returns 10
get_ceil([1, 2, 3], 2) returns 2
```

# Running and Testing
We have included a few test cases to ensure that your implementations are
correct. Once you have made your changes, run the program to test.

```
> python main.py
All tests passed!
```
