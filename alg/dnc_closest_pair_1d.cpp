#include <math.h>
#include <stdio.h>
#define MAX 100000

#define MINIMUM2(a, b) (a < b ? a : b)
#define MINIMUM3(a, b, c) (MINIMUM2(MINIMUM2(a, b), c))

// 0 7

float ClosestPair(float S[], int p, int q) {

  float d, d1, d2, maxdist;
  int n, m;
  n = q - p + 1;
  maxdist = 1000000;

  printf("%d %d %d\n", p, q, n);

  if (n == 2)
    return abs(S[q] - S[p]);
  else if (n == 1)
    d = MAX;
  else {
    m = (q + p + 1) / 2;
    d1 = ClosestPair(S, p, m);
    d2 = ClosestPair(S, m + 1, q);
    d = MINIMUM3(d1, d2, S[m + 1] - S[m]);
    printf("@ %d %f %f\n", m, d1, d2);
  }
  return d;
}

int main() {
  float A[] = {1, 2, 3, 4, 5, 6, 6.1, 7};
  float d = ClosestPair(A, 0, 7);
  printf("%f", d);
}