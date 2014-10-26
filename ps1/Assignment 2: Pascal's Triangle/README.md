# Summary
Write a program that takes a number, n,  as input from the user and prints the
first n rows of Pascal's Triangle.

# What Is Pascal's Triangle
From Wikipedia:

```
The rows of Pascal's triangle are conventionally enumerated starting with row n
= 0 at the top. The entries in each row are numbered from the left beginning
with k = 0 and are usually staggered relative to the numbers in the adjacent
rows. A simple construction of the triangle proceeds in the following manner. On
row 0, write only the number 1. Then, to construct the elements of following
rows, add the number above and to the left with the number above and to the
right to find the new value. If either the number to the right or left is not
present, substitute a zero in its place. For example, the first number in the
first row is 1 (the sum of 0 and 1), whereas the numbers 1 and 3 in the third
row are added to produce the number 4 in the fourth row.
```

See http://en.wikipedia.org/wiki/Pascal's_triangle

# Example Output
Your program should prompt the user for the total number of rows to print.

```
> python main.py
Enter the number of rows to print: 5
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```

