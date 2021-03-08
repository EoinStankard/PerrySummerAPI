# PerrySummerAPI
Imagine we are making a private messaging service for our new company Perry’s Summer Vacation Goods and Services. We need you to create an automated test script that verifies the Message API, not User API.

### Requirements of Perry’s Summer Vacation Goods and Services.
**Develop a scalable API to be able to handle the many messages this company is going to handle**

- The application should be a REST API (No need for any kind of UI)

- The application should be ready to run in the cloud or in a container.

- The application data must be persisted in a database of some type.

- The application must be able to create and get users.

- We do not expect you do handle any kind of authentication for users.
  - The application must allow users to send a message to one other user.

- No need to consider group chats.
  - The application must allow editing and deleting messages.

- The application must be able to get all the messages sent between two users.

### How to Run the Api

Please clone the full directory.

This API is run on the local machine and not in the cloud

1. Configure your SQL database username and password in "dbconfig.py"
2. To create SQL table run "python createDatabase.py"
3. To run the API run "python messageAPI.py"
4. API will probably run on http://127.0.0.1:5000/

### POSTMAN Testing

As i have no previous knowledge of postman i was not familiar with how testing was done on this environment,
I was able to Create a user/message and List users/Messages

Shared https://www.getpostman.com/collections/8faf1d34cc93292bf8e6

For all the other commands, the CRUD command would work fine on the command line but would not work on POSTMAN. I was unable to figure out the problem


### CRUD Commands
#### USER EXAMPLES

**Create user**
1. Through postman
2. curl -X POST -d "{\"name\":\"User One\"}" -H Content-Type:application/json http://127.0.0.1:5000/users

**Get User**
1. Through Postman
2. curl -X GET  http://127.0.0.1:5000/users

**Get User By ID**
1. curl -X GET -d "{\"id\":\"d3517764-8045-11eb-80a8-a0a4c514fdba\"}" -H Content-Type:application/json http://127.0.0.1:5000/users/:id

**Update User by ID**
1. curl -X PUT -d "{\"name\":\"Updated User One\", \"id\":\"d3517764-8045-11eb-80a8-a0a4c514fdba\"}" -H Content-Type:application/json http://127.0.0.1:5000/users/:id

**Delete User by ID**
1. curl -X DELETE -d "{\"id\":\"a2607ae8-8051-11eb-90c7-a0a4c514fdba\"}" -H Content-Type:application/json http://127.0.0.1:5000/users/:id


#### MESSAGE EXAMPLES

**Create Message**
1. Through Postman
2. curl -X POST -d "{\"fromID\":\"d3517764-8045-11eb-80a8-a0a4c514fdba\",\"toID\":\"d3517764-8045-11eb-80a8-a0a4c514fdba\",\"message\":\"Hello User ddddd\"}" -H Content-Type:application/json http://127.0.0.1:5000/message

**Get Messages**
1. Through Postman
2. curl -X GET  http://127.0.0.1:5000/message

**Get message by Message ID**
1. curl -X GET -d "{\"id\":\"fdc24490-8045-11eb-91ef-a0a4c514fdba\"}" -H Content-Type:application/json http://127.0.0.1:5000/message/:id

**Update Message By Message ID**
1. curl -X PUT -d "{\"message\":\"Updated message 333333\", \"id\":\"fdc24490-8045-11eb-91ef-a0a4c514fdba\"}" -H Content-Type:application/json http://127.0.0.1:5000/message/:id

**Delete Message by Message ID**
1. curl -X DELETE -d "{\"id\":\"fdc24490-8045-11eb-91ef-a0a4c514fdba\"}" -H Content-Type:application/json http://127.0.0.1:5000/message/:id

**Get Messages between two users**

Could not get this part as i was unable to understand how the query was parsed




