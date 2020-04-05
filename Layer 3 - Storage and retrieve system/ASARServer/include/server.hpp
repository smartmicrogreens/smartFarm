#ifndef SERVER_H
#define SERVER_H

#include <ESP8266WiFi.h>

class ASARServer {
private:
    WiFiServer* server;
    WiFiClient* client;

    const char* ssid = "testing";
    const char* password = "1234567890";

public:
    ASARServer();
    String read();
};

#endif