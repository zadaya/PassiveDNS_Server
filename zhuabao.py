# coding:utf-8

from scapy.layers.inet import *
from scapy.sendrecv import sniff

def pack_callback(packet):
    print(packet.show())
    if packet[UDP].payload:
        mail_packet = str(packet[UDP].payload)
        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print("Server:%s" % packet[IP].dst)
            print("%s" % packet[UDP].payload)

#sniff()第一个参数可以筛选协议类型及端口号，第二个参数设置监听的网卡名
sniff(filter="udp port 53", iface='Realtek PCIe GbE Family Controller', prn=pack_callback, count=100)