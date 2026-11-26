#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Seed the random number generator using the current time
    // This should only be called once per program execution
    srand(time(NULL));

    // Generate a random number between 1 and 100
    int random_num = (rand() % 100) + 1;

    printf("Random number between 1 and 100: %d\n", random_num);

    return 0;
}
