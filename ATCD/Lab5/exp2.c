#include <stdio.h>
#include <string.h>

int main()
{
    int n, i;
    char line[50];
    char lhs, rhs1, rhs2;

    printf("Enter number of productions: ");
    scanf("%d", &n);
    getchar(); // clear newline from buffer

    printf("\nEnter productions (Example: S a A or S a):\n");
    printf("\nDFA Transitions:\n");
    printf("-----------------\n");

    for (i = 0; i < n; i++)
    {
        fgets(line, sizeof(line), stdin);

        // Try reading 3 symbols first
        if (sscanf(line, " %c %c %c", &lhs, &rhs1, &rhs2) == 3 &&
            rhs2 >= 'A' && rhs2 <= 'Z')
        {
            // A → aB
            printf("δ(%c, %c) = %c\n", lhs, rhs1, rhs2);
        }
        else if (sscanf(line, " %c %c", &lhs, &rhs1) == 2)
        {
            // A → a
            printf("δ(%c, %c) = F\n", lhs, rhs1);
        }
        else
        {
            printf("Invalid production format\n");
        }
    }

    printf("\nStart State: S");
    printf("\nFinal State: F\n");

    return 0;
}