# python-to-webAPI
Call WebAPI from Python code and perform CRUD operations

Prerequisites :
1.Install Requests and SimpleJson Packages
2.Run the WebApi  Rest service with CRUD operations locally or deploy in IIS

Steps to follow to connect to WebAPI
Install python and follow the below steps :
1.Add Path in environment variables : example-add c:\python34;c:\python34\scripts

The above are the python installed paths python34-version

neccessary paths: c:\python34;c:\python34\scripts

2.Install  SimpleJson Package

3.Place Request Packages in Lib/SitePackages folder(check Requests folder)

4.Deploy WebAPI(.net) Rest service with CRUD operations in IIS or run it locally(use the ActionMethod name as path in python code to connect to service)

5.Run the database scripts in SQLServer(WebAPICRUD.zip-->ReadMe.txt) 

Finally run the RestServiceUsingWebApi.py python  file to perform CRUD operations from python using WebApi






