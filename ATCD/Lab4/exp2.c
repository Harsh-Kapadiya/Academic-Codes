#include <stdio.h>

int main()
{
    int state, symbol, i, j, start;

    printf("Enter the number of states: ");
    scanf("%d", &state);

    printf("Enter the number of input symbols: ");
    scanf("%d", &symbol);

    char sym[symbol];

    // Input symbols
    for (i = 0; i < symbol; i++)
    {
        printf("Enter input symbol %d: ", i + 1);
        scanf(" %c", &sym[i]);
    }

    int dfa[state][symbol];

    // Transition table input
    printf("\nEnter transition table (row-wise):\n");
    printf("States are Q0 to Q%d\n", state - 1);
    printf("Enter only state numbers\n\n");

    for (i = 0; i < state; i++)
    {
        printf("For state Q%d: ", i);
        for (j = 0; j < symbol; j++)
        {
            scanf("%d", &dfa[i][j]);
        }
    }

    printf("\nEnter the start state: ");
    scanf("%d", &start);

    int final[state];
    printf("Enter final states (1 = final, 0 = non-final):\n");
    for (i = 0; i < state; i++)
    {
        printf("Is Q%d final? ", i);
        scanf("%d", &final[i]);
    }

    // Regular Grammar Output
    printf("\nRegular Grammar Productions:\n");

    for (i = 0; i < state; i++)
    {
        for (j = 0; j < symbol; j++)
        {
            printf("Q%d -> %c Q%d", i, sym[j], dfa[i][j]);
            if (final[dfa[i][j]])
            {
                printf(" | %c", sym[j]);
            }
            printf("\n");
        }
    }

    return 0;
}