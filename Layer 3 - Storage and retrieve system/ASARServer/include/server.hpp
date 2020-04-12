#ifndef SERVER_H
#define SERVER_H

#include <ESP8266WiFi.h>
#include <SoftwareSerial.h>
#include <CRC32.h>

#define STACK_PROTECTOR 512
#define TELNET_PORT 23
#define BAUD_RATE 74800
#define START_C "abc"
#define END_C '>'

class ASARServer {
private:
    const char* ssid = "testing";
    const char* password = "1234567890";
    //const size_t STACK_PROTECTOR = 512;

    WiFiServer* server;
    WiFiClient* clients;
    size_t maxToTcp;
    bool dataFlag;
    //CRC32 crc;
    //SoftwareSerial* logger;

public:
    ASARServer();
    void displayConnectedUsers();
    void updateIOStreams();
    String encapsulate(String);
};

#endif