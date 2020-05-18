#include "asarencapsulation.h"

#define DO_DEBUG 0

ASAREncapsulation::ASAREncapsulation()
{
    crc = new CRC32();
    crc->reset();
}

QString ASAREncapsulation::encapsulate(QString _instruction, QString _body) {
    crc->reset();

    // Iterate while udpate CRC value per value
    for(int i=0; i<_body.length(); i++)
        crc->update( (uint8_t) _body.at(i).toLatin1() );

    // Calculate checksum once all values were included.
    QString checksum(QString::number(crc->finalize()));
    #if DO_DEBUG == 1
        qDebug() << _body;
        qDebug() << "(Encap) " << checksum;
    #endif
    // Concatenate to achieve the full chain with begin, middle and end characters.
    //return "*ard*" + _instruction + "%" + _body + MIDDLE_C + checksum + END_C;
        return "<" + _body + ">";
}

QString ASAREncapsulation::decapsulate(QString _package, bool& _validChecksum) {
    QString instruction, output, checksum;
    uint32_t checksumVal;
    crc->reset();

    if(_package.startsWith('<')) {
        _package.remove('<');
        _package.remove('>');
        qDebug() << _package;
        return _package;   // Removes ends and returns the body
    } else {
        QString ret = "Error: Wrong start seq. (" + _package + ")";
    }

//    if(_package.startsWith(START_C))
//    {
//        // Extract Instruction
//        instruction = _package.section('%', 0);  // Returns the string from the beggining to '%'
//        instruction.remove(0, 5); // Removes START_C
//        output.remove(output.indexOf('%'), output.length());

//        // Extract OUTPUT
//        output = _package.section('%', 0);  // Returns the string from the beggining to '%'
//        //output.remove(0, 5);
//        output.remove(output.indexOf('%'), output.length());    // Removes first 3 characters

//#if DO_DEBUG == 1
//        qDebug() << output;
//#endif

//        // Extract CHECKSUM
//        checksum = _package.remove(0, _package.indexOf('%')+1);  // Leaves only the tail.
//        checksum.chop(1);
//        checksumVal = (uint32_t) checksum.toULong();

//#if DO_DEBUG == 1
//        qDebug() << "Received: " << checksum;
//#endif

//        // Calculate checksum based on output
//        for(int i=0; i<output.length(); i++)
//            crc->update( (uint8_t) output.at(i).toLatin1() );

//#if DO_DEBUG == 1
//        qDebug() << "Calculated: " << crc->finalize();
//#endif

//        // Validate checksum
//        _validChecksum = crc->finalize() == checksumVal;

//        if(_validChecksum) return output;                   // If checksum is correct, return the string
//        else return "Error: Invalid Checksum(" + checksum + ")";     // Otherwise, return null string.
//    }
//    else return "Error: Wrong start sequence received.";
}
