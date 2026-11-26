// server.cpp
#include <iostream>
#include <winsock2.h>
using namespace std;

#pragma comment(lib, "ws2_32.lib")

#define PORT 8080

int main()
{
    WSADATA ws;
    WSAStartup(MAKEWORD(2, 2), &ws);

    SOCKET serverSocket;
    serverSocket = socket(AF_INET, SOCK_DGRAM, 0);

    sockaddr_in serverAddr, clientAddr;
    int clientLen = sizeof(clientAddr);

    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(PORT);
    serverAddr.sin_addr.s_addr = INADDR_ANY;

    bind(serverSocket, (sockaddr *)&serverAddr, sizeof(serverAddr));

    char buffer[1024];

    cout << "Server is running...\n";

    while (true)
    {
        memset(buffer, 0, sizeof(buffer));

        recvfrom(serverSocket, buffer, sizeof(buffer), 0,
                 (sockaddr *)&clientAddr, &clientLen);

        string request = buffer;
        cout << "Client Request: " << request << endl;

        // ------------------ ECHO ------------------
        if (request == "ECHO")
        {
            recvfrom(serverSocket, buffer, sizeof(buffer), 0,
                     (sockaddr *)&clientAddr, &clientLen);

            sendto(serverSocket, buffer, strlen(buffer), 0,
                   (sockaddr *)&clientAddr, clientLen);
        }

        // ------------------ ARITHMETIC ------------------
        else if (request == "ARITH")
        {
            int a, b;
            char op;

            recvfrom(serverSocket, (char *)&a, sizeof(a), 0,
                     (sockaddr *)&clientAddr, &clientLen);

            recvfrom(serverSocket, (char *)&b, sizeof(b), 0,
                     (sockaddr *)&clientAddr, &clientLen);

            recvfrom(serverSocket, &op, sizeof(op), 0,
                     (sockaddr *)&clientAddr, &clientLen);

            int result;

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
            default:
                result = 0;
            }

            sendto(serverSocket, (char *)&result, sizeof(result), 0,
                   (sockaddr *)&clientAddr, clientLen);
        }

        // ------------------ ASCII ------------------
        else if (request == "ASCII")
        {
            char ch;

            recvfrom(serverSocket, &ch, sizeof(ch), 0,
                     (sockaddr *)&clientAddr, &clientLen);

            int ascii = (int)ch;

            sendto(serverSocket, (char *)&ascii, sizeof(ascii), 0,
                   (sockaddr *)&clientAddr, clientLen);
        }

        // ------------------ CHAT ------------------
        else if (request == "CHAT")
        {
            while (true)
            {
                memset(buffer, 0, sizeof(buffer));

                recvfrom(serverSocket, buffer, sizeof(buffer), 0,
                         (sockaddr *)&clientAddr, &clientLen);

                string msg = buffer;
                cout << "Client: " << msg << endl;

                if (msg == "exit")
                    break;

                string reply;
                cout << "Server: ";
                getline(cin, reply);

                sendto(serverSocket, reply.c_str(), reply.length(), 0,
                       (sockaddr *)&clientAddr, clientLen);

                if (reply == "exit")
                    break;
            }
        }
    }

    closesocket(serverSocket);
    WSACleanup();
}