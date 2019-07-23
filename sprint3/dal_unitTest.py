#DAL Unit Test
from datalogic import DataLogic
import sqlite3
#Database Test
dl = DataLogic()
connection = sqlite3.connect("accounts.db")
cursor = connection.cursor()
connection.row_factory = sqlite3.Row

cursor.execute("SELECT * FROM accounts")
rows = cursor.fetchall()

#Test Unique Key
check_1 = False
for row in rows:
    try:
        dl.insertData(row[1],row[2],row[3])
        check_1 = False
    except:        
        check_1 = True        
        continue
        
if check_1 is True:
    print("unique key is ok")
else:
    print("unique key is not ok")

#Test isUserExist
for row in rows:
    check_2 = dl.isUserExist(row[1])
if check_2 is True:
    check_2 = dl.isUserExist(0)
    if check_2 is False:
        print("isUserExist ok")
    else:
        print("isUser not ok")
else:
    print("isUserExit not ok")

#Test isMatch 
for row in rows:
    check_3 = dl.isMatch(row[1])
    
if check_3 is False:
    print("isMatch not ok")
else:
    for row in rows:
        check_3 = dl.isMatch(0)
    if check_3 is True:
        print("isMatch not ok")
    else:
        print("isMatch ok")

#Test insertData
num = []
check_4 = False
for i in range (10):
    un = "sebsebsebsebsebseb" + str(i)
    pw = "besbesbesbesbesbes"  + str(i)
    fn = "esbesbesbesbesbesb"  + str(i)
    try:
        dl.insertData(un,pw,fn)
        connection.commit()
    except:
        continue
    check_4 = dl.isUserExist(un)
    if check_4 is True:
        cursor.execute("DELETE FROM accounts WHERE USERNAME =?",(un,))
        connection.commit()
    else:
        check_4 = False
        
if check_4 is True:
    print("insertData is ok")
else:
    print("insertData is not ok")
    
connection.close()
