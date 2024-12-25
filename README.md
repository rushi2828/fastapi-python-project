Install Mysql server
Install Mysql workbench

Commad for run this project:
$ uvicorn main:app --reload

Postman url to create user 
POST http://127.0.0.1:8000/items

Request body:
{
    "name": "first",
    "description": "This is first description"
}

To view user 
GET http://127.0.0.1:8000/items/1

