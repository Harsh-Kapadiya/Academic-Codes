#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

const int TOTAL_FRAMES = 5;      // total frames to send
const int LOSS_PROBABILITY = 30; // % chance of frame/ACK loss

// Simulate sending frame
bool sendFrame(int frameNo)
{
    cout << "Sending Frame " << frameNo << endl;

    int random = rand() % 100;
    if (random < LOSS_PROBABILITY)
    {
        cout << "Frame " << frameNo << " LOST during transmission!\n";
        return false;
    }

    cout << "Frame " << frameNo << " delivered successfully.\n";
    return true;
}

// Simulate receiving ACK
bool receiveACK(int frameNo)
{
    int random = rand() % 100;
    if (random < LOSS_PROBABILITY)
    {
        cout << "ACK " << frameNo << " LOST!\n";
        return false;
    }

    cout << "ACK " << frameNo << " received successfully.\n";
    return true;
}

int main()
{
    srand(time(0));

    int Sn = 0; // sequence number

    while (Sn < TOTAL_FRAMES)
    {

        cout << "\n----------------------------\n";

        bool frameStatus = sendFrame(Sn);

        if (!frameStatus)
        {
            cout << "Timeout! Resending Frame " << Sn << endl;
            continue; // resend same frame
        }

        bool ackStatus = receiveACK(Sn);

        if (!ackStatus)
        {
            cout << "Timeout! ACK not received. Resending Frame " << Sn << endl;
            continue; // resend same frame
        }

        cout << "Frame " << Sn << " successfully transmitted.\n";
        Sn++; // move to next frame
    }

    cout << "\nAll frames transmitted successfully!\n";
    return 0;
}