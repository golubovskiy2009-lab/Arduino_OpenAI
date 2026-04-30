const int sensorPin = A0;
const int ledPin = 13;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int val = analogRead(sensorPin);
  
  Serial.print("SENSOR_DATA:");
  Serial.println(val);

  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "LED_ON") {
      digitalWrite(ledPin, HIGH);
    } 
    else if (command == "LED_OFF") {
      digitalWrite(ledPin, LOW);
    }
  }
  delay(1000); 
}
