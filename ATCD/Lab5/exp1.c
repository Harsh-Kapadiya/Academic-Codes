#include <stdio.h>
#include <string.h>
int main()
{
    int n, i;
    char lhs, rhs1, rhs2;
    printf("Enter number of productions: ");
    scanf("%d", &n);
    printf("\nEnter productions (Example: S a A or S a):\n");
    printf("Enter -1 fo the final state transition\n");
    printf("\nDFA Transitions:\n");
    printf("-----------------\n");
    for (i = 0; i < n; i++)
    {
        scanf(" %c", &lhs); 
        scanf(" %c", &rhs1);
        if (scanf(" %c", &rhs2) == 1 && rhs2 >= 'A' && rhs2 <= 'Z')
        {
            // A → aB
            printf("δ(%c, %c) = %c\n", lhs, rhs1, rhs2);
        }
        else
        {
            // A → a
            printf("δ(%c, %c) = F\n", lhs, rhs1);
        }
    }
    printf("\nStart State: S");
    printf("\nFinal State: F\n");
    return 0;
}