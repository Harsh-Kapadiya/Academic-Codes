#include <stdio.h>

int main() {
    int bucket_size, output_rate, n, i;
    int packets[20];

    printf("Enter bucket size: ");
    scanf("%d", &bucket_size);

    printf("Enter output rate: ");
    scanf("%d", &output_rate);

    printf("Enter number of packets: ");
    scanf("%d", &n);

    printf("Enter packet sizes:\n");
    for(i = 0; i < n; i++) {
        scanf("%d", &packets[i]);
    }

    int current = 0;

    for(i = 0; i < n; i++) {
        printf("\nIncoming packet: %d\n", packets[i]);

        if(current + packets[i] > bucket_size) {
            printf("Bucket overflow! Packet dropped.\n");
        } else {
            current += packets[i];
            printf("Packet accepted. Current bucket size: %d\n", current);
        }

        if(current > 0) {
            int sent = (current < output_rate) ? current : output_rate;
            current -= sent;
            printf("Sent %d bytes. Remaining: %d\n", sent, current);
        }
    }

    return 0;
}