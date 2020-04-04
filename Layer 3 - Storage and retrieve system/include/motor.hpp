#ifndef MOTOR_HPP
#define MOTOR_HPP

#include <Arduino.h>

class Motor {

private:
    int pinA, pinB;
    int speed;
    const int REGULAR_SPEED = 40;
public:
    Motor(int, int, int);
    Motor(int, int);
    void moveForward();
    void moveBackward();
    void setNominalSpeed();
    void updateSpeed(int);
    void stop();
};

#endif