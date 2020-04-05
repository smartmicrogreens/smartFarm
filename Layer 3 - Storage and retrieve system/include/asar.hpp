#ifndef ASAR_HPP
#define ASAR_HPP

#include <Arduino.h>
#include <LinkedList.h>
#include "motor.hpp"
#include <Ultrasonic.h>

class ASAR {

private:
    int direction;
    String curStation;
    String previousStation;
    Motor* leftMotor;
    Motor* rightMotor;
    Ultrasonic* usSensor;

    const int US_PING = 1;
    const int US_ECHO = 2;

    const int rightMotorPinA = 6;
    const int rightMotorPinB = 9;
    const int leftMotorPinA = 10;
    const int leftMotorPinB = 11;

    const int NORTH = 0;
    const int SOUTH = 1;
    const int EAST = 2;
    const int WEST = 3;

    const int TIME_90 = 1500;
    const int TIME_180 = 3000;
    const int TIME_360 = 6000;

    // Robot physical parameters
    const int radiusChasis = 0.25; // Radius of the chasis(From center of the robot to the center of the wheel, looking from above).
    const int radiusWheels = 0.05; // Radius of the wheel
    const int fullTurnMotorSteps = 200; // Motor total steps in one turn

    const int RIGHT_IR_PIN = 36;
    const int LEFT_IR_PIN = 37;
    bool IR_R, IR_L; 

public:
    ASAR();

    void readInfrared(bool&, bool&);
    bool compareDistance(uint8_t);

    void moveForward();
    void stop();

    bool headNorth();
    bool headEast();
    bool headSouth();
    bool headWest();

    void rotateCounterClockwise(int, int);
    void rotateClockwise(int, int);
};

#endif