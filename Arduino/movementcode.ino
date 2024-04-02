#include <Wire.h>
int pul = 8;
int dir = 9;

void setup() {
  pinMode(pul,OUTPUT);
  pinMode(dir,OUTPUT);
  Serial.begin(9600);
}

void moveFunc(int numSteps, int direction){
  if(direction == 1){
    digitalWrite(dir,HIGH);
    for(int x = 0; x < numSteps; x++){
      digitalWrite(pul,HIGH);
      delayMicroseconds(5000);
      digitalWrite(pul,LOW);
      delayMicroseconds(5000);
    }
  }
  else if(direction == 0){
    digitalWrite(dir,LOW);
    for(int x = 0; x < 200; x++){
      digitalWrite(pul,HIGH);
      delayMicroseconds(5000);
      digitalWrite(pul,LOW);
      delayMicroseconds(5000);
    }
  }
}

void moveForward(){
  moveFunc(1600,1);
}

void moveBack(){
  moveFunc(1600,0);
}


void loop() { 
  if (Serial.available() > 0) {
    int inByte = Serial.read();
    switch (inByte) {

      case '1': {
        //move forward
        break;
      }
      case '2': {
        //move back
        break;
      }
    }
  }
}