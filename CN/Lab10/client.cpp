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
    clientSocket = socket(AF_INET, SOCK_DGRAM, 0);

    sockaddr_in serverAddr;
    int serverLen = sizeof(serverAddr);

    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(PORT);
    serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");

    int choice;

    while (true)
    {
        cout << "\n1. Echo\n2. Arithmetic\n3. ASCII\n4. Chat\n5. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;
        cin.ignore();

        char buffer[1024];

        // ------------------ ECHO ------------------
        if (choice == 1)
        {
            sendto(clientSocket, "ECHO", 4, 0,
                   (sockaddr *)&serverAddr, serverLen);

            cout << "Enter message: ";
            cin.getline(buffer, sizeof(buffer));

            sendto(clientSocket, buffer, strlen(buffer), 0,
                   (sockaddr *)&serverAddr, serverLen);

            recvfrom(clientSocket, buffer, sizeof(buffer), 0,
                     NULL, NULL);

            cout << "Echo from server: " << buffer << endl;
        }

        // ------------------ ARITHMETIC ------------------
        else if (choice == 2)
        {
            sendto(clientSocket, "ARITH", 5, 0,
                   (sockaddr *)&serverAddr, serverLen);

            int a, b;
            char op;

            cout << "Enter two numbers: ";
            cin >> a >> b;

            cout << "Enter operator (+ - * /): ";
            cin >> op;

            sendto(clientSocket, (char *)&a, sizeof(a), 0,
                   (sockaddr *)&serverAddr, serverLen);

            sendto(clientSocket, (char *)&b, sizeof(b), 0,
                   (sockaddr *)&serverAddr, serverLen);

            sendto(clientSocket, &op, sizeof(op), 0,
                   (sockaddr *)&serverAddr, serverLen);

            int result;

            recvfrom(clientSocket, (char *)&result, sizeof(result), 0,
                     NULL, NULL);

            cout << "Result from server: " << result << endl;
        }

        // ------------------ ASCII ------------------
        else if (choice == 3)
        {
            sendto(clientSocket, "ASCII", 5, 0,
                   (sockaddr *)&serverAddr, serverLen);

            char ch;
            cout << "Enter character: ";
            cin >> ch;

            sendto(clientSocket, &ch, sizeof(ch), 0,
                   (sockaddr *)&serverAddr, serverLen);

            int ascii;

            recvfrom(clientSocket, (char *)&ascii, sizeof(ascii), 0,
                     NULL, NULL);

            cout << "ASCII value: " << ascii << endl;
        }

        // ------------------ CHAT ------------------
        else if (choice == 4)
        {
            sendto(clientSocket, "CHAT", 4, 0,
                   (sockaddr *)&serverAddr, serverLen);

            while (true)
            {
                cout << "You: ";
                cin.getline(buffer, sizeof(buffer));

                sendto(clientSocket, buffer, strlen(buffer), 0,
                       (sockaddr *)&serverAddr, serverLen);

                if (string(buffer) == "exit")
                    break;

                recvfrom(clientSocket, buffer, sizeof(buffer), 0,
                         NULL, NULL);

                cout << "Server: " << buffer << endl;

                if (string(buffer) == "exit")
                    break;
            }
        }

        else if (choice == 5)
        {
            break;
        }
    }

    closesocket(clientSocket);
    WSACleanup();
}