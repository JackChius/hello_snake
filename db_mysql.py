#! /usr/bin/env python3
# import csv
import MySQLdb
import sys
# from datetime import datetime,date

con = MySQLdb.connect(host='localhost',port=3306,db='my_suppliers',\
user='root',passwd='root')
c = con.cursor() 
c.execute("""insert into Suppliers values (%s,%s,%s,%s,%s);""",['haha_input','fun','990','1510.0','2008/02/18'])
con.commit()
print('success to insert db')
c.execute("select * from Suppliers")
rows = c.fetchall()
for row in rows:
    row_list = []
    for col_index in range(len(row)):
        row_list.append(str(row[col_index]))
    print(row_list)
print('success to check for db')

