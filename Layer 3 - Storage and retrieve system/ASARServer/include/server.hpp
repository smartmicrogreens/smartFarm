#ifndef SERVER_H
#define SERVER_H

#include <ESP8266WiFi.h>
#include <SoftwareSerial.h>

#define STACK_PROTECTOR 512

class ASARServer {
private:
    const char* ssid = "testing";
    const char* password = "1234567890";
    const int MAX_SRV_CLIENTS = 2;
    //const size_t STACK_PROTECTOR = 512;

    WiFiServer* server;
    WiFiClient* clients;
    //SoftwareSerial* logger;
public:
    ASARServer();
    void displayConnectedUsers();
    void read();
};

#endif