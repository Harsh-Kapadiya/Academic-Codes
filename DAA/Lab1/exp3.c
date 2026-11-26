#include <stdio.h>
#include <time.h>

int main() {
    clock_t start, end;
    double cpu_time_used;

    start = clock(); // Record the start time

    /* Code block to measure */
    for (int i = 0; i < 444000000; i++) {
        // do some stuff
    }

    end = clock(); // Record the end time

    // Calculate the elapsed time in seconds
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Time taken: %lf seconds\n", cpu_time_used);

    return 0;
}
