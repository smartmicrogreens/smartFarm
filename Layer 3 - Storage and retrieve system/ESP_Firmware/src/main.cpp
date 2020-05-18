#include <Arduino.h>
#include <SimpleDHT.h>
#include <ESP8266WiFi.h>

#define STACK_PROTECTOR 512
#define PORT 23  // 23 -> Telnet port
#define BAUD_RATE 74800 // This baud rate allows to see the flash mem. output.
#define LIGHTS 4

/* Function definition */
void scanclient();  // Checks for available clients to connect
void receive(); // Checks and received incoming data
void split(String, byte*);
void interpret(char); // Interpret incoming instructions and executes action
void printLightStatus(); // Prints to client the status of all lights

const char* ssid = "testing";
const char* password = "1234567890";
// const char* ssid = "wabisabihouse654_NW";
// const char* password = "wabisabihouse654";
const int LIGHT_PINOUT[LIGHTS] = {0,4,5,16};
const int DEHUMIDIFIER_PIN = 1;
const int DHT_DATA_PIN = 2;
const int CONNECTED = 15;

WiFiServer* server;
WiFiClient* client;
SimpleDHT11 dht11(DHT_DATA_PIN);

String buffer;
byte temperature;
byte humidity;
int instruction = -1;

void setup() {

  /* INITIALIZE CONTROL PINS */
  pinMode(DEHUMIDIFIER_PIN, OUTPUT); digitalWrite(DEHUMIDIFIER_PIN, LOW); // Initialize dehumidifier GPIO
  pinMode(CONNECTED, OUTPUT); digitalWrite(CONNECTED, LOW); // Initialize WiFi connection indicator GPI15
  for(int i=0; i<LIGHTS; i++) { 
    pinMode(LIGHT_PINOUT[i], OUTPUT); digitalWrite(LIGHT_PINOUT[i], LOW); 
  }

  Serial.begin(BAUD_RATE);
  delay(500);
  //Serial.swap();
  server = new WiFiServer(PORT);
  client = new WiFiClient;

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  if (Serial.availableForWrite()) Serial.println("Connecting");
  while (WiFi.status() != WL_CONNECTED) delay(500);

  server->setNoDelay(true);
  server->begin();
  Serial.print("<Connected as " + WiFi.localIP().toString() + ">");

  //client->println("Initialization completed.");

}

void loop() {
  scanclient(); // Handles connection to client 
  receive();  // Receives messages from client
}

void inline scanclient() {
  if (server->hasClient())  // If User is waiting to connect
    if (!client->connected()) { // Check if no user is connected
      *client = server->available(); // Then add the one waiting to connect
      //client->print(HEADER + "WiFI status: " + WiFi.status() == WL_CONNECTED ? "TRUE" : "FALSE");
      // client->println ("Telnet connection opened: ");
      // client->println (" -Your IP: " + client->remoteIP().toString());
      // client->println (" -Server IP: " + client->localIP().toString());
      // client->print   (" -Your port: "); client->println(client->remotePort());
      // client->print   (" -Server port: "); client->println(client->localPort());
      digitalWrite(CONNECTED, HIGH);
      
    }
  if(!client->connected()) digitalWrite(CONNECTED, LOW);
}

void inline receive() {
  // Receive data
  if  (client->available() > 0) 
    if  (client->read() == '<') {
      buffer = client->readStringUntil('>');
      interpret(buffer.charAt(0));
    }
}

void interpret(char _instruction) {
  /* OPTION 0: Replies with humidity and temperature information from the sensor. */
  if (_instruction == '0') {
    int dhterr = SimpleDHTErrSuccess;
    if((dhterr = dht11.read(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
      client->print("99;Read DHT11 failed, err="); client->println(dhterr);
    } else {
      // We reply for instruction 0, separating temperature and humidity with ';'
      String output = "0;"; output.concat(temperature); output.concat(";"); output.concat(humidity);;
      client->print(output);
    }
  }
  /* OPTION 1: Switches dehumidifier current state. */
  /* Probably will be updated in order to achive PWM control over the pump
    * in order to manage the overall power of it. */
  else if (_instruction == '1') { 
    if(digitalRead(DEHUMIDIFIER_PIN) == HIGH) 
      digitalWrite(DEHUMIDIFIER_PIN, LOW);
    else
      digitalWrite(DEHUMIDIFIER_PIN, HIGH);
    client->println("<" + (String)(digitalRead(DEHUMIDIFIER_PIN) == HIGH ? "1" : "0") + ">");
  }

  /* OPTION 2: Lights control */
  else if (_instruction == '2') {
    if(buffer.length() == 5 + LIGHTS) {
      for(int i=0; i<LIGHTS; i++) {
        if(buffer.charAt(i*2+2) == '1')
          digitalWrite(LIGHT_PINOUT[i], HIGH);
        else digitalWrite(LIGHT_PINOUT[i], LOW);
      }
    }
    printLightStatus();  
  }
  /* OPTION 99: Wrong input */
  else client->println("<99>"); // Int 99 means unknown command.

  buffer.clear(); // Clean buffer;
}

void printLightStatus() {
  String output = "<2;";
  int i=0;
  for(;i<LIGHTS-1; i++) 
    output.concat((String)(digitalRead(LIGHT_PINOUT[i]) == HIGH ? "1" : "0") + ";");
    output.concat((String)(digitalRead(LIGHT_PINOUT[i]) == HIGH ? "1" : "0") + ">");
  client->println(output);
}