#include <Arduino.h>
#include <Servo.h>

#define LFTreadMtrPin 2
#define RFTreadMtrPin 3
#define LRTreadMtrPin 4
#define RRTreadMtrPin 5
#define LFFlipMtrPin 6
#define RFFlipMtrPin 7
#define LRFlipMtrPin 8
#define RRFlipMtrPin 9
#define B1MtrPin 10
#define B2MtrPin 11
#define ElbowMtrPin 12
#define WRowMtrPin 13
#define WFlexMtrPin 44
#define ClawMtrPin 45
#define TurtMtrPin 46

Servo LFTreadMtr;
Servo RFTreadMtr;
Servo LRTreadMtr;
Servo RRTreadMtr;
Servo LFFlipMtr;
Servo RFFlipMtr;
Servo LRFlipMtr;
Servo RRFlipMtr;
Servo B1Mtr;
Servo B2Mtr;
Servo ElbowMtr;
Servo WRowMtr;
Servo WFlexMtr;
Servo ClawMtr;
Servo TurtMtr;

const int GreenledPin = 52;
const int ledPin = 53;

String receivedData = "";  // Stores incoming data

void setup() {
    Serial.begin(9600);  // Start serial communication
    LFTreadMtr.attach(LFTreadMtrPin);
    RFTreadMtr.attach(RFTreadMtrPin);
    LRTreadMtr.attach(LRTreadMtrPin);
    RRTreadMtr.attach(RRTreadMtrPin);
    LFFlipMtr.attach(LFFlipMtrPin);
    RFFlipMtr.attach(RFFlipMtrPin);
    LRFlipMtr.attach(LRFlipMtrPin);
    RRFlipMtr.attach(RRFlipMtrPin);
    B1Mtr.attach(B1MtrPin);
    B2Mtr.attach(B2MtrPin);
    ElbowMtr.attach(ElbowMtrPin);
    WRowMtr.attach(WRowMtrPin);
    WFlexMtr.attach(WFlexMtrPin);
    ClawMtr.attach(ClawMtrPin);
    TurtMtr.attach(TurtMtrPin);
    pinMode(GreenledPin, OUTPUT);
    pinMode(ledPin, OUTPUT);
}

void loop() {
    // Check if serial data is available
    while (Serial.available()) {
        char incomingChar = Serial.read();  // Read one character

        // Append to string unless it's the end of the message
        if (incomingChar == '>') {
            processCommand(receivedData);  // Process the full command
            receivedData = "";  // Reset string for next command
        } else {
            receivedData += incomingChar;  // Build command string
        }
    }
}

// Function to process structured commands
void processCommand(String command) {
    int StopMotorVal = 1500;
    int MotorSpeed = 70;
    int StallSpeed = 40;
    int SlowStallSpeed = 30;

    // Ensure the message is correctly formatted
    if (command.startsWith("<") && command.indexOf(':') > 0) {
        String prefix = command.substring(1, command.indexOf(':'));  // Extract prefix
        String value = command.substring(command.indexOf(':') + 1);  // Extract value

        // Handle movement commands
        if (prefix == "D") {
            if (value == "W") {
                ElbowMtr.writeMicroseconds(StopMotorVal);
                WRowMtr.writeMicroseconds(StopMotorVal);
            } else if (value == "w") {
                ElbowMtr.writeMicroseconds(0);
                WRowMtr.writeMicroseconds(0);
            }
        }
        
        // Handle flipper commands
        else if (prefix == "A") {
            if (value == "T") {
                digitalWrite(ledPin, HIGH);
            } else if (value == "t") {
                digitalWrite(ledPin, LOW);
            }
        }
        
        // Emergency Stop
        else if (prefix == "E" && value == "STOP") {
            Serial.println("EMERGENCY STOP ACTIVATED!");
            // Add stop motor logic
        }
        
        // Unknown command
        else {
            Serial.println("Unknown Command: " + command);
        }
    }
}
