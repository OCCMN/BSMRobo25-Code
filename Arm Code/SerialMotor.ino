#include <Servo.h>

#define RowMotorPin 3
#define ExtMotorPin 5
#define TurPWMPin 6
#define BaseMotor1Pin 9
#define BaseMotor2Pin 10

Servo RowMotor;
Servo ExtMotor;
Servo B1Motor;
Servo B2Motor;

const int ledPin = 13;  // Pin for LED (or another device you want to control)
const int DIRpin = 7; //DIR Pin for Brushed Turret Motor

void setup() {
    Serial.begin(9600);
    RowMotor.attach(RowMotorPin);
    ExtMotor.attach(ExtMotorPin);
    B1Motor.attach(BaseMotor1Pin);
    B2Motor.attach(BaseMotor2Pin);
    pinMode(TurPWMPin, OUTPUT);
    pinMode(DIRpin, OUTPUT);
    pinMode(ledPin, OUTPUT);
}

void loop() {
    int StopMotorVal = 1500; //Neutral signal for brushless
    int MotorSpeed = 70; //Speed Setting for motor movement 

    if (Serial.available() > 0) {
        char command = Serial.read();  // Read the incoming byte as a char

        // Respond to specific key presses
        if (command == 'H') {
            digitalWrite(ledPin, HIGH);  // Turn on LED
        }
        else if (command == 'h') {
            digitalWrite(ledPin, LOW);  // Turn off LED
        }
        else if (command == 'J') {
          RowMotor.writeMicroseconds(StopMotorVal + MotorSpeed);
        }
        else if (command == 'j') {
          RowMotor.writeMicroseconds(StopMotorVal);
        }
        else if (command == 'L') {
          RowMotor.writeMicroseconds(StopMotorVal - MotorSpeed);
        }
        else if (command == 'l') {
          RowMotor.writeMicroseconds(StopMotorVal);
        }
        else if (command == 'I') {
          ExtMotor.writeMicroseconds(StopMotorVal + MotorSpeed);
        }
        else if (command == 'i') {
          ExtMotor.writeMicroseconds(StopMotorVal);
        }
        else if (command == 'K') {
          ExtMotor.writeMicroseconds(StopMotorVal - MotorSpeed);
        }
        else if (command == 'k') {
          ExtMotor.writeMicroseconds(StopMotorVal);
        }
        else if (command == 'W') {
          B1Motor.writeMicroseconds(StopMotorVal + MotorSpeed);
          B2Motor.writeMicroseconds(StopMotorVal + MotorSpeed);
        }
        else if (command == 'w') {
          B1Motor.writeMicroseconds(StopMotorVal);
          B2Motor.writeMicroseconds(StopMotorVal);
        }
        else if (command == 'S') {
          B1Motor.writeMicroseconds(StopMotorVal - MotorSpeed);
          B2Motor.writeMicroseconds(StopMotorVal - MotorSpeed);
        }
        else if (command == 's') {
          B1Motor.writeMicroseconds(StopMotorVal);
          B2Motor.writeMicroseconds(StopMotorVal);
        }
        else if (command == 'A') {
          analogWrite(TurPWMPin, 102);
          digitalWrite(DIRpin, HIGH); 
        }
        else if (command == 'a') {
          analogWrite(TurPWMPin, 0);
          digitalWrite(DIRpin, LOW); 
        }
        else if (command == 'D') {
         analogWrite(TurPWMPin, 102);
         digitalWrite(DIRpin, LOW);
        }
        else if (command == 'd') {
          analogWrite(TurPWMPin, 0);
          digitalWrite(DIRpin, LOW); 
        }
        
        // Add more responses for other keys here
    }
}
