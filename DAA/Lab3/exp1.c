// Fractional Knapsack using Greedy + Max-Heap (Top-K efficient approach)

#include <stdio.h>

struct Item
{
    int weight;
    int value;
    float ratio;
};

// ---------- Utility ----------

void swap(struct Item *a, struct Item *b)
{
    struct Item t = *a;
    *a = *b;
    *b = t;
}

// Maintain max-heap property
void heapify(struct Item heap[], int n, int i)
{
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && heap[l].ratio > heap[largest].ratio)
        largest = l;

    if (r < n && heap[r].ratio > heap[largest].ratio)
        largest = r;

    if (largest != i)
    {
        swap(&heap[i], &heap[largest]);
        heapify(heap, n, largest);
    }
}

void buildHeap(struct Item heap[], int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(heap, n, i);
}

struct Item extractMax(struct Item heap[], int *n)
{
    struct Item root = heap[0];
    heap[0] = heap[*n - 1];
    (*n)--;
    heapify(heap, *n, 0);
    return root;
}

// ---------- Main ----------

int main()
{
    int n;
    float capacity;

    printf("Enter number of items: ");
    scanf("%d", &n);

    struct Item heap[n];

    for (int i = 0; i < n; i++)
    {
        printf("\nItem %d value: ", i + 1);
        scanf("%d", &heap[i].value);

        printf("Item %d weight: ", i + 1);
        scanf("%d", &heap[i].weight);

        heap[i].ratio = (float)heap[i].value / heap[i].weight;
    }

    printf("\nEnter knapsack capacity: ");
    scanf("%f", &capacity);

    // Build max-heap instead of sorting
    buildHeap(heap, n);

    float totalProfit = 0.0;

    // Greedy selection (always pick best ratio first)
    while (n > 0 && capacity > 0)
    {
        struct Item best = extractMax(heap, &n);

        if (capacity >= best.weight)
        {
            capacity -= best.weight;
            totalProfit += best.value;
        }
        else
        {
            totalProfit += best.ratio * capacity;
            break;
        }
    }

    printf("\nMaximum Profit = %.2f\n", totalProfit);

    return 0;
}