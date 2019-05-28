# 导入pymysql
import pymysql
from dnslogs import DnsLogs

import datetime

class DnsLogsDao():
    # 连接MySQL数据库
    def connectDB(self):
        # 输入数据库的IP地址，用户名，密码，端口
        db = pymysql.Connect(host='localhost',
                            port=3306,
                            user='root',
                            passwd='',
                            db='passivedns_db',
                            charset='utf8')
        return db

    # 创建表
    def createTable(self):
        db = self.connectDB()
        # 使用cursor()方法创建一个游标对象
        cursor = db.cursor()
        # 创建一个表
        # sqlStr = 'CREATE TABLE aaa(title varchar(40),amount int,month int,interest float)'
        sqlStr = 'CREATE TABLE dnslogs(id int primary key not null auto_increment , domain varchar(255), domain_ip varchar(40), dns_client_ip varchar(40), dns_server_ip varchar(40), record_time varchar(255))'
        # 使用cursor()方法执行sql语句
        cursor.execute(sqlStr)

    # 插入数据
    def insertData(self, sniffDnsLogs = DnsLogs()):
        db = self.connectDB()
        # 使用cursor()方法创建一个游标对象
        cursor = db.cursor()
        sql = "INSERT INTO dnslogs (domain, domain_ip, dns_client_ip, dns_server_ip, record_time) VALUES ('%s','%s','%s','%s','%s')"
        # data = ('www.zzzzzzaaaaa.com', '10.250.17.23', '121.250.17.113', '121.250.17.23', '1.223')
        data = (sniffDnsLogs.domain, sniffDnsLogs.domain_ip, sniffDnsLogs.dns_client_ip, sniffDnsLogs.dns_server_ip, sniffDnsLogs.record_time)
        cursor.execute(sql % data)
        db.commit()
        print('成功插入', cursor.rowcount, '条数据')
    
    # 数据查重
    def checkingData(self, sniffDnsLogs = DnsLogs()):
        isRepeat = False
        db = self.connectDB()
        # 使用cursor()方法创建一个游标对象
        cursor = db.cursor()
        sql = "SELECT dnslogs.id FROM dnslogs WHERE dnslogs.domain = '%s' AND dnslogs.domain_ip = '%s' AND dnslogs.dns_server_ip = '%s'"
        data = (sniffDnsLogs.domain, sniffDnsLogs.domain_ip, sniffDnsLogs.dns_server_ip)
        cursor.execute(sql % data)
        db.commit()       
        try:
            # 如果查询结果返回正常，说明存在相同DNS记录，则执行更新相应记录即可
            repeatDataID = cursor.fetchall()[0][0]
            print('存在重复的记录，数据ID:', repeatDataID,'，执行更新操作……')
            self.updateData(sniffDnsLogs, repeatDataID)
        except IndexError as identifier:
            # 如果查询结果返回异常，说明未找到相同DNS记录，则执行插入数据
            self.insertData(sniffDnsLogs)
        
    # 更新数据
    def updateData(self, sniffDnsLogs = DnsLogs(), repeatDataID = 0):
        print(sniffDnsLogs.dns_client_ip, sniffDnsLogs.dns_server_ip, sniffDnsLogs.record_time, repeatDataID)
        db = self.connectDB()
        # 使用cursor()方法创建一个游标对象
        cursor = db.cursor()
        sql = "UPDATE dnslogs SET dns_client_ip = '%s', record_time = '%s' WHERE id = %d"
        data = (sniffDnsLogs.dns_client_ip, sniffDnsLogs.record_time, repeatDataID)
        cursor.execute(sql % data)
        db.commit()
        print('成功更新ID为', repeatDataID, '数据记录')
    
    def sayHello(self):
        print("##########test############ hello zadaya~! #############test#############")

# TestDnsLogsDao = DnsLogsDao()
# TestDnsLogs = DnsLogs()
# TestDnsLogs.domain = '0123'
# TestDnsLogs.domain_ip = '3210'
# TestDnsLogs.dns_client_ip = 'zay'
# TestDnsLogs.dns_server_ip = 'zadaya'
# TestDnsLogs.record_time = datetime.datetime.now()

# TestDnsLogsDao.checkingData(TestDnsLogs)