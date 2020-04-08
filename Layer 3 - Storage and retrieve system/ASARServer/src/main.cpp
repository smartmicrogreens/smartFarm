//#include <Arduino.h>
#include "server.hpp"
ASARServer* server;
void setup() {
  // put your setup code here, to run once:
  server = new ASARServer();
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println( server->read() );
  server->displayConnectedUsers();
  server->updateIOStreams();
}