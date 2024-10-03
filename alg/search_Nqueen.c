#include <stdio.h>
#include <stdlib.h>
#define N 4

int row[N];
int cnt = 0;;

int check(int r, int c) {
    for (int i = 0; i < r; i++) {
        if (row[i] == c || abs(row[i] - c) == abs(i - r)) {
            return 0;
        }
    }
    return 1;
}

void print_chess() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%c", j == row[i] ? 'Q' : '.');
        }
        printf("\n");
    }
    printf("\n");
}

void search(int r) {
    if (r == N) {
        print_chess();
        cnt++;
        return;
    }
    for (int col = 0; col < N; col++) {
        if (check(r, col)) {
            row[r] = col;
            search(r + 1);
        }
    }
}

int main() {
    search(0);

    printf("%d\n", cnt);
    return 0;
}