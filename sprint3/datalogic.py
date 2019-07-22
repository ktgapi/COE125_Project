import sqlite3

class DataLogic:
    def __init__(self):
        self.connection = sqlite3.connect("accounts.db")
        self.cursor = self.connection.cursor()
        self.connection.row_factory = sqlite3.Row
        #self.userTemp = None
        self.userTemp = None

    def isUserExist(self,user):
        self.cursor.execute("SELECT * FROM accounts ")
        rows = self.cursor.fetchall()
        for row in rows:
            if (str(row[1]) == user):
                self.userTemp = row[1]
                self.connection.commit()
                return True
        self.connection.commit()
        return False
    def isMatch(self, pw):
        self.cursor.execute("SELECT * FROM accounts ")
        rows = self.cursor.fetchall()
        #mess = "Incorrect Password"
        for row in rows:
            if (str(row[1]) == self.userTemp):
                if(str(row[2]) == pw):
                    self.connection.commit()
                    return str(row[3])
                else:
                    self.connection.commit()
                    return ""
                    #return mess
    def insertData(self,user,pw,fn):
        self.cursor.execute('Insert INTO accounts(USERNAME,PASSWORD,FULLNAME) VALUES(?,?,?)',(user,pw,fn))
        self.connection.commit()