# coding:utf-8

from scapy.layers.inet import *
from scapy.all import sniff

def pack_callback(packet):
    # print(packet.show())
    if packet[UDP].payload:
        if (packet.sprintf("%DNS.qr%") == "1"):
            print(packet.show())
        # if (packet.sprintf("%DNS.qr%") == "0"):
        #     print("\n\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\n")

        # aaaa=packet.sprintf("Etherent source: %Ether.src%    IP src: %IP.src%    DNS src: %DNS.id%")
        # print(aaaa)
        # print("###################################################################")
    
        # DNS_packet = str(packet[UDP].payload)
        # if "user" in DNS_packet.lower() or "pass" in DNS_packet.lower():
        #     print("Server:%s" % packet[IP].dst)
        #     print("%s" % packet[UDP].payload)

#sniff()第一个参数可以筛选协议类型及端口号，第二个参数设置监听的网卡名
dnsSniffPacket = sniff(filter="udp port 53", iface='Realtek PCIe GbE Family Controller', prn=pack_callback, count=100)
