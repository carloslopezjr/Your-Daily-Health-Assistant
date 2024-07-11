#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>

#define PIR_PIN 26  // WiringPi pin 0 is BCM_GPIO 17


void delay_minutes(int minutes) {
    delay(minutes * 60 * 1000);
}

int main(void) {
    // Setup wiringPi and the PIR_PIN as input
    if (wiringPiSetup() == -1) {
        printf("WiringPi setup failed!\n");
        return 1;
    }

    pinMode(PIR_PIN, INPUT);

    printf("PIR Sensor Test (CTRL+C to exit)\n");

    const char *python_file = "functions.py";

    // This needs to keep going after program finished
    while (1) {
        if (digitalRead(PIR_PIN) == HIGH) {
            printf("Motion Detected! Starting Program\n");
            char command[256];
            snprintf(command, sizeof(command), "./run_python.sh %s", python_file);

            int result = system(command);

            if (result == -1) {
                perror("system");
                return 1;
            }

            // break;
            delay_minutes(10);

        } else {
            printf("No Motion\n");
            delay(1000);  // Wait for 1 second
        }
    }

    return 0;
    
}
