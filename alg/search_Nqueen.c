#include <stdio.h>
#include <stdlib.h>
#define N 4

int Q[N]; // Q[i] = j means that the queen in the i-th column is in the j-th row
int cnt=0;

int promising(int c, int r) {
    for (int i = 0; i < c; i++) {
        if (Q[i] == r || abs(Q[i] - r) == abs(i - c)) {
            return 0;
        }
    }
    return 1;
}

void search(int c) {
    if (c == N) {
        // print_chess();
        cnt++;
        return;
    }
    for (int r = 0; r < N; r++) {
        if (promising(c, r)) {
            Q[c] = r;
            search(c + 1);
        }
    }
}
int main() {
    search(0);
    printf("%d", cnt);
    return 0;
}