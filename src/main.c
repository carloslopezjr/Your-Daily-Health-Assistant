#include <wiringPi.h>
#include <stdio.h>

#define PIR_PIN 26  // WiringPi pin 0 is BCM_GPIO 17

int main(void) {
    // Setup wiringPi and the PIR_PIN as input
    if (wiringPiSetup() == -1) {
        printf("WiringPi setup failed!\n");
        return 1;
    }

    pinMode(PIR_PIN, INPUT);

    printf("PIR Sensor Test (CTRL+C to exit)\n");

    while (1) {
        if (digitalRead(PIR_PIN) == HIGH) {
            printf("Motion Detected!\n");
            // delay(1000);  // Wait for 1 second
        } else {
            printf("No Motion\n");
            // delay(1000);  // Wait for 1 second
        }
    }

    return 0;
}
