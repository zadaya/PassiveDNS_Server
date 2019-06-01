import socket
import threading


def udpRecvfromData():
    ip_port = ("", 10025)
    udpRecv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    udpRecv.bind(ip_port)
    while True:
        print("wait revcData……")
        data, sourceAddr = udpRecv.recvfrom(1024)
        print(str(data, "utf-8"))
    udpRecv.close()


def udpSendtoData():
    ip_port = ("127.0.0.1", 10025)
    udpSend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    while True:
        inp = input("数据：").strip()
        if inp == "exit":
            break
        print(inp)
        udpSend.sendto(bytes(inp, encoding="utf-8"), ip_port)
    udpSend.close()


# 开启一个线程循环接收数据
recvThread = threading.Thread(target=udpRecvfromData, name="RecvfromDataThread")
recvThread.start()

sendtoThread = threading.Thread(target=udpSendtoData, name="SendtoDataThread")
sendtoThread.start()
