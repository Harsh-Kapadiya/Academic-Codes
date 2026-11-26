#include <stdio.h>
#include <ctype.h>
#include <string.h>
// DFA for mobile number (10 digits)
int validateMobile(char *str)
{
    int state = 0;
    for (int i = 0; str[i] != '\0'; i++)
    {
        char c = str[i];
        switch (state)
        {
        case 0:
            if (isdigit(c))
                state = 1;
            else
                return 0;
            break;
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
        case 7:
        case 8:
        case 9:
            if (isdigit(c))
                state++;
            else
                return 0;
            break;
        default:
            return 0;
        }
    }
    if (state == 10)
        return 1;
    else
        return 0;
}
// NFA-style email validation
int validateEmail(char *str)
{
    int i = 0, state = 0;
    while (str[i] != '\0')
    {
        char c = str[i];
        switch (state)
        {
        // username
        case 0:
            if (isalnum(c) || c == '.' || c == '_')
                state = 0;
            else if (c == '@')
                state = 1;
            else
                return 0;
            break;
        // domain
        case 1:
            if (isalpha(c))
                state = 2;
            else
                return 0;
            break;
        case 2:
            if (isalpha(c))
                state = 2;
            else if (c == '.')
                state = 3;
            else
                return 0;
            break;
        // extension
        case 3:
            if (isalpha(c))
                state = 4;
            else
                return 0;
            break;
        case 4:
            if (isalpha(c))
                state = 4;
            else
                return 0;
            break;
        }
        i++;
    }
    if (state == 4)
        return 1;
    else
        return 0;
}
int main()
{
    char email[100];
    char phone[20];
    printf("Enter Email: ");
    scanf("%s", email);
    if (validateEmail(email))
        printf("Valid Email\n");
    else
        printf("Invalid Email\n");
    printf("Enter Mobile Number: ");
    scanf("%s", phone);
    if (validateMobile(phone))
        printf("Valid Mobile Number\n");
    else
        printf("Invalid Mobile Number\n");
    return 0;
}
