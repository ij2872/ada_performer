#include <Adafruit_CircuitPlayground.h>

float X, Y, Z;

void setup() {
  Serial.begin(9600);
  CircuitPlayground.begin();
}

void loop() {
  X = CircuitPlayground.motionX();
  Y = CircuitPlayground.motionY();
  Z = CircuitPlayground.motionZ();

//  @TODO send compact y and z data. Maybe change the delay.
  Serial.print(X);
  Serial.print("\n");
//  Serial.print(Y);
//  Serial.println(Z);

  delay(100);
}
