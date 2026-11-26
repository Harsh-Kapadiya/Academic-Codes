#include <stdio.h>
#include <time.h>

int main()
{
    int size = 4;
    int choice;
    clock_t start, end;
    double cpu_time_used;

    int matrix_1[4][4], matrix_2[4][4];

    printf("Enter elements of first 4x4 matrix:\n");
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            scanf("%d", &matrix_1[i][j]);

    printf("Enter elements of second 4x4 matrix:\n");
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            scanf("%d", &matrix_2[i][j]);

    while (1)
    {
        printf("\nChoose method:\n");
        printf("1. Strassen Matrix Multiplication\n");
        printf("2. Standard Matrix Multiplication\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        if (choice != 1 && choice != 2)
        {
            printf("Wrong choice entered. Program terminated.\n");
            break;
        }

        // ---------- STRASSEN ----------
        if (choice == 1)
        {
            start = clock();
            int n = 2;

            int A11[2][2], A12[2][2], A21[2][2], A22[2][2];
            int B11[2][2], B12[2][2], B21[2][2], B22[2][2];

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    A11[i][j] = matrix_1[i][j];
                    A12[i][j] = matrix_1[i][j + n];
                    A21[i][j] = matrix_1[i + n][j];
                    A22[i][j] = matrix_1[i + n][j + n];

                    B11[i][j] = matrix_2[i][j];
                    B12[i][j] = matrix_2[i][j + n];
                    B21[i][j] = matrix_2[i + n][j];
                    B22[i][j] = matrix_2[i + n][j + n];
                }
            }

            int M1[2][2], M2[2][2], M3[2][2], M4[2][2];
            int M5[2][2], M6[2][2], M7[2][2];

            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                {
                    M1[i][j] = (A11[i][j] + A22[i][j]) * (B11[i][j] + B22[i][j]);
                    M2[i][j] = (A21[i][j] + A22[i][j]) * B11[i][j];
                    M3[i][j] = A11[i][j] * (B12[i][j] - B22[i][j]);
                    M4[i][j] = A22[i][j] * (B21[i][j] - B11[i][j]);
                    M5[i][j] = (A11[i][j] + A12[i][j]) * B22[i][j];
                    M6[i][j] = (A21[i][j] - A11[i][j]) * (B11[i][j] + B12[i][j]);
                    M7[i][j] = (A12[i][j] - A22[i][j]) * (B21[i][j] + B22[i][j]);
                }

            int C11[2][2], C12[2][2], C21[2][2], C22[2][2];

            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                {
                    C11[i][j] = M1[i][j] + M4[i][j] - M5[i][j] + M7[i][j];
                    C12[i][j] = M3[i][j] + M5[i][j];
                    C21[i][j] = M2[i][j] + M4[i][j];
                    C22[i][j] = M1[i][j] - M2[i][j] + M3[i][j] + M6[i][j];
                }

            int result[4][4];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                {
                    result[i][j] = C11[i][j];
                    result[i][j + n] = C12[i][j];
                    result[i + n][j] = C21[i][j];
                    result[i + n][j + n] = C22[i][j];
                }

            printf("\nResult (Strassen):\n");
            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                    printf("%d ", result[i][j]);
                printf("\n");
            }

            end = clock();
            printf("Time: %.10lf seconds\n",
                   ((double)(end - start)) / CLOCKS_PER_SEC);
        }

        // ---------- STANDARD ----------
        else
        {
            start = clock();
            int result[4][4] = {0};

            for (int i = 0; i < size; i++)
                for (int j = 0; j < size; j++)
                    for (int k = 0; k < size; k++)
                        result[i][j] += matrix_1[i][k] * matrix_2[k][j];

            printf("\nResult (Standard):\n");
            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j < size; j++)
                    printf("%d ", result[i][j]);
                printf("\n");
            }

            end = clock();
            printf("Time: %.10lf seconds\n",
                   ((double)(end - start)) / CLOCKS_PER_SEC);
        }
    }

    return 0;
}