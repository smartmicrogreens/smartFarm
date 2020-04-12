#include <asarcom.hpp>
#include <CRC32.h>

ASARCOM::ASARCOM() {
    Serial1.begin(ESP8266_BAUD_RATE);   // Start communication with ESP8266(DO NOT CHANGE)

    /* ESP6288 TRASH AVOID WORKAROUND
     * Below code delays 6 sec to avoid the trash data from ESP8266.
     * Then, once it arrives, it is known beforehand that the total is 63 bytes.
     * We read the bytes into a trash can array and forget about get rid of it.
     * */
    // delay(6000);
    // uint8_t tcan[63];
    // if(Serial1.available() > 0) Serial1.readBytes(tcan, 63);

}

void ASARCOM::addInstruction(Command) {

}
void ASARCOM::stopProcess() {

}
int ASARCOM::calculateChecksum(Command) {
    
}

bool ASARCOM::read(LinkedList<char>& _buffer) {

    char input;
    if(Serial1.available() > 0) 
    {
      input = Serial1.read();   // Read once and check if is begin-of-line character.
      if(input == '@') 
      {
         input = Serial1.read();    // Read next
         while (input != '>')       // Keep reading and saving until end-of-line character.
         {
            if(input > 0)           // User to avoid trash from ESP8266 serial(Yes, chinese garbage)
            {
                crc.update(input);    // Update CRC
                //Serial.print(input);  
                _buffer.add(input);     // Add char to buffer
            }
            input = Serial1.read();
         }

      //Serial.println(" ");
      Serial.print("Checksum = ");
      Serial.println(crc.finalize(), HEX);
      crc.reset();

      }
    }


    // bool checksumValid = false;
    // Command temp;
    // char readCharacter;
    // int i = 0;
    // crc.reset();
    // if(Serial1.available() <= 0) return false;
    // else 
    // {
    //     readCharacter = Serial1.read();
    //     if(readCharacter == '@') // Looks for character of beggining of line
    //     {
    //         Serial.print("@ ");

    //         /* 
    //          * Read BODY of the message */
    //         bool endOfTransmision = false;
    //         while(!endOfTransmision) 
    //         {
    //             readCharacter = Serial1.read();
    //             if(readCharacter != '%')    // While eol character is not present, continue reading.
    //             {
    //                 buffer.add(readCharacter);
    //                 crc.update(readCharacter);
    //             }
    //             else endOfTransmision = true;   // End of line character detected
    //         }

    //         /* 
    //          * Read CHECKSUM of the message */
    //         //bool endOfChecksum = false;
    //         //while (!endOfChecksum) 
    //         //{
    //         readCharacter = Serial1.read();
    //         Serial.print("Checksum(Serial) = ");
    //         Serial.println(checksum, BIN);
    //         //}
    //         Serial.print("Checksum size = ");
    //         Serial.println(i);
    //         checksumValid = crc.finalize() == checksum;
    //     }
    //     readBytes = buffer.size();
    //     //temp = interpretInput(checksumValid);   // converts from array of data to command type
    //     // Validates checksum
    //     if(checksumValid) {
    //         pipeline.add(temp);
    //         Serial.print("Checksum(CRC32) = ");
    //         Serial.println(crc.finalize(), HEX);
    //     }
    //     else return false;
    // }
    // return true;
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