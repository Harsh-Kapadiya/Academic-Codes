#include <stdio.h>

int main()
{
    int bucket_size, token_rate, n, i;
    int packets[20];

    printf("Enter bucket size (max tokens): ");
    scanf("%d", &bucket_size);

    printf("Enter token generation rate: ");
    scanf("%d", &token_rate);

    printf("Enter number of packets: ");
    scanf("%d", &n);

    printf("Enter packet sizes:\n");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &packets[i]);
    }

    int tokens = bucket_size;

    for (i = 0; i < n; i++)
    {
        tokens += token_rate;

        if (tokens > bucket_size)
            tokens = bucket_size;

        printf("\nPacket size: %d\n", packets[i]);
        printf("Available tokens: %d\n", tokens);

        if (tokens >= packets[i])
        {
            tokens -= packets[i];
            printf("Packet transmitted. Remaining tokens: %d\n", tokens);
        }
        else
        {
            printf("Not enough tokens. Packet delayed/dropped.\n");
        }
    }

    return 0;
}