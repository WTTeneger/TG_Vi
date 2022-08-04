'''
n: u1102095_tgvi
k: utf8mb4
u: u1102095_tgvi
p: nE5pA4aC7w
'''
from cmath import log
import datetime
import pymysql

# Connect to the database
# connection = pymysql.connect(host='37.140.192.90',
#                              user='u1102095_tgvi',
#                              password='nE5pA4aC7w',
#                              database='u1102095_tgvi')
#                             #  cursorclass=pymysql.cursors.DictCursor)

class DB:
    cl = None
    id = 0
    
        
    def __str__(self):
        # print('self', self.id)
        return str(f'id_{self.id}_db_{self.db}')
    

    def __init__(self):
        DB.id += 1
        self.id = DB.id
        if DB.cl == None:
            self.db = pymysql.connect(host='37.140.192.90',
                             user='u1102095_tgvi',
                             password='nE5pA4aC7w',
                             database='u1102095_tgvi',
                             cursorclass=pymysql.cursors.DictCursor)
            DB.cl = self
        else:
            self.db = DB.cl.db

class dbmethods(DB):
    def __init__(self):
        super().__init__()
    
    def create_user(self, tgid, name='', from_user=0):
        print(self.db)
        with self.db.cursor() as cursor:
            try:
                sql = 'INSERT INTO `user` (`tgid`, `name`, `from_user`, `data_reg`, `payabled`) VALUES ({value_1},"{value_2}",{value_3},"{value_4}",{value_5})'\
                      ''.format(value_1 = tgid, value_2=name, value_3=from_user, value_4=datetime.datetime.now(), value_5=False)
                print(sql)
                cursor.execute(sql)
                self.db.commit()
                return True
            except:
                return False
            
            
    def add_ref_for_user(self, tgid):
        with self.db.cursor() as cursor:
            try:
                sql = f"UPDATE `user` SET `count_refferal` = count_refferal+1 WHERE `user`.`tgid` = {tgid};"
                print(sql)
                cursor.execute(sql)
                self.db.commit()
                return True
            except:
                return False
    
    
    def get_all_info(self, tgid):
        with self.db.cursor() as cursor:
            try:
                sql = f"SELECT * FROM `user` WHERE `user`.`tgid` = {tgid};"
                print(sql)
                cursor.execute(sql)
                result = cursor.fetchone()
                # print(result)
                return result
            except:
                return False
    
    
    def set_payabled(self, tgid, sphere = ''):
       with self.db.cursor() as cursor:
            try:
                sql = f"UPDATE `user` SET `count_payable_refferal` = count_payable_refferal+1, `sphere` = '{sphere}' WHERE `user`.`from_user` = {tgid};"
                print(sql)
                cursor.execute(sql)
                self.db.commit()
                sql = f"UPDATE `user` SET `payabled` = '1' WHERE `user`.`tgid` = {tgid};"
                cursor.execute(sql)
                self.db.commit()
                
                return True
            except:
                return False
            
    def set_payable_data(self, tgid, data):
        with self.db.cursor() as cursor:
            try:
                sql = f"UPDATE `user` SET `paymentData` = '{data}' WHERE `user`.`tgid` = {tgid};"
                print(sql)
                cursor.execute(sql)
                self.db.commit()
                return True
            except:
                return False
# c1 = dbmethods()
