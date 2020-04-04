#include "asar.hpp"

ASAR::ASAR( int MOTOR_R_A,
            int MOTOR_R_B,
            int MOTOR_L_A,
            int MOTOR_L_B,
            int US_PING,
            int US_ECHO,
            int RFID_SS,
            int RFID_RST,
            int RIGHT_IR_PIN,
            int LEFT_IR_PIN) {

    rightMotor = new Motor(MOTOR_R_A, MOTOR_R_B);
    leftMotor = new Motor(MOTOR_L_A, MOTOR_L_B);
    usSensor = new Ultrasonic(US_PING, US_ECHO);
    rfidSensor = new MFRC522(RFID_SS, RFID_RST);   // Create MFRC522 instance.
    IR_L_PIN = LEFT_IR_PIN;
    IR_R_PIN = RIGHT_IR_PIN;

    /* Initialization of RFID reader */
    SPI.begin();  // SPI initialized for RFID board
    rfidSensor->PCD_Init(); // Init MFRC522 card
    delay(4);
}

void ASAR::readInfrared(bool& R, bool& L) {
    // Reads both sensors and compare with 1. If 1, will turn true, if 0 will turn false.
    R = digitalRead(IR_R_PIN) == 1;
    L = digitalRead(IR_L_PIN) == 1;
}

bool ASAR::compareDistance(uint8_t _distance) {
    // _distance can be between 2 and 400 cm
    if(usSensor->read() == _distance) return true;
    else return false;
}

String ASAR::readStationID() {
    // Time to read the card's UID is 10~11ms
    rfidSensor->PICC_ReadCardSerial();
    String uid(rfidSensor->uid.uidByte[0]);
    for(int i=0; i<9; i++)
        uid.concat(rfidSensor->uid.uidByte[i]);
    return uid;
}

bool ASAR::hasArrivedToStation() {
    // Time to detect the card is 3ms
    return rfidSensor->PICC_IsNewCardPresent();
}

void ASAR::moveForward() {

    if(IR_R && IR_L) {
        this->rightMotor->updateSpeed(180);
        this->leftMotor->updateSpeed(180);
        this->rightMotor->moveForward();
        this->leftMotor->moveForward();
    }
    else if(!IR_R && IR_L) {
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

