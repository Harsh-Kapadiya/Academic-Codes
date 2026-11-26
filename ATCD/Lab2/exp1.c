#include <stdio.h>
#include <string.h>

int main()
{
    // Transition table: states q0, q1, q2 and inputs 0, 1
    int transition[3][2] = {
        {0, 1}, // q0
        {2, 1}, // q1c
        {0, 1}  // q2
    };

    char input[100];
    int currentState = 0; // Start state q0

    printf("Enter the input string (0s and 1s only): ");
    scanf("%99s", input);   // prevents buffer overflow

    int length = strlen(input);

    for (int i = 0; i < length; i++)
    {
        if (input[i] != '0' && input[i] != '1')
        {
            printf("Invalid input symbol detected. DFA accepts only 0 and 1.\n");
            return 0;
        }

        int symbol = input[i] - '0';
        currentState = transition[currentState][symbol];
    }

    // Accepting state: q1
    if (currentState == 1)
        printf("String is ACCEPTED by the DFA\n");
    else
        printf("String is REJECTED by the DFA\n");

    return 0;
}
