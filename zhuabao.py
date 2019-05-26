from scapy.layers.inet import *
from scapy.all import sniff
import os


def pack_callback(packet):
    # print(packet.show())
    if packet[UDP].payload:
        if (packet.sprintf("%DNS.qr%") == "1"):
            # print(packet[UDP].show())
            # packet['DNSRR'].show()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for i in range(1,packet['DNS'].ancount+1):
                domain_str = packet['DNSRR'][i-1].rrname
                ipaddr_str = packet['DNSRR'][i-1].rdata
                print("[No.%d] response: Qname: %s    Rdata: %s" % (i, domain_str, ipaddr_str))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# sniff()第一个参数可以筛选协议类型及端口号，第二个参数设置监听的网卡名
iface = os.getenv("IFACE", "Realtek PCIe GbE Family Controller")
dnsSniffPacket = sniff(filter="udp port 53", iface=iface, prn=pack_callback, count=0)
