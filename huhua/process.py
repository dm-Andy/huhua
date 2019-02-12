import redis
import pymysql
from const import *
import json

class Processor:
    def __init__(self):
        # decode_responses=True 写入的键值对中的value为str类型，不加这个参数写入的则为字节类型。
        self.redis_cli = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        self.conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB, port=MYSQL_PORT)
        self.cursor = self.conn.cursor()
    
    def run(self):
        pass
        # 把分类信息写入到数据库
        # self.process_classification()
        
        # 把分类所有数据写入到数据库
        # self.process_classification_all()

        # 把类别信息写入数据库，子分类用sql语句处理
        # self.process_category()
        # update category set parent_id=1 where name in ('一年生草本花卉','二年生草本花卉','多年生草本花卉')
        # update category set parent_id=2 where name in ('乔木花卉','灌木花卉','藤本花卉')
        # update category set parent_id=3 where name in ('球茎花卉','鳞茎花卉','块茎花卉','根茎花卉','块根花卉')
        

        # self.process_flowers()

    def process_classification(self):
        sql = 'insert into classification (name,value) values '
        while True:
            data = self.redis_cli.lpop(CLASSIFICATION_KEY)
            if not data:
                break
            data = json.loads(data)
            print(data['name'])
            sql += '("%s","%s"),' % (data['name'], data['value'])
            
        if sql.endswith(','):
            sql = sql.rstrip(',')

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print('process_classification success')
        except Exception as ex:
            self.conn.rollback()

    def process_classification_all(self):
        sql = 'insert into classification_all (classification,name) values '
        num = 0
        while True:
            data = self.redis_cli.lpop(CLASSIFICATION_ALL_KEY)
            num += 1
            if not data:
                break
            data = json.loads(data)
            sql += '("%s","%s"),' % (data['classification'], data['name'])
            if num >= 100:
                print(num)
                sql = sql.rstrip(',')
                self.cursor.execute(sql)
                num = 0
                sql = 'insert into classification_all (classification,name) values '
            
        if sql.endswith(','):
            sql = sql.rstrip(',')

        try:
            print(num)
            self.cursor.execute(sql)
            self.conn.commit()
            print('process_classification_all success')
        except Exception as ex:
            self.conn.rollback()

    def process_category(self):
        sql = 'insert into category (name) values '
        while True:
            data = self.redis_cli.lpop(CATEGORY_KEY)
            if not data:
                break
            data = json.loads(data)
            sql += '("%s"),' % data['name']
            print(data['name'])
            
        if sql.endswith(','):
            sql = sql.rstrip(',')

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print('process_category success')
        except Exception as ex:
            self.conn.rollback()
        
    def process_flowers(self): 
        query = 'select id,name from category'
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        dic = {}
        for x in rows:
            id = x[0]
            name = x[1]
            dic[name] = id

        while True:
            sql = 'insert into flowers (name,en_name,alias,keshu,shenghuaqi,category_id) values '
            data = self.redis_cli.lpop(FLOWERS_DETAIL_KEY)
            if not data:
                print('process_flowers success')
                break
            data = json.loads(data)
            print(data['name'])

            sql += '("%s","%s","%s","%s","%s",%d)' % (data['name'], pymysql.escape_string(data['en_name']), data['alias'], data['keshu'], data['shenghuaqi'], dic[data['category']])

            try:
                self.cursor.execute(sql)
                # 获取插入的id
                last_id = self.cursor.lastrowid
                
                # 花卉图片，节省性能，用sql修改图片链接
                # update flowers_pic set path=replace(path,'_140_120','')
                sql_img = 'insert into flowers_pic (flower_id,path) values (%d,"%s")' % (last_id, data['pic'])
                self.cursor.execute(sql_img)

                # 花卉扩展表
                sql_ext = 'insert into flowers_extension (flower_id,name,value) values '
                for x in data['dic']:
                    sql_ext += '(%d,"%s","%s"),' % (last_id, x['name'], pymysql.escape_string(x['val']))

                if sql_ext.endswith(','):
                    sql_ext = sql_ext.rstrip(',')

                self.cursor.execute(sql_ext)
                self.conn.commit()
            except Exception as ex:
                print('process_flowers error:\n%s\n%s' % ( data['name'],ex))
                self.conn.rollback()
      

if __name__ == '__main__':
    processor = Processor()
    processor.run()