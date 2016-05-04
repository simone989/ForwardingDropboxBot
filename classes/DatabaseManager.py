import MySQLdb

class DatabaseManager(object):
    def __init__(self):
        self.db=MySQLdb.connect("localhost","root","1404","ForwardingDropboxBot")
        self.cursor=self.db.cursor()

    def tokenNotUsed(self,token):
        sql="SELECT Id FROM Utenti WHERE Token='"+token+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        if(result):
            return False
        else:
            return True




data=DatabaseManager()


#sql="INSERT INTO Utenti(Username,ChatId,Token) VALUES ('test',753537,'febfyefbeubfubfejd')"

try:
    test=data.tokenNotUsed("febfyefbeubfubfejd11")

    print(test)
except Exception as error:
    print (error)
