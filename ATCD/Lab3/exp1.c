#include <stdio.h>
#include <string.h>
#define MAX_STATES 10
#define MAX_SYMBOLS 5
int nfa[MAX_STATES][MAX_SYMBOLS][MAX_STATES];
int nfa_states, symbols;
int dfa[MAX_STATES][MAX_SYMBOLS][MAX_STATES];
int dfa_states = 0;
/* Check if a DFA state already exists */
int isPresent(int state_set[MAX_STATES])
{
    for (int i = 0; i < dfa_states; i++)
    {
        if (memcmp(dfa[i][0], state_set, sizeof(int) * MAX_STATES) == 0)
            return i;
    }
    return -1;
}
int main()
{
    int i, j, k;
    printf("Enter number of NFA states: ");
    scanf("%d", &nfa_states);
    printf("Enter number of input symbols: ");
    scanf("%d", &symbols);
    printf("Enter NFA transition table:\n");
    printf("(Enter 1 if transition exists, else 0)\n");
    for (i = 0; i < nfa_states; i++)
    {
        for (j = 0; j < symbols; j++)
        {
            printf("From state %d on symbol %d:\n", i, j);
            for (k = 0; k < nfa_states; k++)
            {
                scanf("%d", &nfa[i][j][k]);
            }
        }
    }
    int queue[MAX_STATES][MAX_STATES];
    int front = 0, rear = 0;
    /* Start DFA state = {0} */
    memset(queue[rear], 0, sizeof(queue[rear]));
    queue[rear][0] = 1;
    memcpy(dfa[dfa_states++][0], queue[rear], sizeof(queue[rear]));
    rear++;
    while (front < rear)
    {
        int current[MAX_STATES];
        memcpy(current, queue[front++], sizeof(current));
        for (j = 0; j < symbols; j++)
        {
            int new_state[MAX_STATES] = {0};
            for (i = 0; i < nfa_states; i++)
            {
                if (current[i])
                {
                    for (k = 0; k < nfa_states; k++)
                    {
                        if (nfa[i][j][k])
                            new_state[k] = 1;
                    }
                }
            }
            if (isPresent(new_state) == -1)
            {
                memcpy(queue[rear], new_state, sizeof(new_state));
                memcpy(dfa[dfa_states++][0], new_state, sizeof(new_state));
                rear++;
            }
        }
    }
    /* Print DFA States */
    printf("\nDFA States:\n");
    for (i = 0; i < dfa_states; i++)
    {
        printf("State %d: { ", i);
        for (j = 0; j < nfa_states; j++)
        {
            if (dfa[i][0][j])
                printf("%d ", j);
        }
        printf("}\n");
    }
    return 0;
}