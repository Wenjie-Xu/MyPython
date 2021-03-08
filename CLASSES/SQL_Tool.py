import pymysql

class SQL_Tool:
    # TODO 创建连接和游标
    def __init__(self, host, port, db, user, passwd, charset='utf8'):
        self.connect = pymysql.connect(host=host, port=port, db=db,
                                       user=user, passwd=passwd, charset=charset)
        # TODO 设置cursor的属性，可以是结果集以字典形式呈现 (cursor=pymysql.cursors.DictCursor)
        self.cursor = self.connect.cursor()

    # TODO 关闭连接和游标
    def __del__(self):
        self.cursor.close()
        self.connect.close()