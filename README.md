# Dathena REST 

## Installation steps
```
$mkdir dathena
$cd dathena
$python3 -m venv env
$source env/bin/activate
$pip3 install -r requirements.txt
```

## User Registration
http://127.0.0.1:8000/auth/register/
Using Postman, enter the following key-value fields:
username : <insert your username>
email : <insert your email>
password : <insert your password>
*password is encrypted
return : status 201 and your username and email


## Token Authentication
Open http://127.0.0.1:8000/api/token/ in browser
Use my crendentials or yours if you prefer
Username : richard
Password : Learning1
get access token
![alt text](https://github.com/savvyguru/dathena/blob/master/media/Screenshot%202020-08-06%20at%2010.04.06%20AM.png)

## Upload File
http://127.0.0.1:8000/upload/
Meta information of file is stored in custom model File_Meta
Using Postman, enter the following key-value fields:
file : <insert your file.txt>
*file type must be.txt else return : status 400 bad request
Authorization:
Type = Bearer Token
Insert you JWT token
return : status 201 and your file information
![alt text](https://github.com/savvyguru/dathena/blob/master/media/Screenshot%202020-08-06%20at%2010.06.10%20AM.png)
  
## List Files
http://127.0.0.1:8000/listfile/
Authorization:
Type = Bearer Token
Insert you JWT token
return : status 201 and list of database in serialized form
![alt text](https://github.com/savvyguru/dathena/blob/master/media/Screenshot%202020-08-06%20at%2010.05.10%20AM.png)

# Celery Application
```
$cd /usr/local/sbin
$brew services stop rabbitmq
$brew services start rabbitmq
```
Go to : http://localhost:15672/#/
Login details: guest:guest
cd back to your django directory and start celery:
```
$celery -A quickstart worker -B -Q celery -l info
```
Celery worker runs every periodically (every 5 seconds) and updates the sensitivity score of the files 
![alt text](https://github.com/savvyguru/dathena/blob/master/media/Screenshot%202020-08-06%20at%209.49.19%20AM.png)
![alt text](https://github.com/savvyguru/dathena/blob/master/media/Screenshot%202020-08-06%20at%209.50.05%20AM.png)

