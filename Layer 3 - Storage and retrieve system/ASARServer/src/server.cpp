#include "server.hpp"

ASARServer::ASARServer() {

    Serial.begin(115200);
    delay(1000);
    server = new WiFiServer(23);
    clients = new WiFiClient;
    WiFi.mode(WIFI_STA);
    WiFi.begin("testing", "1234567890");
    Serial.print("Connecting");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println(" ");
    server->setNoDelay(true);
    Serial.print("Connected to WiFi. IP:");
    Serial.println(WiFi.localIP());
    
    server->begin();
    //client = new WiFiClient();
}
void ASARServer::displayConnectedUsers() {
    size_t maxToTcp = 0;
    if (server->hasClient())
        if (!clients->available()) { // equivalent to !serverClients[i].connected()
            *clients = server->available();
            Serial.print("Client connected .-");
        }

    while (clients->available() && Serial.availableForWrite() > 0) {
        // working char by char is not very efficient
        Serial.write(clients->read());

        maxToTcp = 0;
        if (clients) {
            size_t afw = clients->availableForWrite();
            if (afw) {
                if (!maxToTcp) maxToTcp = afw;
                else maxToTcp = std::min(maxToTcp, afw);
            } 
        }
    }
    
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