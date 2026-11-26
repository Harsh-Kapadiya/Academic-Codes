#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    clock_t start, end;
    double cpu_time_used;
    int size;
    // printf("Enter the size of a square matrix: ");
    // scanf("%d", &size);
    int matrix_1[size][size];
    printf("Enter the elements of the first squeare matrix:\n");
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            printf("Enter the element at position (%d, %d): ", i + 1, j + 1);
            scanf("%d", &matrix_1[i][j]);
        }
    }
    int matrix_2[size][size];
    printf("Enter the elements of the first squeare matrix:\n");
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            printf("Enter the element at position (%d, %d): ", i + 1, j + 1);
            scanf("%d", &matrix_2[i][j]);
        }
    }

    start = clock(); // Record the start time

    printf("\n\nThe multiplication of the two matrices is:\n");
    int result[size][size];
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            result[i][j] = 0;
            for (int k = 0; k < size; k++)
            {
                result[i][j] += matrix_1[i][k] * matrix_2[k][j];
            }
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

    end = clock(); // Record the end time
    cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Time taken: %lf seconds\n", cpu_time_used);
    return 0;
}