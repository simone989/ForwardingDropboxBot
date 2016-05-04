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
    def userNotAreToken(self,Username):
        sql="SELECT * FROM Utenti WHERE Username='"+Username+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        if(result):
            return False
        else:
            return True
    def chatidNotUsed(self,ChatId):
        sql="SELECT * FROM Utenti WHERE ChatId= "+str(ChatId)
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        if(result):
            return False
        else:
            return True
    def updateToken(self,Username,Token):
        if(self.tokenNotUsed(Token)):
            sql="UPDATE Utenti SET Token='"+Token+"'WHERE Username='"+Username+"'"
            result=self.cursor.execute(sql)
            self.db.commit()
            if(result):
                return True
            else:
                return False
        else:
            return False

    def insertNewUser(self,Username,ChatId,Token):
        if(self.tokenNotUsed(Token) and self.userNotAreToken(Username) and self.chatidNotUsed(ChatId)):
            sql="INSERT INTO Utenti(Username,ChatId,Token) VALUES ('"+Username+"',"+str(ChatId)+",'"+Token+"')"
            result=self.cursor.execute(sql)
            self.db.commit()
            if(result):
                return True
            else:
                return False
        else:
            return False
    def dropWitchUser(self,UserName):
        sql="DELETE FROM Utenti Where Username='"+UserName+"'"
        result=self.cursor.execute(sql)
        self.db.commit()
        if(result):
            return True
        else:
            return False
    def dropWitchChatId(self,ChatId):
        sql="DELETE FROM Utenti Where ChatId= "+str(ChatId)
        result=self.cursor.execute(sql)
        self.db.commit()
        if(result):
            return True
        else:
            return False
    def dropWitchToken(self,Token):
        sql="DELETE FROM Utenti Where Token='"+Token+"'"
        result=self.cursor.execute(sql)
        self.db.commit()
        if(result):
            return True
        else:
            return False
    def getTokenWitchUsername(self,Username):
        sql="SELECT Token FROM Utenti WHERE Username ='"+Username+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        for row in result:
            TokenDB= row[0]
            if(TokenDB):
                return TokenDB
            else:
                return False
    def getTokenWitchChatId(self,ChatId):
        sql="SELECT Token FROM Utenti WHERE ChatId ="+str(ChatId)
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        for row in result:
            TokenDB= row[0]
            if(TokenDB):
                return TokenDB
            else:
                return False
    def getUsernameWitchToken(self,Token):
        sql="SELECT Username FROM Utenti WHERE Token ='"+Token+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        for row in result:
            UsernameDB= row[0]
            if(UsernameDB):
                return UsernameDB
            else:
                return False
    def getUsernameWitchChatId(self,ChatId):
        sql="SELECT Username FROM Utenti WHERE ChatId ="+str(ChatId)
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        for row in result:
            UsernameDB= row[0]
            if(UsernameDB):
                return UsernameDB
            else:
                return False
                #AGGIUNGERE IL GETCHAID CON IL TOKEN E USERNAME
    def getChatIdWitchToken(self,Token):
        sql="SELECT ChatId  FROM Utenti WHERE Token ='"+Token+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        for row in result:
            ChatIdDB= row[0]
            if(ChatIdDB):
                return ChatIdDB
            else:
                return False
    def getChatIdWitchUsername(self,Username):
        sql="SELECT ChatId FROM Utenti WHERE ChatId ='"+Username+"'"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        for row in result:
            ChatIdDB= row[0]
            if(ChatIdDB):
                return ChatIdDB
            else:
                return False



"""
    test=data.tokenNotUsed("febfyefbeubfubfejd11")
    test=data.userNotAreToken("test")
    test=data.updateToken("test","fbeuffbfefen")
    test=data.chatidNotUsed(7535337)
    test=data.insertNewUser("ciao2",74537,"efufenudbeud")
    test=data.dropWitchToken("efufenudbeud")
"""



data=DatabaseManager()


#sql="INSERT INTO Utenti(Username,ChatId,Token) VALUES ('test',753537,'febfyefbeubfubfejd')"

try:

    test=data.getTokenWitchChatId(753537)
    print(test)
except Exception as error:
    print (error)
