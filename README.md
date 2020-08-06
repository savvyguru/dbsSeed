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
http://127.0.0.1:8000/auth/register/ <br/>
Using Postman, enter the following key-value fields: <br/>
username : <insert your username> <br/>
email : <insert your email> <br/>
password : <insert your password> <br/>
*password is encrypted <br/>
return : status 201 and your username and email <br/>


## Token Authentication
Open http://127.0.0.1:8000/api/token/ in browser <br/>
Use my crendentials or yours if you prefer <br/>
Username : richard <br/>
Password : Learning1 <br/>
get access token <br/>
![alt text](https://github.com/savvyguru/dathena/blob/master/media/Screenshot%202020-08-06%20at%2010.04.06%20AM.png)

## Upload File
http://127.0.0.1:8000/upload/ <br/>
Meta information of file is stored in custom model File_Meta <br/>
Using Postman, enter the following key-value fields: <br/>
file : next_client.txt <insert your file.txt> <br/>
*file type must be.txt else return : status 400 bad request <br/>
Authorization: <br/>
Type = Bearer Token <br/>
Insert you JWT token <br/>
return : status 201 and your file information <br/>
Take note that the sensitivity score is null when you first upload <br/>
![alt text](https://github.com/savvyguru/dathena/blob/master/media/Screenshot%202020-08-06%20at%2010.17.24%20AM.png)
![alt text](https://github.com/savvyguru/dathena/blob/master/media/Screenshot%202020-08-06%20at%2010.18.42%20AM.png)

  
## List Files
http://127.0.0.1:8000/listfile/
Authorization: <br/>
Type = Bearer Token <br/>
Insert you JWT token <br/>
return : status 201 and list of database in serialized form <br/>
![alt text](https://github.com/savvyguru/dathena/blob/master/media/Screenshot%202020-08-06%20at%2010.05.10%20AM.png)

# Celery Application
```
$cd /usr/local/sbin
$brew services stop rabbitmq
$brew services start rabbitmq
```
Go to : http://localhost:15672/#/ <br/>
Login details: guest:guest <br/>
cd back to your django directory and start celery: <br/>
```
$celery -A quickstart worker -B -Q celery -l info
```
Celery worker runs every periodically (every 5 seconds) and updates the sensitivity score of the files 
![alt text](https://github.com/savvyguru/dathena/blob/master/media/Screenshot%202020-08-06%20at%209.49.19%20AM.png)
![alt text](https://github.com/savvyguru/dathena/blob/master/media/Screenshot%202020-08-06%20at%209.50.05%20AM.png)
Take note that the sensitivity score of next_client.txt got updated by celery app
![alt text](https://github.com/savvyguru/dathena/blob/master/media/Screenshot%202020-08-06%20at%2010.19.26%20AM.png)

