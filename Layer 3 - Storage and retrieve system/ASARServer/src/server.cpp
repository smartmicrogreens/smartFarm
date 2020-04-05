#include "server.hpp"

ASARServer::ASARServer() {
    Serial.begin(115200);
    delay(1000);
    server = new WiFiServer(80);
    WiFi.mode(WIFI_STA);
    WiFi.begin("testing", "1234567890");
    Serial.print("Connecting");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println(" ");
    Serial.print("Connected to WiFi. IP:");
    Serial.println(WiFi.localIP());
    
    server->begin();
    //client = new WiFiClient();
}
String ASARServer::read() {
    client = new WiFiClient( server->available() );
 
  if (client) {
    //uint8_t buffer[160];
    while (client->connected()) {
 
        while (client->available() > 0) {
            char c = client->read();
            Serial.write(c);
        //char c = client->read(buffer, 160);
        }
 
        delay(10);
        client->stop();
        Serial.println("Client disconnected");
    }
 
  }
  delete client;
  return "OK";
}