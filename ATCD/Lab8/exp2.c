#include <stdio.h>
#include <string.h>

#define MAX 100

char stack[MAX];
int top = -1;

// Push operation
void push(char c) {
    if (top == MAX - 1) {
        printf("Stack Overflow\n");
        return;
    }
    stack[++top] = c;
}

// Pop operation
char pop() {
    if (top == -1) {
        return '\0'; // empty stack
    }
    return stack[top--];
}
int isValid(char *str) {
    int i = 0;

    // Step 1: Push all 'a'
    while (str[i] == 'a') {
        push('a');
        i++;
    }
    while (str[i] == 'b') {
        if (top == -1) {
            return 0; //
        }
        pop();
        i++;
    }
    if (str[i] == '\0' && top == -1) {
        return 1; // valid
    }

    return 0; // invalid
}

int main() {
    char str[MAX];

    printf("Enter string: ");
    scanf("%s", str);

    if (isValid(str)) {
        printf("String belongs to L = a^n b^n\n");
    } else {
        printf("String does NOT belong to L = a^n b^n\n");
    }

    return 0;
}