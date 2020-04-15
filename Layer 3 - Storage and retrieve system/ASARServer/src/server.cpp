#include "server.hpp"

ASARServer::ASARServer() {

    //Serial.flush();
    Serial.begin(BAUD_RATE);
    delay(1000);
    server = new WiFiServer(TELNET_PORT);
    clients = new WiFiClient;

    WiFi.mode(WIFI_STA);
    WiFi.begin("testing", "1234567890");

    Serial.print(encapsulate("Connecting"));
    while (WiFi.status() != WL_CONNECTED) delay(500);


    server->setNoDelay(true);
    Serial.print(encapsulate("Connected to WiFi - Your IP: "));
    Serial.print(encapsulate(WiFi.localIP().toString()));
    //Serial.write('\0');
    
    server->begin();
    maxToTcp = 0;
    //client = new WiFiClient();
}
void ASARServer::displayConnectedUsers() {
    
    if (server->hasClient())  // If User is waiting to connect
        if (!clients->connected()) { // Check if no user is connected
            *clients = server->available(); // Then add the one waiting to connect
            Serial.print(encapsulate("Client connected - IP: "));
            Serial.println(encapsulate(clients->remoteIP().toString()));
        }
}

void ASARServer::updateIOStreams() {
    dataFlag = false;
    // Update for incoming messages(From WiFi to Serial port)
    if(clients->available() && Serial.availableForWrite() > 0) dataFlag = true;
    String body;

    while (clients->available() && Serial.availableForWrite() > 0) {
        // working char by char is not very efficient
        body.concat((char)clients->read());
        dataFlag = true;

        maxToTcp = 0;   // Max data to send by TCP
        if (clients) {
            size_t afw = clients->availableForWrite();
            if (afw) {
                if (!maxToTcp) maxToTcp = afw;
                else maxToTcp = std::min(maxToTcp, afw);
            } 
        }
    }
    if(dataFlag) Serial.print(encapsulate(body));
    
    size_t availableOnSerial = Serial.available();
    if(availableOnSerial <= STACK_PROTECTOR) {
        String buffer = Serial.readString();
        if(clients->availableForWrite() >= availableOnSerial  &&  buffer.length() <= STACK_PROTECTOR) 
            size_t tcp_sent = clients->print(buffer);
    }

    // // Update for outcoming messages(From Serial port to WiFi)
    // // Checks UART data
    // //bool validChecksum = false;
    // size_t len = std::min((size_t)Serial.available(), maxToTcp);
    // len = std::min(len, (size_t)STACK_PROTECTOR);
    // if (len) {
    //     uint8_t sbuf[len];
    //     //String strbuffer = Serial.readString();
    //     size_t serial_got = Serial.readBytes(sbuf, len);
    //     String strbuf((char*) sbuf); 
    //     // strbuffer = decapsulate(strbuffer, validChecksum);

    //     // push UART data to all connected telnet clients
    //     // if client.availableForWrite() was 0 (congested)
    //     // and increased since then,
    //     // ensure write space is sufficient:
    //     //if(validChecksum) {
    //         if (clients->availableForWrite() >= serial_got) {
    //             size_t tcp_sent = clients->write(sbuf, serial_got);
    //             //size_t tcp_sent = clients->println(strbuffer);
    //             if (tcp_sent != len)  Serial.printf("len mismatch: available:%zd serial-read:%zd tcp-write:%zd\n", len, serial_got, tcp_sent);
    //         }
    //     //} else clients->println("Error: Invalid checksum.");
    // }
}

String ASARServer::encapsulate(String _body) {
    CRC32 crc;
    crc.reset();

    // Iterate while udpate CRC value per value 
    for(unsigned int i=0; i<_body.length(); i++)
        crc.update( (uint8_t) _body.charAt(i) );  

    String checksum(crc.finalize());    // Calculate checksum once all values were included.
    return TO_ARD_START_C + _body + "%" + checksum + ">";    // Concatenate to achieve the full chain with begin,
                                                             // middle and end characters.
}

String ASARServer::decapsulate(String _package, bool& _validChecksum) {
    String output, checksum;
    uint32_t checksumVal;
    CRC32 crc;
    crc.reset();

    if(_package.startsWith(FROM_ARD_START_C))
    {
        output.concat(_package.substring( _package.indexOf(TO_ARD_START_C.charAt(2))+1,      // Substring between "abc" ...
                                          _package.indexOf("%")));      // and "%" --> returns the BODY

        checksum.concat(_package.substring( _package.indexOf("%")+1,    // Substring between "%" ...
                                            _package.indexOf(">")));    // and ">" --> returns the CHECKSUM

        checksumVal = (uint32_t) checksum.toInt();
        
        for(unsigned int i=0; i<output.length(); i++)   // Calculating Checksum based on the data to compare to received value.
            crc.update( (uint8_t) output.charAt(i) );


        _validChecksum = crc.finalize() == checksumVal; // Validate if checksum matches.
        
        // clients->print("Checksum = (Ard) ");
        // clients->print(checksumVal, HEX);
        // clients->print(" / (ESP) ");
        // clients->println(crc.finalize(), HEX);
        
        if(_validChecksum) return output;                   // If checksum is correct, return the string
        else return "(ESP8266) Checksum is NOT valid.";     // Otherwise, return null string.
    }

}