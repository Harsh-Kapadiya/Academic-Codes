#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    clock_t start, end;
    double cpu_time_used;
    int size = 4;
    int matrix_1[size][size];
    printf("Enter the elements of the first squeare matrix of size 4x4:\n");
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            printf("Enter the element at position (%d, %d): ", i + 1, j + 1);
            scanf("%d", &matrix_1[i][j]);
        }
    }
    int matrix_2[size][size];
    printf("Enter the elements of the second squeare matrix of size 4x4:\n");
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {

            printf("Enter the element at position (%d, %d): ", i + 1, j + 1);
            scanf("%d", &matrix_2[i][j]);
        }
    }

    start = clock(); // Record the start time

    int new_size = size / 2;
    int A11[new_size][new_size], A12[new_size][new_size], A21[new_size][new_size], A22[new_size][new_size];
    int B11[new_size][new_size], B12[new_size][new_size], B21[new_size][new_size], B22[new_size][new_size];
 
    // Dividing matrix_1 into 4 submatrices
    for (int i = 0; i < new_size; i++)
    {
        for (int j = 0; j < new_size; j++)
        {
            A11[i][j] = matrix_1[i][j];
            A12[i][j] = matrix_1[i][j + new_size];
            A21[i][j] = matrix_1[i + new_size][j];
            A22[i][j] = matrix_1[i + new_size][j + new_size];

            B11[i][j] = matrix_2[i][j];
            B12[i][j] = matrix_2[i][j + new_size];
            B21[i][j] = matrix_2[i + new_size][j];
            B22[i][j] = matrix_2[i + new_size][j + new_size];
        }
    }
    int M1[new_size][new_size], M2[new_size][new_size], M3[new_size][new_size], M4[new_size][new_size];
    int M5[new_size][new_size], M6[new_size][new_size], M7[new_size][new_size];
    // Calculating M1 to M7:
    for (int i = 0; i < new_size; i++)
    {
        for (int j = 0; j < new_size; j++)
        {
            M1[i][j] = (A11[i][j] + A22[i][j]) * (B11[i][j] + B22[i][j]);
            M2[i][j] = (A21[i][j] + A22[i][j]) * B11[i][j];
            M3[i][j] = A11[i][j] * (B12[i][j] - B22[i][j]);
            M4[i][j] = A22[i][j] * (B21[i][j] - B11[i][j]);
            M5[i][j] = (A11[i][j] + A12[i][j]) * B22[i][j];
            M6[i][j] = (A21[i][j] - A11[i][j]) * (B11[i][j] + B12[i][j]);
            M7[i][j] = (A12[i][j] - A22[i][j]) * (B21[i][j] + B22[i][j]);
        }
    }

    int C11[new_size][new_size], C12[new_size][new_size], C21[new_size][new_size], C22[new_size][new_size];
    // Calculating C11, C12, C21, C22:
    for (int i = 0; i < new_size; i++)
    {
        for (int j = 0; j < new_size; j++)
        {
            C11[i][j] = M1[i][j] + M4[i][j] - M5[i][j] + M7[i][j];
            C12[i][j] = M3[i][j] + M5[i][j];
            C21[i][j] = M2[i][j] + M4[i][j];
            C22[i][j] = M1[i][j] - M2[i][j] + M3[i][j] + M6[i][j];
        }
    }

    int result[size][size];

    // Combine submatrices into result matrix
    for (int i = 0; i < new_size; i++)
    {
        for (int j = 0; j < new_size; j++)
        {
            result[i][j] = C11[i][j];
            result[i][j + new_size] = C12[i][j];
            result[i + new_size][j] = C21[i][j];
            result[i + new_size][j + new_size] = C22[i][j];
        }
    }
    end = clock(); // Record the end time
    cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Time taken: %lf seconds\n", cpu_time_used);
    return 0;
}