// This code is largely modified from the original code in Competitive Programming 4 by Steven Halim

#include <stdio.h>
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MAX_N 10
#define MAX_W 100

int W = 50;
int N = 3;
int values[] = {60,100, 120, 20, 30};
int weights[] = {10, 20, 30, 10, 20};

int memo[MAX_N][MAX_W+1]; // memoization table

int cnt_call_recursive = 0;
int cnt_call_dp = 0;
int cnt_call_bb = 0;
 
int f(int i, float remW)
{
    cnt_call_recursive++;

    if (remW == 0 || i >= N) // base case
        return 0;

    int ans = f(i+1, remW); // not take 

    if (weights[i] <= remW) // if available, take
        ans = MAX(ans, values[i] + f(i+1, remW - weights[i]));

    return ans;
}

int dp(int id, int remW) { // remW: remaining weight left
    cnt_call_dp++;

    if (remW == 0 || i >= N) // base case
        return 0;

    int *ans = &memo[id][remW];
    if (*ans != -1) return *ans; // memoization check

    if (weights[id] <= remW) // if available, take
        return *ans = MAX(dp(id+1, remW),   // has choice, skip
                    values[id]+dp(id+1, remW - weights[id])); // or take  

    else
        return *ans = dp(id+1, remW); // no choice, skip
}

int dp_tabulation()
{
    int table[N][W+1];
    for (int i = 0; i < N; ++i) table[i][0] = 0;
    for (int w = 0; w <= W; ++w) table[0][w] = 0;

    for (int i = 1; i < N; i++) {
        for (int w = 1; w <= W; w++) {
            if (weights[i-1] <= w)
                table[i][w] = MAX(table[i-1][w], values[i-1] + table[i-1][w-weights[i-1]]);

            else
                table[i][w] = table[i-1][w];
        }
    }
    return table[N-1][W];
}

// Make a code using branch and bound approach to solve the knapsack problem


int main() {
    int answer;
    answer = f(0, W);
    printf("%d: Solution by complete search\n", answer);
    printf("%d: cnt_call_recursive\n\n", cnt_call_recursive);

    // initalize memoization table
    for (int i = 0; i < N; i++)
        for (int j = 0; j < W+1; j++)
            memo[i][j] = -1;

    answer = dp(0, W);
    printf("%d: Solution by dynamic programming with top-down\n", answer);
    printf("%d: cnt_call_dp\n\n", cnt_call_dp);

    answer = dp_tabulation();
    printf("%d: Solution by dynamic programming with bottom-up\n", answer);
    printf("%d: table size of N*(W+1)\n\n", N*(W+1));

    answer = branch_and_bound(0, W, 0);
    printf("%d: Solution by branch and bound\n", answer);
    printf("%d: cnt_call_bb\n\n", cnt_call_bb);

    return 0;
}