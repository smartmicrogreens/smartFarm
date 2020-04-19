#include <asarcom.hpp>
#include <CRC32.h>

ASARCOM::ASARCOM() {
    Serial1.begin(ESP8266_BAUD_RATE);   // Start communication with ESP8266(DO NOT CHANGE)
    crc.reset();
}

void ASARCOM::addInstruction(Command) {

}
void ASARCOM::stopProcess() {

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

void ASARCOM::read(uint8_t& _instruction, String& _buffer, bool& _validChecksum) {
    String startSeq, input, checksum;

    //crc.reset();
    if(Serial1.available() > 0) 
    {
        startSeq = Serial1.readStringUntil('d');   // Read once and check if is begin-of-line character.

        if(startSeq == "ar") 
        {
            input = Serial1.readStringUntil('%');
            _instruction = input.toInt();
            input.remove(0);
            checksum = Serial1.readStringUntil('>');

            for(unsigned int i=0; i<input.length(); i++)
                crc.update( (uint8_t) input.charAt(i) );

            _validChecksum = crc.finalize() == (uint32_t)checksum.toInt();
            //Serial.print("Checksum: ");
            //Serial.println(_validChecksum ? "TRUE" : "FALSE");
            _buffer = input;

            crc.reset();
        }
    }

}

void ASARCOM::write(String _body) {
    //String output;
    CRC32 crc;
    crc.reset();
    // Iterate while udpate CRC value per value 
    for(unsigned int i=0; i<_body.length(); i++)
        crc.update( (uint8_t) _body.charAt(i) ); 

    Serial1.print("esp" + _body + "%" + crc.finalize() + ">");
}