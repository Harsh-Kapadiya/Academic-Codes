/*
REGEX TO DFA
Steps:
1. Convert regex to NFA (Thompson’s construction)
2. Convert NFA to DFA (subset construction)
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100
#define STATES 50

int dfa[STATES][2];
int nfa[STATES][2][STATES];
int nfa_states = 0;
int dfa_states = 0;

int isPresent(int set[], int n, int x)
{
    for(int i=0;i<n;i++)
        if(set[i]==x) return 1;
    return 0;
}

void addTransition(int from, int symbol, int to)
{
    nfa[from][symbol][to] = 1;
}

int main()
{
    char regex[50];
    printf("Enter simple regex (a,b,|,.,*): ");
    scanf("%s", regex);

    printf("\n--- DFA Construction (Simplified Demonstration) ---\n");

    /*
      For lab purpose:
      Instead of full Thompson implementation,
      we simulate subset construction explanation.
    */

    printf("States created sequentially for each symbol.\n");

    int current = 0;

    for(int i=0; i<strlen(regex);i++)
    {
        if(regex[i]=='a' || regex[i]=='b')
        {
            printf("q%d -- %c --> q%d\n", current, regex[i], current+1);
            current++;
        }
    }

    printf("\nStart state : q0\n");
    printf("Final state : q%d\n", current);

    return 0;
}