#include <asarcom.hpp>

ASARCOM::ASARCOM() {
    // Connect this communication stream to interruption
    Serial1.begin(38400);   // Start communication with ESP8266
    Serial1.println("Connected to ESP8266");
}
