#ifndef SERVER_H
#define SERVER_H

#include <ESP8266WiFi.h>
#include <SoftwareSerial.h>
#include <CRC32.h>

#define STACK_PROTECTOR 512
#define TELNET_PORT 23
#define BAUD_RATE 74800

class ASARServer {
private:
    const char* ssid = "testing";
    const char* password = "1234567890";
    const String TO_ARD_START_C = "ard";
    const String FROM_ARD_START_C = "esp";
    //const size_t STACK_PROTECTOR = 512;

    WiFiServer* server;
    WiFiClient* clients;
    size_t maxToTcp;
    bool dataFlag;
    String body;
    //CRC32 crc;
    //SoftwareSerial* logger;

public:
    ASARServer();
    void displayConnectedUsers();
    void updateIOStreams();
    String encapsulate(String);
    String decapsulate(String, bool&);
};

#endif