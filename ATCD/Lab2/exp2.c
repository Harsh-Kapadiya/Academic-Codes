#include <stdio.h>
#include <string.h>
int main(){
    int transition_table[3][2] = {
        {1, 0}, // State 0 transitions
        {2, 0}, // State 1 transitions
        {2, 2}  // State 2 transitions
    };
    int current_state = 0; 
    char input_string[100];
    printf("Enter a binary string: ");
    scanf("%s", input_string);
    int length = strlen(input_string);
    for(int i = 0; i < length; i++){
        char symbol = input_string[i];
        if(symbol == '0'){
            current_state = transition_table[current_state][0];
        } else if(symbol == '1'){
            current_state = transition_table[current_state][1];
        } else {
            printf("Invalid input symbol: %c\n", symbol);
            return 1;
        }
    }
    if(current_state == 1){
        printf("The string is accepted by the DFA.\n");
    } else {
        printf("The string is rejected by the DFA.\n");
    }
    return 0;
}