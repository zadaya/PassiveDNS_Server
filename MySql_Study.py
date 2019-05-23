# 导入pymysql
import pymysql

# 连接MySQL数据库
def connectDB():
    # 输入数据库的IP地址，用户名，密码，端口
    db = pymysql.Connect(host='localhost',
                        port=3306,
                        user='root',
                        passwd='',
                        db='111',
                        charset='utf8')
    return db

# 创建表
def createTable():
    # 创建一个表
    sqll = 'CREATE TABLE aaa(title varchar(40),amount int,month int,interest float)'
    sqll = 'CREATE TABLE testTable(title varchar(40),amount int,month int,interest float)'
    # 使用cursor()方法执行sql语句
    cursor.execute(sqll)


sql = "INSERT INTO dnslogs (domain, domain_ip, dns_client_ip, dns_server_ip, record_time) VALUES ('%s','%s','%s','%s','%s')"
data = ('www.zadaya.com', '10.250.17.23', '121.250.17.113', '121.250.17.23', '1.223')

db = connectDB()
# 使用cursor()方法创建一个游标对象
cursor = db.cursor()
cursor.execute(sql % data)
db.commit()
print('成功插入', cursor.rowcount, '条数据')
