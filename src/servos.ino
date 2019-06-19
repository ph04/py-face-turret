#include <Servo.h>

#define PINY 47 // change with your own PINs
#define PINX 53

Servo myservoX;
Servo myservoY;

void setup() {
  myservoX.attach(PINX);
  myservoY.attach(PINY);
  Serial.begin(9600);
}

void loop() {
  int X[3] = {0, 0, 0}; 
  int Y[3] = {0, 0, 0};
  
  for (int i = 0; i < 3; i++) {
    while (1) {
      if (Serial.available()) {
        X[i] = Serial.read() - '0';
        Serial.print(X[i]);
        //Serial.print("");
        break;
      }
    }
  }

  myservoX.write(X[0] * 100 + X[1] * 10 + X[2]);

  Serial.print("; ");

  for (int i = 0; i < 3; i++) {
    while (1) {
      if (Serial.available()) {
        Y[i] = Serial.read() - '0';
        Serial.print(Y[i]);
        //Serial.print("");
        break;
      }
    }
  }

  myservoY.write(Y[0] * 100 + Y[1] * 10 + Y[2]);

  Serial.println(";");
}
