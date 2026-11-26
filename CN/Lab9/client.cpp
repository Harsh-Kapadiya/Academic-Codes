// client.cpp
#include <iostream>
#include <winsock2.h>
using namespace std;

#pragma comment(lib, "ws2_32.lib")
#define PORT 8080

int main()
{
    WSADATA ws;
    WSAStartup(MAKEWORD(2, 2), &ws);

    SOCKET clientSocket;
    sockaddr_in serverAddr;

    clientSocket = socket(AF_INET, SOCK_STREAM, 0);

    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(PORT);
    serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");

    connect(clientSocket, (sockaddr *)&serverAddr, sizeof(serverAddr));

    int choice;

    while (true)
    {
        cout << "\n1. Echo\n2. Add\n3. Calculator\n4. ASCII\n5. Factorial\n6. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        send(clientSocket, (char *)&choice, sizeof(choice), 0);

        // -------- ECHO --------
        if (choice == 1)
        {
            char msg[100];
            cin.ignore();

            cout << "Enter message: ";
            cin.getline(msg, 100);

            send(clientSocket, msg, strlen(msg) + 1, 0);
            recv(clientSocket, msg, sizeof(msg), 0);

            cout << "Server Echo: " << msg << endl;
        }

        // -------- ADD --------
        else if (choice == 2)
        {
            int a, b;

            cout << "Enter two numbers: ";
            cin >> a >> b;

            send(clientSocket, (char *)&a, sizeof(a), 0);
            send(clientSocket, (char *)&b, sizeof(b), 0);

            int result;
            recv(clientSocket, (char *)&result, sizeof(result), 0);

            cout << "Result: " << result << endl;
        }

        // -------- CALCULATOR --------
        else if (choice == 3)
        {
            int a, b;
            char op;

            cout << "Enter two numbers: ";
            cin >> a >> b;
            cout << "Enter operator (+ - * / %): ";
            cin >> op;

            send(clientSocket, (char *)&a, sizeof(a), 0);
            send(clientSocket, (char *)&b, sizeof(b), 0);
            send(clientSocket, &op, sizeof(op), 0);

            int result;
            recv(clientSocket, (char *)&result, sizeof(result), 0);

            cout << "Result: " << result << endl;
        }

        // -------- ASCII --------
        else if (choice == 4)
        {
            char ch;

            cout << "Enter character: ";
            cin >> ch;

            send(clientSocket, &ch, sizeof(ch), 0);

            int ascii;
            recv(clientSocket, (char *)&ascii, sizeof(ascii), 0);

            cout << "ASCII value: " << ascii << endl;
        }

        // -------- FACTORIAL --------
        else if (choice == 5)
        {
            int n;

            cout << "Enter number: ";
            cin >> n;

            send(clientSocket, (char *)&n, sizeof(n), 0);

            long long fact;
            recv(clientSocket, (char *)&fact, sizeof(fact), 0);

            cout << "Factorial: " << fact << endl;
        }

        else if (choice == 6)
        {
            break;
        }
    }

    closesocket(clientSocket);
    WSACleanup();

    return 0;
}