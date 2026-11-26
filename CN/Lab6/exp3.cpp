#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

const int LOSS_PROBABILITY = 30; // % chance of frame loss

int main()
{
    srand(time(0));

    int totalFrames, windowSize;

    cout << "Enter total number of frames: ";
    cin >> totalFrames;

    cout << "Enter window size: ";
    cin >> windowSize;

    bool received[100] = {false}; // receiver buffer
    int base = 0;

    cout << "\n===== Selective Repeat ARQ Simulation =====\n";

    while (base < totalFrames)
    {
        /* ---- Send frames in window ---- */
        for (int i = base; i < base + windowSize && i < totalFrames; i++)
        {
            if (!received[i])
            {
                cout << "\nSender -> Sending Frame " << i;

                int r = rand() % 100;

                if (r < LOSS_PROBABILITY)
                {
                    cout << "\nChannel xx Frame " << i << " LOST";
                }
                else
                {
                    cout << "\nReceiver <- Frame " << i << " received";
                    received[i] = true;
                    cout << "\nReceiver -> ACK " << i << " sent";
                }
            }
        }

        /* ---- Slide window if base frame received ---- */
        while (received[base] && base < totalFrames)
        {
            base++;
        }

        cout << "\nWindow slides. New base = " << base << "\n";
    }

    cout << "\nAll frames transmitted successfully!\n";
    return 0;
}