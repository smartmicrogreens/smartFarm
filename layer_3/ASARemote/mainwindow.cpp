#include "mainwindow.h"
#include "ui_mainwindow.h"

#define TELNET_PORT 23

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
    , tcpSocket(new QTcpSocket(this))
{
    ui->setupUi(this);
    in.setDevice(tcpSocket);
    in.setVersion(QDataStream::Qt_4_9);
    peer = new QHostAddress("192.168.0.128");
    //tcpSocket->setPeerAddress(*peer);
    //tcpSocket->setPeerPort(23);
    connect(tcpSocket, &QIODevice::readyRead, this, &MainWindow::updateInputBuffer);

    // Initialize flags
    isConnected = false;

    // Initialize GUI
    ui->teConsole->setReadOnly(true);
    QColor a(0, 255, 0);
    ui->teConsole->setTextColor(a);

    // Initialize Objects
    encapsulation = new ASAREncapsulation();
}

void MainWindow::send(QString _inst, QString _msg)
{
    tcpSocket->write( encapsulation->encapsulate(_inst, _msg).toLatin1() );
}

void MainWindow::updateInputBuffer()
{
    QString line("Robot-> ");
    QString buffer, checksum;
    bool checksumValid = true;
//    checksum = buffer;
//    buffer = buffer.remove(0, 3);
//    checksum.remove(0, checksum.indexOf('%'));
//    buffer.remove(buffer.indexOf('%'), buffer.length());
    //buffer = encapsulation->decapsulate(tcpSocket->readAll(), checksumValid);
    buffer = encapsulation->decapsulate(tcpSocket->readAll(), checksumValid);
    qDebug() << buffer;
    ui->teConsole->append(line + buffer);
}

void MainWindow::on_btnConnect_clicked()
{
    if(!isConnected) {
        tcpSocket->abort();
        tcpSocket->connectToHost(*peer, 23);
        if(tcpSocket->isOpen()) {
            ui->teConsole->append("Connected from -> " +
                                  tcpSocket->localAddress().toString() +
                                  "(" + QString::number(tcpSocket->localPort()) + ")");
            isConnected = true;
            ui->btnConnect->setText("Disconnect");
        }
    } else {
        tcpSocket->disconnectFromHost();
        isConnected = false;
        ui->btnConnect->setText("Connect");
    }

}

// Instructions to be passed in the message for the robot.

#define GO_TO_STATION       "0"
#define ROTATE_EAST           "1"
#define ROTATE_WEST          "2"
#define APPROACH_SHELF  "3"
#define LEAVE_SHELF          "4"
#define STORAGE_TRAY        "5"
#define RETRIEVE_TRAY       "6"
#define BACK_TO_BASE       "7"

void MainWindow::on_btnMoveToStation_clicked()
{
    QString instruction(GO_TO_STATION);
    QString body = "body";
    send(instruction, body);
}

void MainWindow::on_leCmdInput_returnPressed()
{
    if ( ! ui->leCmdInput->text().isEmpty() && tcpSocket->isOpen()) {
        //tcpSocket->write( encapsulation->encapsulate( ui->leCmdInput->text()).toLatin1() );
        send("101", ui->leCmdInput->text());
        //qDebug() << "Write -> " << encapsulation->encapsulate( ui->leCmdInput->text() ).toLatin1() ;
        ui->leCmdInput->clear();
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}
