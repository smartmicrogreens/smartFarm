#include "server.hpp"

ASARServer::ASARServer() {

    //Serial.flush();
    Serial.begin(BAUD_RATE);
    delay(1000);
    server = new WiFiServer(TELNET_PORT);
    clients = new WiFiClient;

    WiFi.mode(WIFI_STA);
    WiFi.begin("testing", "1234567890");

    Serial.println("Connecting");
    while (WiFi.status() != WL_CONNECTED) delay(500);


    server->setNoDelay(true);
    Serial.write("@Connected to WiFi - Your IP:");
    Serial.println(WiFi.localIP());
    Serial.write('>');
    
    server->begin();
    maxToTcp = 0;
    //client = new WiFiClient();
}
void ASARServer::displayConnectedUsers() {
    
    if (server->hasClient())  // If User is waiting to connect
        if (!clients->connected()) { // Check if no user is connected
            *clients = server->available(); // Then add the one waiting to connect
            Serial.println(START_C);
            Serial.print("Client connected - IP: ");
            Serial.println(clients->remoteIP().toString());
            Serial.print(END_C);
        }
}

void ASARServer::updateIOStreams() {
    bool clientFlag = false;
    //if(clients->;
    // Update for incoming messages(From WiFi to Serial port)
    if(clients->available() && Serial.availableForWrite() > 0) Serial.println(START_C);

    while (clients->available() && Serial.availableForWrite() > 0) {
        // working char by char is not very efficient
        Serial.write(clients->read());
        clientFlag = true;

        maxToTcp = 0;   // Max data to send by TCP
        if (clients) {
            size_t afw = clients->availableForWrite();
            if (afw) {
                if (!maxToTcp) maxToTcp = afw;
                else maxToTcp = std::min(maxToTcp, afw);
            } 
        }
    }
    if(clientFlag) Serial.write(END_C);



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
