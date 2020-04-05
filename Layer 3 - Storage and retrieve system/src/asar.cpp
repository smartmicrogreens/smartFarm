#include "asar.hpp"
#include "motor.hpp"
#include <Arduino.h>
ASAR::ASAR() {
    rightMotor = new Motor(rightMotorPinA, rightMotorPinB);
    leftMotor = new Motor(leftMotorPinA, leftMotorPinB);
    usSensor = new Ultrasonic(US_PING, US_ECHO);
}

void ASAR::readInfrared(bool& R, bool& L) {
    // Reads both sensors and compare with 1. If 1, will turn true, if 0 will turn false.
    R = digitalRead(RIGHT_IR_PIN) == 1;
    L = digitalRead(LEFT_IR_PIN) == 1;
}
bool ASAR::compareDistance(uint8_t _distance) {
    // _distance can be between 2 and 400 cm
    if(usSensor->read() == _distance) return true;
    else return false;
}

void ASAR::moveForward() {

    readInfrared(IR_R, IR_L);
    Serial.print("Right: ");
    Serial.print(IR_R);
    Serial.print(" - Left:");
    Serial.println(IR_L);
    if(IR_R && IR_L) {
        this->rightMotor->updateSpeed(180);
        this->leftMotor->updateSpeed(180);
        this->rightMotor->moveForward();
        this->leftMotor->moveForward();
        Serial.println("Derecho!");
    }
    else if(!IR_R && IR_L){
        //this->leftMotor->updateSpeed(10);
        //this->leftMotor->moveForward();
        this->stop();
        this->rotateClockwise(50, 500);
    }
    else if (IR_R && !IR_L) {
        // this->rightMotor->updateSpeed(10);
        // this->rightMotor->moveForward();
        this->stop();
        this->rotateCounterClockwise(50, 500);
    }
    else if(!IR_R && !IR_L) this->stop();
}
void ASAR::stop() {
    this->rightMotor->stop();
    this->leftMotor->stop();
}
bool ASAR::headNorth() {
    // Rotates in clockwise/counterclockwise direction, enough time to reach 90/180 degrees.
    if (direction == WEST) rotateClockwise(100, TIME_90);
    else if (direction == EAST) rotateCounterClockwise(100, TIME_90);
    else if (direction == SOUTH) rotateCounterClockwise(100, TIME_180);
    return true;
}
bool ASAR::headEast() {
    // Rotates in clockwise/counterclockwise direction, enough time to reach 90/180 degrees.
    if (direction == WEST) rotateClockwise(100, TIME_180);
    else if (direction == NORTH) rotateCounterClockwise(100, TIME_90);
    else if (direction == SOUTH) rotateClockwise(100, TIME_90);
    return true;
}
bool ASAR::headSouth() {
    // Rotates in clockwise/counterclockwise direction, enough time to reach 90/180 degrees.
    if (direction == WEST) rotateCounterClockwise(100, TIME_90);
    else if (direction == EAST) rotateClockwise(100, TIME_90);
    else if (direction == NORTH) rotateCounterClockwise(100, TIME_180);
    return true;
}
bool ASAR::headWest() {
    // Rotates in clockwise/counterclockwise direction, enough time to reach 90/180 degrees.
    if (direction == NORTH) rotateCounterClockwise(100, TIME_90);
    else if (direction == EAST) rotateCounterClockwise(100, TIME_180);
    else if (direction == SOUTH) rotateClockwise(100, TIME_90);
    return true;
}

void inline ASAR::rotateClockwise(int _speed, int _time) {
    this->rightMotor->updateSpeed(80);
    this->leftMotor->updateSpeed(80);
    this->rightMotor->moveBackward();
    this->leftMotor->moveForward();
    delay(_time);
}

void inline ASAR::rotateCounterClockwise(int _speed, int _time) {
    this->rightMotor->updateSpeed(80);
    this->leftMotor->updateSpeed(80);
    this->rightMotor->moveForward();
    this->leftMotor->moveBackward();
    delay(_time);
}

