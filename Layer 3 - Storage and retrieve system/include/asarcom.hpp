#ifndef ASARCOM_HPP
#define ASARCOM_HPP

#include <Arduino.h>
#include <LinkedList.h>

#define BUFF_SIZE 512

// Instructions to be passed in the message for the robot.
enum instructions {goToStation, rotateEast, rotateWest, approachShelf, leaveShelf, storageTray, retrieveTray, backToBase};

typedef struct {
    char instruction;
    String body;
    int checksum;   // instruction + body.size() = checksum value
} Command;

class ASARCOM {
private:
    byte* buffer;
    int readBytes;
    LinkedList<Command> pipeline;

public:
    ASARCOM();
    void readStream();
    void addInstruction(Command);
    void stopProcess();
    Command interpretInput(bool& _validChecksum);
    int calculateChecksum(Command);
};

#endif // ASARCOM_HPP