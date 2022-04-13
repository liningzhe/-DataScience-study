# -*- codeing= utf-8 -*-
# Author：Nina
# Time:2021/9/4 17:34
# file:excel.py

from xlrd import open_workbook
import sqlite3
import types


def read_excel(sheet):
    # 判断有效sheet
    if sheet.nrows > 0 and sheet.ncols > 0:
        for row in range(1, sheet.nrows):
            row_data = []
            for col in range(sheet.ncols):
                data = sheet.cell(row, col).value
                # if type(data) is types.FloatType:
                #     data = int(data)
                # elif type(data) is types.UnicodeType:
                #     data = data.encode("utf-8")
                #
                # excel表格内容数据类型转换  float->int，unicode->utf-8

                row_data.append(data)
            check_data_length(row_data)


# 检查row_data长度
def check_data_length(row_data):
    if len(row_data) == 1469:
        insert_sqlite(row_data)


def insert_sqlite(row_data):
    # 打开数据库（不存在时会创建数据库）
    con = sqlite3.connect("dingzhen.db")
    cur = con.cursor()
    try:
        cur.execute('''create table if not exists contacts
                    (ID integer primary key autoincrement,
                    Post-title text,
                    time integer,
                    Replay integer);''')

        # #插入数据不要使用拼接字符串的方式，容易收到sql注入攻击;
        cur.execute('''insert into contacts(ID,Post-title,time,Replay) values(?,?,?,?)''',row_data)
        con.commit()
    except sqlite3.Error as e:
        print("An error occurred: %s", e.args[0])
    finally:
        cur.close()
        con.close()

xls_file = "Dingzhen.xls"
book = open_workbook(xls_file)

for sheet in book.sheets():
    read_excel(sheet)
print("------ Done ------")