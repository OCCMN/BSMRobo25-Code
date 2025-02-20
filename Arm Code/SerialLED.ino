const int ledPin = 13;  // Pin for LED (or another device you want to control)

void setup() {
    Serial.begin(9600);
    pinMode(ledPin, OUTPUT);
}

void loop() {
    if (Serial.available() > 0) {
        char command = Serial.read();  // Read the incoming byte as a char

        // Respond to specific key presses
        if (command == 'H') {
            digitalWrite(ledPin, HIGH);  // Turn on LED
        }
        else if (command == 'h') {
            digitalWrite(ledPin, LOW);  // Turn off LED
        }
        // Add more responses for other keys here
    }
}
