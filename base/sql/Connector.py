import pymysql

# 获取数据库连接
db = pymysql.Connect(
    host='rm-8vbz6r721g3qy9enpio.mysql.zhangbei.rds.aliyuncs.com',
    port=3306,
    user='king',
    passwd='$king123',
    db='ant_build',
    charset='utf8mb4'
)


# 执行sql语句
def execute(sql, data):
    # noinspection PyBroadException
    try:
        # 获取游标
        cursor = db.cursor()
        # 执行sql语句
        cursor.execute(sql, data)
        # 提交到数据库执行
        db.commit()
    except BaseException:
        # 如果发生错误回滚
        db.rollback()
    db.close()
    print('成功执行', cursor.rowcount, '条数据')
