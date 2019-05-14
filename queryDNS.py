
from scapy.all import *
#导入socket的包
from socket import *

def dns_query(dns_name):
	dns_result = sr1(IP(dst="114.114.114.114")/UDP()/DNS(id=168,qr=0,opcode=0,rd=1,qd=DNSQR(qname=dns_name)),verbose=False)
	#id标识字段（匹配请求与回应），qr等于0标识查询报文，opcode为0表示标准查询，rd为1表示期望递归，qname参数为要查询的域名
	layer = 1
	while True:  #不太确定DNSRR到底有几组
		try:
			if dns_result.getlayer(DNS).fields['an'][layer].fields['type'] == 1:
				dns_result_ip = dns_result.getlayer(DNS).fields['an'][layer].fields['rdata']
				#每一层就是一个记录，但是不一定是A，可能是CNAME
				print ('域名: {0:<18} 对应的IP地址：{1}'.format(dns_name,dns_result_ip))
			layer +=1
		except :#如果超出范围就跳出循环
			break 

while True:
    str = input()
    if str == "":
        print("循环结束！")
        break
    dns_query(str)

# while True:
#     str = input()
#     if str == "":
#         print("循环结束！")
#         break
#     print("您输入的是：" + str)


# 创建 socket 对象
udpSocket = socket(AF_INET, SOCK_DGRAM)
# 本地主机绑定端口
udpSocket.bind(("",8080))
# 主函数
def main():
    while True:
        # 接收信息
        msg,addrInfo = udpSocket.recvfrom(1024)
        # 收到信息后使用 utf-8 解码
        #print("收到来自 %s 的信息：%s"%(addrInfo[0],msg.decode("utf-8")))
if __name__ == '__main__':
    main()