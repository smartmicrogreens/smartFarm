#include <asarcom.hpp>

ASARCOM::ASARCOM() {
    // Connect this communication stream to interruption

}

void ASARCOM::addInstruction(Command) {

}
void ASARCOM::stopProcess() {

}
int ASARCOM::calculateChecksum(Command) {
    
}

Command ASARCOM::interpretInput(bool& _validChecksum) {
    // [Instruction(1Byte)] - [Body(nBytes)] - [Checksum(1Byte)]
    // Transfers data from byte array to a Command type.
    // Return if checksum was correct or not.
    Command output;
    int checksum = 0;
    output.instruction = buffer[0];
    for(int i=1; i<(readBytes-1); i++){
        checksum += (int8_t)buffer[i];
        output.body.concat(buffer[i]);
    }
    output.checksum = buffer[readBytes];
    checksum = (int8_t) checksum/buffer[0];
    _validChecksum = output.checksum == checksum;
    return output;
}