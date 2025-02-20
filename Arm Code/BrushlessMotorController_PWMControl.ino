//Programmer: OCase Date:2/18/25
#include <Servo.h>

#define MotorPin 9

Servo Motor;

void setup() {
    Motor.attach(MotorPin);
}

void loop() {
    int StopMotorVal = 1500;  // Neutral signal for brushless motors
    int MotorSpeed = 280;     // Adjust for desired speed range (typically ±500)
    /*Issue(2/18/25): Higher speeds than about '280', gets worse the higher it goes. Lowwer limit unknown
      May be a problem with motor controller config. NOT HIGH PRIORITY.*/

    //+: counter clockwise direction
    //-: clockwise direction, for those who couldn't figure it out 
    Motor.writeMicroseconds(StopMotorVal + MotorSpeed);
    delay(100);  // Wait 1 second
}
