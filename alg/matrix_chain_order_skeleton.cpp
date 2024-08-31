/*

Make a program to solve the minimimum number of matrix multiplications given a sequence of matric sizes.

In the input, the first line indicates the length n of the sequence. The second
line corresponds to p0 p1 ... pn, where the size of the first matrix is p0 x p1
and the second matrix size is p1 x p2 and so on. We have n-1 matrices.

The output is the minimum number of matrix multipplication.

Sample test cases
Input
3
1 2 3

Output
6

---
In this case, we have two matrices of size 1x2 and 2x3. There is only one way to
parenthesize and the minimum number of matrix multiplication is 1x2x3=6

*See test cases
*/

#include <stdio.h>

int main() {
  int n;
  int arr[100];

  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
  }
}