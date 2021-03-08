from perrySummer import perrySummer
from flask import Flask, url_for, request, redirect, abort, jsonify
import datetime as dt
app = Flask(__name__, static_url_path='', static_folder='staticpages')

#**************************************************************************************
#                   USER FUNCTIONS
#**************************************************************************************

# CREATE/GET A USER
# curl -X GET  http://127.0.0.1:5000/users
# curl -X POST -d "{\"name\":\"User One\"}" -H Content-Type:application/json http://127.0.0.1:5000/users
@app.route('/users',methods = ['GET','POST'])
def CreateGetUsers():
    if request.method == 'GET':
        print("user is GET")
        return jsonify(perrySummer.getUsers())
    elif request.method == 'POST':
        print("user is POST")
        user = {
            "name": request.json["name"]
        }
        return jsonify(perrySummer.createUser(user))




#GET UPDATE USER BY ID
#curl -X GET -d "{\"id\":\"d3517764-8045-11eb-80a8-a0a4c514fdba\"}" -H Content-Type:application/json http://127.0.0.1:5000/users/:id
#curl -X PUT -d "{\"name\":\"Updated User One\", \"id\":\"d3517764-8045-11eb-80a8-a0a4c514fdba\"}" -H Content-Type:application/json http://127.0.0.1:5000/users/:id
#curl -X DELETE -d "{\"id\":\"a2607ae8-8051-11eb-90c7-a0a4c514fdba\"}" -H Content-Type:application/json http://127.0.0.1:5000/users/:id
@app.route('/users/:id',methods = ['GET','PUT','DELETE'])
def getUserbyID():
    print("here")
    if request.method == 'GET':
        print("user is")
        id = {
            "id": request.json["id"]
        }
        return jsonify(perrySummer.getUserbyID(id))
    elif request.method == "PUT":
        print("Updated user is")
        id = {
            "id": request.json["id"],
            "name": request.json["name"]
        }
        return jsonify(perrySummer.updateUserbyID(id))
    elif request.method == "DELETE":
        print("Delete user")
        id = {
            "id": request.json["id"]
        }
        return perrySummer.deleteUserID(id)

#**************************************************************************************
#                   Message FUNCTIONS
#**************************************************************************************

#CREATE A MESSAGE
# curl -X POST -d "{\"fromID\":\"d3517764-8045-11eb-80a8-a0a4c514fdba\",\"toID\":\"d3517764-8045-11eb-80a8-a0a4c514fdba\",\"message\":\"Hello User ddddd\"}" -H Content-Type:application/json http://127.0.0.1:5000/message
@app.route('/message',methods = ['POST'])
def CreateMessage():
    if request.method == 'POST':
        print("Messahe is POST")
        message = {
            "fromID": request.json["fromID"],
            "toID": request.json["toID"],
            "message": request.json["message"]
        }
        return jsonify(perrySummer.createMessage(message))

#curl -X GET  http://127.0.0.1:5000/message
@app.route('/message',methods = ['GET'])
def getMessages():
    if request.method == 'GET':
        x = request._get_current_object()
        x= str(x)
        uid =x.replace("' [GET]>","")
        uid = uid.partition("fromID=")[2]
        if uid == "":
            return jsonify(perrySummer.getMessages())
        else:
            return perrySummer.getMessagebyID(uid)
        

#curl -X GET -H Content-Type:application/json http://127.0.0.1:5000/message?fromID=d3517764-8045-11eb-80a8-a0a4c514fdba
#@app.route('/message?fromID=d3517764-8045-11eb-80a8-a0a4c514fdba',methods = ['GET'])
#def getMessage():
 #   print("Mes is GET")
  #  if request.method == 'GET':
   #     print("Mes is GET")
    #    message = {
     #       "fromID": request.json["fromID"],
      #      "toID": request.json["toID"]
       # }
        #print("here")
        #return jsonify(perrySummer.getMessagebyID(message))


#GET UPDATE MESSAGE BY ID
#curl -X GET -d "{\"id\":\"fdc24490-8045-11eb-91ef-a0a4c514fdba\"}" -H Content-Type:application/json http://127.0.0.1:5000/message/:id
#curl -X PUT -d "{\"message\":\"Updated message 333333\", \"id\":\"fdc24490-8045-11eb-91ef-a0a4c514fdba\"}" -H Content-Type:application/json http://127.0.0.1:5000/message/:id
#curl -X DELETE -d "{\"id\":\"fdc24490-8045-11eb-91ef-a0a4c514fdba\"}" -H Content-Type:application/json http://127.0.0.1:5000/message/:id
#@app.route('/message/:id',methods = ['GET','PUT','DELETE'])
@app.route('/message/:id',methods = ['DELETE','GET','PUT'])
def GetUpdateDeleteMessage():
    if request.method == 'GET':
        print("message is")
        id = {
            "id": request.json["id"]
        }
        return jsonify(perrySummer.getMessagebyID(id))
    elif request.method == "PUT":
        print("Updated message is")
        message = {
            "id": request.json["id"],
            "message": request.json["message"]
        }
        return jsonify(perrySummer.updateMessagebyID(message))
    elif request.method == "DELETE":
        print("Delete message")
        id = {
            "id": request.json["id"]
        }
        return perrySummer.deleteMessagebyID(id)
    

if __name__ == "__main__":
    app.run(debug=True)