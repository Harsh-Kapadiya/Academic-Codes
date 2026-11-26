#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX 100

char stack[MAX];
int top = -1;

void push(char c) {
    if (top < MAX - 1) stack[++top] = c;
}

char pop() {
    return (top >= 0) ? stack[top--] : '\0';
}

bool is_accepted(char *input) {
    int i = 0;
    int n = strlen(input);

    // Phase 1: Push 0s and 1s onto stack until a non-binary character is found
    while (i < n && (input[i] == '0' || input[i] == '1')) {
        push(input[i]);
        i++;
    }

    // Phase 2: Treat the current character as the separator 'C'
    // If we reached the end without a separator, or if the separator is a 0/1 (logic-wise), reject.
    if (i == n || input[i] == '0' || input[i] == '1') {
        return false; 
    }
    
    printf("Detected separator: '%c'\n", input[i]);
    i++; // Skip the separator

    // Phase 3: Match the remaining input against the stack
    while (i < n) {
        if (pop() != input[i]) {
            return false; 
        }
        i++;
    }

    // Accept only if stack is empty (perfect match)
    return (top == -1);
}

int main() {
    char input[MAX];
    printf("Enter string (e.g., 101#101 or 00X00): ");
    scanf("%s", input);

    if (is_accepted(input)) {
        printf("Result: Accepted!\n");
    } else {
        printf("Result: Rejected.\n");
    }

    return 0;
}