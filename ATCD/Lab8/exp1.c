#include <stdio.h>
#include <string.h>
#define MAX 100
char stack[MAX];
int top = -1;
void push(char c)
{
    if (top == MAX - 1)
    {
        printf("Stack Overflow\n");
    }
    else
    {
        stack[++top] = c;
    }
}

void pop()
{
    if (top == -1)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        top--;
    }
}

int isBalanced(char *exp)
{
    int i;
    for (i = 0; exp[i] != '\0'; i++)
    {
        if (exp[i] == '(' || exp[i] == '{' || exp[i] == '[')
        {
            push(exp[i]);
        }
        else if (exp[i] == ')' || exp[i] == '}' || exp[i] == ']')
        {
            if (top == -1)
            {
                return 0;
            }
            char topChar = stack[top];
            pop();
            if ((exp[i] == ')' && topChar != '(') ||
                (exp[i] == '}' && topChar != '{') ||
                (exp[i] == ']' && topChar != '['))
            {
                return 0;
            }
        }
    }
    return top == -1;
}
int main()
{
    char exp[MAX];
    printf("Enter an expression: ");
    fgets(exp, MAX, stdin);
    exp[strcspn(exp, "\n")] = '\0'; // Remove newline character
    if (isBalanced(exp))
    {
        printf("The expression is balanced.\n");
    }
    else
    {
        printf("The expression is not balanced.\n");
    }
    return 0;
}