#include <stdio.h>
#include <time.h>
// Function to swap two elements
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
// Partition function
int partition(int arr[], int low, int high)
{
    int pivot = arr[high]; // pivot element
    int i = low - 1;

    for (int j = low; j < high; j++)
    {
        if (arr[j] <= pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

// Quick Sort function
void quickSort(int arr[], int low, int high)   
{
    if (low < high)
    {
        int pi = partition(arr, low, high);

        // Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Function to print array
void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Driver code
int main()
{
    clock_t start, end;
    double cpu_time_used;
    start = clock(); // Record the start time
    // int arr[] = {48, 55, 7, 5, 10, 68, 36, 70, 100, 93, 82, 49, 46, 60, 74, 35, 64, 84, 88, 83, 28, 81, 44, 43, 29,  79, 61, 17, 20, 51, 54, 42, 76, 25, 94, 97, 58, 92, 56, 73, 6, 3, 24, 45, 30, 78, 52, 63, 21, 11, 95, 50, 26, 69, 67, 41, 13, 31, 59, 27, 96, 62, 15, 38, 87, 71, 14, 40, 2, 47, 89, 86, 77, 9, 1, 33, 18, 91, 85, 72, 65, 99, 4, 53, 12, 66, 90, 19, 32, 22, 75, 8, 39, 57, 98, 16, 23, 80, 37, 34};


    // int arr[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100};

    
    int arr[] = {100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original Array: ");
    printArray(arr, n);

    quickSort(arr, 0, n - 1);

    printf("Sorted Array (Quick Sort): ");
    printArray(arr, n);


    end = clock(); // Record the end time
    cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Time taken: %lf seconds\n", cpu_time_used);
    
    return 0;
}
