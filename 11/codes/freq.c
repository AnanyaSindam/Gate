#include <stdio.h>
#include <math.h>

#define NUM_POINTS 1000

double magnitude_response(double omega) {
    return 3 / sqrt(1 + omega * omega);
}

double phase_response(double omega) {
    double real_part = 3 * cos(-3 * omega);
    double imag_part = 3 * sin(-3 * omega);
    return atan2(imag_part, 1 + omega) * 180 / M_PI;
}

int main() {
    FILE *freqFile = fopen("freq.dat", "w");
    if (freqFile) {
        double w[NUM_POINTS], magnitude[NUM_POINTS], phase[NUM_POINTS];

        // Calculate values for magnitude and phase responses
        for (int i = 0; i < NUM_POINTS; ++i) {
            w[i] = i * 10.0 / (NUM_POINTS - 1);
            magnitude[i] = magnitude_response(w[i]);
            phase[i] = phase_response(w[i]);
            // Write frequency, magnitude, and phase to file
            fprintf(freqFile, "%lf %lf %lf\n", w[i], magnitude[i], phase[i]);
        }

        fclose(freqFile);
    } else {
        printf("Error: Unable to create file.\n");
    }
    return 0;
}

