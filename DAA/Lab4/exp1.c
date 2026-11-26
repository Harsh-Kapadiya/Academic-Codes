#include <stdio.h>
#include <stdlib.h>
#define MAX 100
struct Node
{
    char data;
    int freq;
    struct Node *left, *right;
};
// create new node
struct Node *newNode(char d, int f)
{
    struct Node *n = (struct Node *)malloc(sizeof(struct Node));
    n->data = d;
    n->freq = f;
    n->left = n->right = NULL;
    return n;
}
// simple function to sort nodes by frequency
void sort(struct Node *arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (arr[j]->freq > arr[j + 1]->freq)
            {
                struct Node *t = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = t;
            }
}
// print Huffman codes
void printCodes(struct Node *root, int code[], int top)
{
    if (root->left)
    {
        code[top] = 0;
        printCodes(root->left, code, top + 1);
    }
    if (root->right)
    {
        code[top] = 1;
        printCodes(root->right, code, top + 1);
    }
    if (!root->left && !root->right)
    {
        printf("%c: ", root->data);
        for (int i = 0; i < top; i++)
            printf("%d", code[i]);
        printf("\n");
    }
}
int main()
{
    int n;
    printf("Enter number of characters: ");
    scanf("%d", &n);
    struct Node *arr[n];
    for (int i = 0; i < n; i++)
    {
        char ch;
        int f;
        printf("Character and frequency: ");
        scanf(" %c %d", &ch, &f);
        arr[i] = newNode(ch, f);
    }
    int size = n;
    while (size > 1)
    {
        sort(arr, size);

        struct Node *left = arr[0];
        struct Node *right = arr[1];

        struct Node *parent = newNode('$', left->freq + right->freq);
        parent->left = left;
        parent->right = right;

        arr[1] = parent;
        arr[0] = arr[size - 1];
        size--;
    }
    int code[MAX], top = 0;
    printf("\nHuffman Codes:\n");
    printCodes(arr[0], code, top);
    return 0;
}