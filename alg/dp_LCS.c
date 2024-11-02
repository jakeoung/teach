#include <stdio.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

char X[] = "spanking";
char Y[] = "amputation";
int cnt_call = 0;

int LCS_recursive(int m, int n) {
  // printf("(%d, %d) ", m, n);
  cnt_call++;
  if (m == 0 || n == 0)
    return 0;
  else if (X[m] == Y[n]) {
    // printf("%c", X[m]);
    return LCS_recursive(m - 1, n - 1) + 1;
  } else {
    return MAX(LCS_recursive(m - 1, n), LCS_recursive(m, n - 1));
  }
}

int main(void) {
  int m = 9;
  int n = 11;
  int table[9][11] = {0};

  // top-down
  printf("\n\nSolution by a recursive function: %d\n",
         LCS_recursive(m - 2, n - 2));
  printf("The recursive function is called %d times\n", cnt_call);

  // bottom-up
  for (int i = 0; i < m; i++)
    table[i][0] = 0;

  for (int j = 0; j < n; j++)
    table[0][j] = 0;

  for (int i = 1; i < m; i++) {
    for (int j = 1; j < n; j++) {
      if (X[i - 1] == Y[j - 1]) {
        table[i][j] = table[i - 1][j - 1] + 1;
      } else {
        if (table[i - 1][j] > table[i][j - 1])
          table[i][j] = table[i - 1][j];
        else
          table[i][j] = table[i][j - 1];
      }
    }
  }

  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      printf("%d ", table[i][j]);
    }
    printf("\n");
  }

  // Exercise
  // From the dynamic programming solution, modify the code to find a largest
  // common subsequence.

  
  return 0;
}