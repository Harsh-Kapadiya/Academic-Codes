#include <iostream>
#include <winsock2.h>
using namespace std;

#pragma comment(lib, "ws2_32.lib")
#define PORT 8080

int main()
{
    WSADATA ws;
    WSAStartup(MAKEWORD(2, 2), &ws);

    SOCKET serverSocket, clientSocket;
    sockaddr_in serverAddr, clientAddr;
    int clientLen = sizeof(clientAddr);

    serverSocket = socket(AF_INET, SOCK_STREAM, 0);

    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(PORT);
    serverAddr.sin_addr.s_addr = INADDR_ANY;

    bind(serverSocket, (sockaddr *)&serverAddr, sizeof(serverAddr));
    listen(serverSocket, 3);

    cout << "Server started...\n";

    clientSocket = accept(serverSocket, (sockaddr *)&clientAddr, &clientLen);

    int choice;

    while (true)
    {
        recv(clientSocket, (char *)&choice, sizeof(choice), 0);

        // -------- ECHO --------
        if (choice == 1)
        {
            char msg[100] = {0};
            recv(clientSocket, msg, sizeof(msg), 0);
            send(clientSocket, msg, strlen(msg) + 1, 0);
        }

        // -------- ADD --------
        else if (choice == 2)
        {
            int a, b;
            recv(clientSocket, (char *)&a, sizeof(a), 0);
            recv(clientSocket, (char *)&b, sizeof(b), 0);

            int result = a + b;
            send(clientSocket, (char *)&result, sizeof(result), 0);
        }

        // -------- CALCULATOR --------
        else if (choice == 3)
        {
            int a, b;
            char op;

            recv(clientSocket, (char *)&a, sizeof(a), 0);
            recv(clientSocket, (char *)&b, sizeof(b), 0);
            recv(clientSocket, &op, sizeof(op), 0);

            int result = 0;

            switch (op)
            {
            case '+':
                result = a + b;
                break;
            case '-':
                result = a - b;
                break;
            case '*':
                result = a * b;
                break;
            case '/':
                result = (b != 0) ? a / b : 0;
                break;
            case '%':
                result = (b != 0) ? a % b : 0;
                break;
            default:
                result = 0;
            }

            send(clientSocket, (char *)&result, sizeof(result), 0);
        }

        // -------- ASCII --------
        else if (choice == 4)
        {
            char ch;
            recv(clientSocket, &ch, sizeof(ch), 0);

            int ascii = (int)ch;
            send(clientSocket, (char *)&ascii, sizeof(ascii), 0);
        }

        // -------- FACTORIAL --------
        else if (choice == 5)
        {
            int n;
            recv(clientSocket, (char *)&n, sizeof(n), 0);

            long long fact = 1;
            for (int i = 1; i <= n; i++)
                fact *= i;

            send(clientSocket, (char *)&fact, sizeof(fact), 0);
        }

        else if (choice == 6)
        {
            break;
        }
    }

    closesocket(clientSocket);
    closesocket(serverSocket);
    WSACleanup();

    return 0;
}