#include <stdio.h>
#include <string.h>

#define CASE 2

#if CASE == 1
int cost_copy = 5;
int cost_insert = 10;
int cost_delete = 10;
#elif CASE == 2
// Last example
int cost_copy = 0;
int cost_insert = 1;
int cost_delete = 1;
#endif

// Utility function to find minimum of three numbers
int min3(int x, int y, int z) {
  return x <= y ? (x <= z ? x : z) : (y <= z ? y : z);
}

int min(int x, int y) { return x <= y ? x : y; }

int edit_distance(char *str1, char *str2, int m, int n) {
  if (m == 0)
    return n * cost_insert;

  if (n == 0)
    return m * cost_delete;

  if (str1[m - 1] == str2[n - 1]) // Copy
    return edit_distance(str1, str2, m - 1, n - 1) + cost_copy;

  return min(edit_distance(str1, str2, m, n - 1) + cost_insert, // Insert
             edit_distance(str1, str2, m - 1, n) + cost_delete  // Remove
  );
}

// Driver code
int main() {
#if CASE == 1
  char str1[] = "algori";
  char str2[] = "al";
#elif CASE == 2
  char str1[] = "monkey";
  char str2[] = "money";
#endif

  int m = strlen(str1);
  int n = strlen(str2);
  int table[n + 1][m + 1];

  // First approach: using recursive function
  printf("Edit distance by recursion: %d\n\n", edit_distance(str1, str2, m, n));

  // Second approach: dynamic programming
  for (int i = 0; i <= n; i++)
    table[i][0] = i * cost_insert;

  for (int j = 0; j <= m; j++)
    table[0][j] = j * cost_delete;

  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      int temp;
      if (str1[j - 1] == str2[i - 1]) // Be careful str1 uses j!
        temp = cost_copy;
      else
        temp = 100; // it should be changed

      table[i][j] =
          min3(cost_delete + table[i][j - 1], cost_insert + table[i - 1][j],
              table[i - 1][j - 1] + temp);
    }
  }

  // print the table
  for (int i = 0; i <= n; i++) {
    for (int j = 0; j <= m; j++) {
      printf("%d ", table[i][j]);
    }
    printf("\n");
  }

  /* Exercise
   * From the dynamic programming solution, modify the code to find a sequence
   * of operations:
   * e.g.: For transforming "algori" to "al", the output can be
   * Copy Copy Delete Delete Delete Delete
   */

  return 0;
}