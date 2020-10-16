import pymysql
import datetime
#https://pypi.org/project/PyMySQL/
class MysqlDBHelper():


    def getConnecttion(self):
        # Connect to the database
        connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='my753721',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        return connection

    def init_db(self):
        sql1_0 = 'DROP TABLE IF EXISTS demo_department'
        sql1_1 = '''CREATE TABLE IF NOT EXISTS demo_department (
                id INTEGER NOT NULL, 
                name VARCHAR(30), 
                create_date DATETIME NULL DEFAULT NOW(), 
                PRIMARY KEY (id)
                );
              '''
        #列信息
        #cur.execute('select * from demo_department')
        #col_name_list = [tuple[0] for tuple in cur.description]
        sql1_2 = "INSERT INTO demo_department (id, name, create_date) VALUES (%s, %s, %s);"
        
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        sql1_data =[(1,	'IT',dt),(2,'Financial',dt),(3,'Market',dt)]

        sql2_0 = 'DROP TABLE IF EXISTS demo_employee'
        sql2_1 = '''
                CREATE TABLE demo_employee (
                    `id` INT NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(30) NULL,
                    `sex` INT NULL,
                    `department_id` INT NULL,
                    `hired_on` DATE NULL,
                    `create_date` DATETIME NULL DEFAULT NOW(),
                    `height` DECIMAL NULL,
                    `remark` VARCHAR(100) NULL,
                    PRIMARY KEY (id)
                );
                '''
        dt = datetime.datetime.now().strftime("%Y-%m-%d")
        sql2_2 = 'INSERT INTO demo_employee (id, name, hired_on, department_id) VALUES (%s, %s, %s, %s);'
        sql2_data =[(1,'John',dt,1),(2,'Mike',dt,1),(3,'Tom',dt,1), (4,'Susan',dt,1),(5,'Wanglin',dt,1),(6,'Simon',dt,1),
                    (7,'Cathy',dt,2),(8,'Marry',dt,2),(9,'Jack',dt,2),(10,'Jame',dt,2),(11,'Shirley',dt,2),(12,'Anne',dt,2),
                    (13,'Billy',dt,3),
                    (14,'Eric',dt,3),
                    (15,'Alan',dt,3),
                    (16,'张大山',dt,3),
                    (17,'陈永生',dt,3),
                    (18,'朱国庆',dt,3),
                    (19,'Mike',dt,4)
                    ]
        connection = self.getConnecttion()
        try:
            with connection.cursor() as cur:
                cur.execute(sql1_0)
                cur.execute(sql1_1)
                rows_affected =cur.executemany(sql1_2,sql1_data)
                print(f'The query affected {cur.rowcount} rows')
                cur.execute(sql2_0)
                cur.execute(sql2_1)
                rows_affected =cur.executemany(sql2_2,sql2_data)
                print(f'The query affected {cur.rowcount} rows')
                connection.commit()

        except Exception as err:
            print(err)
        finally:
            connection.close()
  



if __name__ == '__main__':
    db = MysqlDBHelper()
    db.init_db()
 