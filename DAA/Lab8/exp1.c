// o-1 knapsack using brute-force method

#include <stdio.h>

struct Item
{
    int weight;
    int value;
    int items;
};

void brute_force(int capacity, struct Item items[], int n)
{
    int maxProfit = 0;
    for (int i = 0; i < (1 << n); i++)
    {
        int totalWeight = 0;
        int totalValue = 0;
        for (int j = 0; j < n; j++)
        {
            if (i & (1 << j))
            {
                totalWeight += items[j].weight;
                totalValue += items[j].value;
            }
        }
        if (totalWeight <= capacity && totalValue > maxProfit)
        {
            maxProfit = totalValue;
        }
    }
    printf("Maximum profit: %d\n", maxProfit);
}

int main()
{
    int capacity, n;
    printf("Enter number of items: ");
    scanf("%d", &n);
    struct Item items[n];
    for (int i = 0; i < n; i++)
    {
        printf("\nItem %d value: ", i + 1);
        scanf("%d", &items[i].value);

        printf("Item %d weight: ", i + 1);
        scanf("%d", &items[i].weight);
    }

    printf("\nEnter knapsack capacity: ");
    scanf("%d", &capacity);

    brute_force(capacity, items, n);
    return 0;
}