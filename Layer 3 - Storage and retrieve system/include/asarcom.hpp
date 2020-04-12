#ifndef ASARCOM_HPP
#define ASARCOM_HPP

#include <Arduino.h>
#include <LinkedList.h>
#include <CRC32.h>

#define BUFF_SIZE 512
#define ESP8266_BAUD_RATE 74880

// Instructions to be passed in the message for the robot.
enum instructions {goToStation, rotateEast, rotateWest, approachShelf, leaveShelf, storageTray, retrieveTray, backToBase};

typedef struct {
    char instruction;
    String body;
} Command;

class ASARCOM {
private:
    LinkedList<char> buffer;
    int readBytes;
    LinkedList<Command> pipeline;
    uint32_t checksum;   // Calculate by CRC32
    CRC32 crc;

public:
    ASARCOM();
    void readStream();
    void addInstruction(Command);
    void stopProcess();
    bool read(LinkedList<char>&);
    bool read(String&);
    void write(String);
    Command interpretInput(bool& _validChecksum);
    int calculateChecksum(Command);
};

#endif // ASARCOM_HPP