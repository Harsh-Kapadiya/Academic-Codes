#include <stdio.h>
int sum_to(int n)
{
    if (n == 2)
        return 1;
    if (n == 3)
        return 2;
    int k = 1;
    while (n > 4)
    {
        k*= 3;
        n -= 3;
    }
    k *= n;
    return k;
}
int main()
{
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    printf("Maximum product: %d\n", sum_to(n));
    return 0;
}