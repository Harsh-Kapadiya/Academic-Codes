#include <stdio.h>

int max(int a, int b)
{
    return (a > b) ? a : b;
}

int rodCutting(int prices[], int n)
{
    int dp[n + 1];

    dp[0] = 0;

    for (int i = 1; i <= n; i++)
    {
        dp[i] = 0;
        for (int j = 1; j <= i; j++)
        {
            dp[i] = max(dp[i], prices[j - 1] + dp[i - j]);
        }
    }

    return dp[n];
}

int main()
{
    int n;

    printf("Enter the length of the rod: ");
    scanf("%d", &n);

    int prices[n];

    printf("Enter the prices for lengths 1 to %d:\n", n);
    for (int i = 0; i < n; i++)
    {
        printf("Price of length %d: ", i + 1);
        scanf("%d", &prices[i]);
    }

    int result = rodCutting(prices, n);

    printf("\nMaximum obtainable profit = %d\n", result);

    return 0;
}