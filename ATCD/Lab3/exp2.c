#include <stdio.h>
#include <string.h>

#define MAX_STATES 10
#define MAX_SYMBOLS 5

// NFA[state][symbol][state]
int nfa[MAX_STATES][MAX_SYMBOLS][MAX_STATES];

// DFA states as sets
int dfa_states[MAX_STATES][MAX_STATES];
int dfa_count = 0;

// Check if DFA state already exists
int isPresent(int state_set[], int nfa_states)
{
    for (int i = 0; i < dfa_count; i++)
    {
        if (memcmp(dfa_states[i], state_set, sizeof(int) * nfa_states) == 0)
            return i;
    }
    return -1;
}

int main()
{
    int states, symbols;
    int i, j, k;

    printf("Enter number of states: ");
    scanf("%d", &states);

    printf("Enter number of symbols: ");
    scanf("%d", &symbols);

    memset(nfa, 0, sizeof(nfa));

    printf("\n### Transition table ###\n");

    // ---------- TABLE STYLE INPUT ----------
    for (i = 0; i < states; i++)
    {
        printf("At State q%d:\n", i);

        for (j = 0; j < symbols; j++)
        {
            int next;
            printf("On Symbol %d State is q", j + 1);
            scanf("%d", &next);

            // single transition NFA
            nfa[i][j][next] = 1;

            // echo input (as shown in your screenshot)
            printf("%d\n", next);
        }
    }

    // ---------- DFA CONSTRUCTION ----------
    int queue[MAX_STATES][MAX_STATES];
    int front = 0, rear = 0;

    // Start DFA state = {q0}
    memset(queue[rear], 0, sizeof(queue[rear]));
    queue[rear][0] = 1;

    memcpy(dfa_states[dfa_count++], queue[rear], sizeof(int) * states);
    rear++;

    while (front < rear)
    {
        int current[MAX_STATES];
        memcpy(current, queue[front++], sizeof(int) * states);

        for (j = 0; j < symbols; j++)
        {
            int new_state[MAX_STATES] = {0};

            for (i = 0; i < states; i++)
            {
                if (current[i])
                {
                    for (k = 0; k < states; k++)
                    {
                        if (nfa[i][j][k])
                            new_state[k] = 1;
                    }
                }
            }

            if (isPresent(new_state, states) == -1)
            {
                memcpy(queue[rear], new_state, sizeof(int) * states);
                memcpy(dfa_states[dfa_count++], new_state, sizeof(int) * states);
                rear++;
            }
        }
    }

    // ---------- PRINT DFA STATES ----------
    printf("\nDFA States:\n");
    for (i = 0; i < dfa_count; i++)
    {
        printf("State %d: { ", i);
        for (j = 0; j < states; j++)
        {
            if (dfa_states[i][j])
                printf("q%d ", j);
        }
        printf("}\n");
    }

    return 0;
}