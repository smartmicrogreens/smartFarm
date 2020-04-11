#include <asarcom.hpp>
#include <CRC32.h>

ASARCOM::ASARCOM() {
    // Connect this communication stream to interruption
    Serial1.begin(74880);   // Start communication with ESP8266
    //Serial1.println("Connected to ESP8266");
}

void ASARCOM::addInstruction(Command) {

}
void ASARCOM::stopProcess() {

}
int ASARCOM::calculateChecksum(Command) {
    
}

bool ASARCOM::read() {
    bool checksumValid = false;
    Command temp;
    char readCharacter;
    int i = 0;
    crc.reset();
    if(Serial1.available() <= 0) return false;
    else 
    {
        readCharacter = Serial1.read();
        if(readCharacter == '@') // Looks for character of beggining of line
        {
            Serial.print("@ ");

            /* 
             * Read BODY of the message */
            bool endOfTransmision = false;
            while(!endOfTransmision) 
            {
                readCharacter = Serial1.read();
                if(readCharacter != '%')    // While eol character is not present, continue reading.
                {
                    buffer.add(readCharacter);
                    crc.update(readCharacter);
                }
                else endOfTransmision = true;   // End of line character detected
            }

            /* 
             * Read CHECKSUM of the message */
            //bool endOfChecksum = false;
            //while (!endOfChecksum) 
            //{
            readCharacter = Serial1.read();
            Serial.print("Checksum(Serial) = ");
            Serial.println(checksum, BIN);
            //}
            Serial.print("Checksum size = ");
            Serial.println(i);
            checksumValid = crc.finalize() == checksum;
        }
        readBytes = buffer.size();
        //temp = interpretInput(checksumValid);   // converts from array of data to command type
        // Validates checksum
        if(checksumValid) {
            pipeline.add(temp);
            Serial.print("Checksum(CRC32) = ");
            Serial.println(crc.finalize(), HEX);
        }
        else return false;
    }
    return true;
}

Command ASARCOM::interpretInput(bool& _validChecksum) {
    // [Instruction(1Byte)] - [Body(nBytes)] - [Checksum(1Byte)]
    // Transfers data from byte array to a Command type.
    // Return if checksum was correct or not.
    // Command output;
    // int checksum;

    // // Update index 0 value for Command type and crc
    // output.instruction = buffer.get(0);
    // crc.update(buffer.get(0));

    // // Update for the rest of the data
    // for(int i=1; i<buffer.size(); i++){
    //     crc.update(buffer.get(i));
    //     output.body.concat(buffer.get(i));
    // }
    // output.checksum = buffer[readBytes];
    // checksum = (int8_t) checksum/buffer[0];
    // _validChecksum = output.checksum == checksum;
    // return output;
}