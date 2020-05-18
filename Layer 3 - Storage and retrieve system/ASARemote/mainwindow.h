#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTcpSocket>
#include <QComboBox>
#include <QLabel>
#include <QNetworkSession>
#include <QDebug>
#include "asarencapsulation.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    void send(QString, QString);
    ~MainWindow();

public slots:
    void updateInputBuffer();

private slots:
    void on_btnConnect_clicked();

    void on_btnMoveToStation_clicked();

    void on_leCmdInput_returnPressed();

private:
    Ui::MainWindow *ui;

    QTcpSocket *tcpSocket = nullptr;
    QHostAddress *peer;
    QDataStream in;
    QString cmdBuffer;

    QNetworkSession *networkSession = nullptr;
    ASAREncapsulation *encapsulation;

    bool isConnected;
};
#endif // MAINWINDOW_H
