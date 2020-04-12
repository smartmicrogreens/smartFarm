#include <asarcom.hpp>
#include <CRC32.h>

ASARCOM::ASARCOM() {
    Serial1.begin(ESP8266_BAUD_RATE);   // Start communication with ESP8266(DO NOT CHANGE)
    crc.reset();
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
    String startSeq;
    char input;
    if(Serial1.available() > 0) 
    {
      startSeq = Serial1.readStringUntil('c');   // Read once and check if is begin-of-line character.
      Serial.println(startSeq);
      if(startSeq == "ab") 
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
}

bool ASARCOM::read(String& _buffer) {
    String startSeq, input, checksum;
    bool checksumValid = false;
    //crc.reset();
    if(Serial1.available() > 0) 
    {
        startSeq = Serial1.readStringUntil('c');   // Read once and check if is begin-of-line character.
        if(startSeq == "ab") 
        {
            input = Serial1.readStringUntil('%');
            checksum = Serial1.readStringUntil('>');
            //Serial.println(startSeq + "c" + input + "%" + checksum + ">");
            Serial.println(input);

            for(unsigned int i=0; i<input.length(); i++)
                crc.update( (uint8_t) input.charAt(i) );

            checksumValid = crc.finalize() == (uint32_t)checksum.toInt();

            // CHECKSUM VALIDATION CONTROL
            //Serial.print("ChecksumIsValid? = ");
            //Serial.println(checksumValid ? "TRUE" : "FALSE");
            //Serial.print(crc.finalize(), HEX);
            //Serial.print(" = ");
            //Serial.println((uint32_t)checksum.toInt(), HEX);
            
            crc.reset();
        }
        return checksumValid;
    }
}