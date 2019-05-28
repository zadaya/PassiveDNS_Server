import os
import time
import datetime
import threading

from scapy.all import sniff
from scapy.layers.inet import *

from dnslogs import DnsLogs
from dnslogsDao import DnsLogsDao


def pack_callback(packet):
    print(packet.show())
    if packet[UDP].payload:
        if (packet.sprintf("%DNS.qr%") == "1"):
            # print(packet[UDP].show())
            # packet['DNSRR'].show()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for i in range(1,packet['DNS'].ancount+1):
                domain_str = str(packet['DNSRR'][0].rrname,"utf-8")
                ipaddr_str = packet['DNSRR'][i-1].rdata
                dnsclientip_str = packet['IP'].dst
                dnsserverip_str = packet['IP'].src
                print("[No.%d] response: Qname: %s    Rdata: %s" % (i, domain_str, ipaddr_str))
                print(packet['DNSRR'][i-1].type)
                if (packet['DNSRR'][i-1].type==1) or (packet['DNSRR'][i-1].type==28):
                    sniffDnsLogs.domain = domain_str
                    sniffDnsLogs.domain_ip = ipaddr_str
                    sniffDnsLogs.dns_client_ip = dnsclientip_str
                    sniffDnsLogs.dns_server_ip= dnsserverip_str
                    sniffDnsLogs.record_time=datetime.datetime.now()
                    DnsLogSDaoThread = threading.Thread(target=DBTest.checkingData(sniffDnsLogs), name="DnsLogsDaoThread")
                    DnsLogSDaoThread.start()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# sniff()第一个参数可以筛选协议类型及端口号，第二个参数设置监听的网卡名
iface = os.getenv("IFACE", "Realtek PCIe GbE Family Controller")
sniffDnsLogs = DnsLogs()
DBTest = DnsLogsDao()
while True:
    try:
        dnsSniffPacket = sniff(filter="udp port 53", iface=iface, prn=pack_callback, count=0)
    except Exception as identifier:
        pass
