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
    

    // Update for outcoming messages(From Serial port to WiFi)
    // Checks UART data
    size_t len = std::min((size_t)Serial.available(), maxToTcp);
    len = std::min(len, (size_t)STACK_PROTECTOR);
    if (len) {
        uint8_t sbuf[len];
        size_t serial_got = Serial.readBytes(sbuf, len);
        // push UART data to all connected telnet clients
        // if client.availableForWrite() was 0 (congested)
        // and increased since then,
        // ensure write space is sufficient:
        if (clients->availableForWrite() >= serial_got) {
            size_t tcp_sent = clients->write(sbuf, serial_got);
            if (tcp_sent != len)  Serial.printf("len mismatch: available:%zd serial-read:%zd tcp-write:%zd\n", len, serial_got, tcp_sent);
        }
    }
}

String ASARServer::encapsulate(String _body) {
    String output;
    CRC32 crc;
    crc.reset();
    for(unsigned int i=0; i<_body.length(); i++)
        crc.update( (uint8_t) _body.charAt(i) );
    String checksum(crc.finalize());
    output.concat("abc" + _body + "%" + checksum + ">");
    return output;
}