

#define PWMPin 6 
const int DIRPin = 7;

void setup() {
  pinMode(PWMPin, OUTPUT);
  pinMode(DIRPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  analogWrite(PWMPin, 102);
  digitalWrite(DIRPin, HIGH);
}
