kyndryl-assignment
------------------
Rest-API system – Home assignment
The goal of this exercise is to check basic knowledge with ORM, Rest-API and DB, and see what you consider production-level code.
Pretend that you got the following request from a client:
We need you to design and implement a system to manage our employees. It should have a Rest-API server that gets 3 values: first name, last name and ID number. The server stores the values in a DB. The ID needs to be numeric. The first name and last name need to contain only letters, and start with an upper-case letter.
In addition, implement an app (command-line or web) for adding new records, and showing a list of the existing records.
Please use flask (or Django) for your solution. Make sure to supply us with all the info required to run and test the code (virtual env in case of python, docker is optional….)


Solution:
---------
There are 5 files in this project:
INDEX.HTMLl is the UI - you can add an Employee First and Last name, the numric ID is added automatically.
SERVER.PYy is the backend code that calls the API.PY
The API connects to the database via the mongo_connetion.py
The backend database used is MongoDB with 2 main tables, EMPLOYEE and SUPPORT
  EMPLOYEE holds the data
  SUPPORT holds the latest employee id as an int, and is growing by 1 each new addition of an Emplyee
  
 CONFIG.INI holds global static data
 VALIDATION.PY holds the validation logic needed for the input
  
