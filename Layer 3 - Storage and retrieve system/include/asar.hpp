#ifndef ASAR_HPP
#define ASAR_HPP

#include <Arduino.h>
#include <LinkedList.h>
#include <Ultrasonic.h>
#include <MFRC522.h>
#include "motor.hpp"

class ASAR {

private:
    int direction;
    String curStation;
    String previousStation;
    Motor* leftMotor;
    Motor* rightMotor;
    Ultrasonic* usSensor;
    MFRC522* rfidSensor;

    /* CONSTANTS */
    // Direction constants
    const int NORTH = 0;
    const int SOUTH = 1;
    const int EAST = 2;
    const int WEST = 3;

    // Time constants. How much rotation time it is needed to achieve a certain angle. 
    // Values needs to be tested. The current ones were defined without any mesurement.
    const int TIME_90 = 1500;
    const int TIME_180 = 3000;
    const int TIME_360 = 6000;

    // Robot physical parameters
    const int radiusChasis = 0.25; // Radius of the chasis(From center of the robot to the center of the wheel, looking from above).
    const int radiusWheels = 0.05; // Radius of the wheel
    const int motorTurnSteps = 200; // Motor total steps in one turn

    // // Pins corresponding to ultrasonic and 
    // int US_PING;
    // int US_ECHO;
    // int RFID_SS;
    // int RFID_RST;

    // // Motor Right and Left pins
    // int MOTOR_R_A;
    // int MOTOR_R_B;
    // int MOTOR_L_A;
    // int MOTOR_L_B;

    // Infrared sensor pins and read variables
    int IR_R_PIN;
    int IR_L_PIN;
    bool IR_R, IR_L; 

public:
    ASAR(   int MOTOR_R_A,
            int MOTOR_R_B,
            int MOTOR_L_A,
            int MOTOR_L_B,
            int US_PING,
            int US_ECHO,
            int RFID_SS,
            int RFID_RST,
            int RIGHT_IR_PIN,
            int LEFT_IR_PIN);

    void readInfrared(bool&, bool&);
    bool compareDistance(uint8_t);

    String readStationID();
    bool hasArrivedToStation();

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