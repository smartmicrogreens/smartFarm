#ifndef ASARENCAPSULATION_H
#define ASARENCAPSULATION_H
#include <CRC32.h>
#include <QString>
#include <QDebug>

#define START_C "*esp*"
#define MIDDLE_C "%"
#define END_C ">"

class ASAREncapsulation
{
    CRC32* crc;
public:
    ASAREncapsulation();
    QString encapsulate(QString _instruction, QString _body);
    QString decapsulate(QString _package, bool& _validChecksum);
};

#endif // ASARENCAPSULATION_H
