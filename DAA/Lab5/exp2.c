#include <stdio.h>
void fibonacci_dp(int n)
{
    if (n <= 0)
    {
        printf("Please enter a positive integer.\n");
        return;
    }
    int fib[n + 1];
    fib[0] = 0;
    if (n > 0)
    {
        fib[1] = 1;
    }
    for (int i = 2; i <= n; i++)
    {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    printf("Fibonacci Series using Dynamic Programming (Bottom-Up):\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d, ", fib[i]);
    }
    printf("%d\n", fib[n]);
}

int main()
{
    int n;
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    fibonacci_dp(n - 1);
    return 0;
}
