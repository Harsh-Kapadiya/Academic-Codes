#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

const int LOSS_PROBABILITY = 30;   // % chance of frame loss

int main()
{
    srand(time(0));

    int totalFrames, windowSize;

    cout << "Enter total number of frames: ";
    cin >> totalFrames;

    cout << "Enter window size: ";
    cin >> windowSize;

    int base = 0;          // first unacknowledged frame
    int nextSeqNum = 0;    // next frame to send

    cout << "\n===== Go-Back-N ARQ Simulation =====\n";

    while (base < totalFrames)
    {
        /* ---- Send frames within window ---- */
        while (nextSeqNum < base + windowSize && nextSeqNum < totalFrames)
        {
            cout << "\nSender -> Sending Frame " << nextSeqNum;

            int r = rand() % 100;

            if (r < LOSS_PROBABILITY)
            {
                cout << "\nChannel xx Frame " << nextSeqNum << " LOST";
                cout << "\nSender !! Timeout -> Go back to Frame " << base << "\n";

                nextSeqNum = base;   // go back
                break;
            }
            else
            {
                cout << "\nReceiver <- Frame " << nextSeqNum << " received";
                nextSeqNum++;
            }
        }

        /* ---- ACK Section ---- */
        if (nextSeqNum > base)
        {
            cout << "\nSender <- ACK received for frames upto "
                 << nextSeqNum - 1 << endl;

            base = nextSeqNum;   // slide window
        }
    }

    cout << "\nAll frames transmitted successfully!\n";
    return 0;
}