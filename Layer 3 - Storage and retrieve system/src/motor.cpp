#include "motor.hpp"

Motor::Motor(int _pinA, int _pinB, int _speed) {
    this->pinA = _pinA;
    this->pinB = _pinB;
    this->speed = _speed;
}

Motor::Motor(int _pinA, int _pinB) {
    this->pinA = _pinA;
    this->pinB = _pinB;
    this->speed = REGULAR_SPEED;
}

void Motor::moveForward() {
    digitalWrite(this->pinA, LOW);
    analogWrite(this->pinB, this->speed);
}

void Motor::moveBackward() {
    digitalWrite(this->pinB, LOW);
    analogWrite(this->pinA, this->speed);
}
void Motor::setNominalSpeed() {
    this->speed = this->REGULAR_SPEED;
}
void Motor::updateSpeed(int _newSpeed) {
    this->speed = _newSpeed;
}
void Motor::stop() {
    digitalWrite(this->pinA, HIGH);
    digitalWrite(this->pinB, HIGH);
}