// Job Sequencing with Deadline (Greedy Approach)
#include <stdio.h>
struct Job
{
    char id;
    int deadline;
    int profit;
};
int main()
{
    int n;
    printf("Enter number of jobs: ");
    scanf("%d", &n);
    struct Job job[n];
    for (int i = 0; i < n; i++)
    {
        printf("\nJob %d ID: ", i + 1);
        scanf(" %c", &job[i].id);
        printf("Deadline: ");
        scanf("%d", &job[i].deadline);
        printf("Profit: ");
        scanf("%d", &job[i].profit);
    }
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (job[j].profit < job[j + 1].profit)
            {
                struct Job temp = job[j];
                job[j] = job[j + 1];
                job[j + 1] = temp;
            }
        }
    }
    int maxDeadline = 0;
    for (int i = 0; i < n; i++)
    {
        if (job[i].deadline > maxDeadline)
            maxDeadline = job[i].deadline;
    }
    char slot[maxDeadline];
    int filled[maxDeadline];
    for (int i = 0; i < maxDeadline; i++)
    {
        slot[i] = '-';
        filled[i] = 0;
    }
    int totalProfit = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = job[i].deadline - 1; j >= 0; j--)
        {
            if (filled[j] == 0)
            {
                filled[j] = 1;
                slot[j] = job[i].id;
                totalProfit += job[i].profit;
                break;
            }
        }
    }
    printf("\nSelected Job Order: ");
    for (int i = 0; i < maxDeadline; i++)
    {
        if (slot[i] != '-')
            printf("%c -> ", slot[i]);
    }
    printf("\nMaximum Profit = %d\n", totalProfit);
    return 0;
}