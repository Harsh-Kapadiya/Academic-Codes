// Fractional Knapsack Problem (Greedy Approach)

#include <stdio.h>
#include <stdlib.h>
// structure to store item details
struct Item
{
    int weight;
    int value;
    float ratio;
};

int main()
{
    int n;
    float capacity;

    printf("Enter number of items: ");
    scanf("%d", &n);

    struct Item item[n];

    // input
    for (int i = 0; i < n; i++)
    {
        printf("\nItem %d value: ", i + 1);
        scanf("%d", &item[i].value);

        printf("Item %d weight: ", i + 1);
        scanf("%d", &item[i].weight);

        item[i].ratio = (float)item[i].value / item[i].weight;
    }

    printf("\nEnter knapsack capacity: ");
    scanf("%f", &capacity);

    // sort items by ratio (descending)
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (item[j].ratio < item[j + 1].ratio)
            {
                struct Item temp = item[j];
                item[j] = item[j + 1];
                item[j + 1] = temp;
            }
        }
    }

    float totalProfit = 0.0;

    // greedy selection
    for (int i = 0; i < n; i++)
    {
        if (capacity >= item[i].weight)
        {
            capacity -= item[i].weight;
            totalProfit += item[i].value;
        }
        else
        {
            totalProfit += item[i].ratio * capacity;
            break;
        }
    }

    printf("\nMaximum Profit = %.f\n", totalProfit);

    return 0;
}