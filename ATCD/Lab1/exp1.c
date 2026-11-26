// write a c programme to count the number of lines, words and number of character present in the file
#include <stdio.h>
int main()
{
    int words = 0;
    int lines = 0;
    int characters = 0;
    FILE *lab1;
    lab1 = fopen("lab1.txt", "r");
    char myString[500];
    // printf("Content present inside the fileis:\n\n");
    while(fgets(myString, 500, lab1) != NULL){
        // printf("%s", myString);
        lines++;
        for(int i = 0; myString[i] != '\0'; i++){
            characters++;
            if(myString[i] == ' ' || myString[i] == '\n'){
                words++;
            }
        }
    }
    printf("\n\nNumber of lines: %d\n", lines);
    printf("Number of words: %d\n", words);
    printf("Number of characters: %d\n", characters);
    fclose(lab1);
    return 0;
}