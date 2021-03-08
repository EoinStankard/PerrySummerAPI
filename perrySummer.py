import mysql.connector
import dbconfig as cfg
from mysql.connector import cursor
import datetime as dt
import uuid

class perrySummer:
    db = ""
    #Connect to DB
    def connectToDB(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user= cfg.mysql['username'],
            password = cfg.mysql['password'],
            database =cfg.mysql['database']
        )

    # Make connection
    def __init__(self):
        self.connectToDB()

    #Make sure connection is alive
    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()
    #**************************************************************************************
    #                   USER FUNCTIONS
    #**************************************************************************************
    def createUser(self,user):
        cursor = self.getCursor()
        sql = "insert into user (name,id) values (%s,%s)"
        id = uuid.uuid1()
        values = [
            user['name'],
            str(id)
        ]
        cursor.execute(sql,values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid

    def getUsers(self):
        cursor = self.getCursor()
        sql = 'select * from user'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToUserDict(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray

    def getUserbyID(self, user):
        cursor = self.getCursor()
        print("GET USER BY ID")
        sql = 'select * from user where id = "%s"'
        values = [ user['id'] ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToUserDict(result)

    def getUserID(self, user):
        cursor = self.getCursor()
        sql = 'select * from user where id = %s'
        values = [ user ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToIDDict(result)

    def updateUserbyID(self, user):
        cursor = self.getCursor()
        sql = "update user set name = %s where id = %s"
        values = [
            user['name'],
            user['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return user

    def deleteUserID(self,user):
        cursor = self.getCursor()
        print("DELTER user id is",user)
        sql = "delete from user where id= %s"
        values = [
           user['id']
        ]
        cursor.execute(sql,values)
        self.db.commit()
        cursor.close()
        return user

    def convertToUserDict(self, result):
        colnames = ['name','id']
        user = {}
        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                user[colName] = value
        return user

    #**************************************************************************************
    #                   Message FUNCTIONS
    #**************************************************************************************
    def createMessage(self,message):
        print("message recieved")
        cursor = self.getCursor()
        sql = "insert into message (fromID,toID,message,time,id) values (%s,%s,%s,%s,%s)"
        time = dt.datetime.now()
        id = uuid.uuid1()
        values = [
            message['fromID'],
            message['toID'],
            message['message'],
            time,
            str(id)
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid


    def getMessages(self):
        print("get message")
        cursor = self.getCursor()
        sql = 'select * from message inner join user u where fromID =u.id;'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToMessageDict(result)
            resultAsDict['fromID']= self.getUserID(resultAsDict['fromID'])
            resultAsDict['toID']= self.getUserID(resultAsDict['toID'])
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray

    def getMessagebyID(self, message):
        cursor = self.getCursor()
        sql = 'select * from message where ID = %s'
        values = [ message['id'] ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        print("result",result)
        cursor.close()
        return self.convertToMessageDict(result)

    def updateMessagebyID(self, message):
        cursor = self.getCursor()
        sql = "update message set message = %s where id = %s"
        values = [
            message['message'],
            message['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return message

    def deleteMessagebyID(self, message):
        cursor = self.getCursor()
        sql = "delete from message where id= %s"
        values = [
            message['id']
        ]
        cursor.execute(sql,values)
        self.db.commit()
        cursor.close()
        return message

    def convertToMessageDict(self, result):
        colnames = ['fromID','toID','message','id','time']
        user = {}
        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                user[colName] = value
        return user

    def convertToIDDict(self, result):
        colnames = ['id']
        user = {}
        if result:
            for i , colName in enumerate(colnames):
                value = result[i+1]
                user[colName] = value
        return user

perrySummer = perrySummer()