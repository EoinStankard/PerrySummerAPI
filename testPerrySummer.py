from perrySummer import perrySummer
import datetime as dt

name1 = {
    'name': "Joe Bloggs"
}

name2 = {
    'name': "Joe Bloggs",
    'id':"3"
}

name3 = {
    'name': "Jane Doe"
}

message1 = {
    "fromID":1,
    "toID":3,
    "message":"Hello from 1 to 3",
    "time":dt.datetime
}

message2 = {
    "fromID":3,
    "toID":1,
    "message":"Hello from 3 to 1",
    "time":dt.datetime
}

message3 = {
    "fromID":3,
    "toID":1,
    "id":5,
    "message":"I am updated",
    "time":dt.datetime
}

#returnvalue = perrySummer.createUser(name3)
#returnvalue = perrySummer.getUsers()
#returnvalue = perrySummer.getUserID(name2)
#returnvalue = perrySummer.updateUserbyID(name2)
#returnvalue = perrySummer.deleteUserbyID(name2)

#returnvalue = perrySummer.createMessage(message1)
returnvalue = perrySummer.createMessage(message2)
#returnvalue = perrySummer.getMessages()
#returnvalue = perrySummer.getMessagebyID(5)
#returnvalue = perrySummer.updateMessagebyID(message3)
#returnvalue = perrySummer.deleteUserbyID(message3)
print(returnvalue)