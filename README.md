# dgflask-app
### Python Application

I have used flask framework to build and render the response from the API https://api.chucknorris.io

Below are the list of the routes which will provide the respective responses.


### Note: In my case i used  both haproxy & application on same host its ip address is  192.168.1.66

### Here i have setup haproxy ipaddress as(for example IP Address: 192.168.1.66) and haproxy  act as proxy running on port no 5002 for the flask app and to access the flask run curl ex: curl http://192.168.1.66:5002/

### To monitor the status of haproxy use the url http://192.168.1.66:8404/stats (port 8404) to check the backend , session rate, error count etc..

#### 1) Route/Endpoint curl http://192.168.1.66:5002/ will return the response "Hello!!!!!! Deutsche Börse Group'" 
#### 2) To get the jokes related response hit the route http://192.168.1.66:5002/jokes 
#### 3) To get the category specific response hit the route http://192.168.1.66:5002/categories/<variable> , change variable with any name from categories list generated from the response https://api.chucknorris.io/jokes/categories example http://192.168.1.66:5002/categories/animal , http://192.168.1.66:5002/categories/political etc..
#### 4) Similar to category specific response hit the route http://192.168.1.66:5002/query/<variable>, replace variable with any name from categories list generated from the response https://api.chucknorris.io/jokes/categories example http://192.168.1.66:5002/query/money  http://192.168.1.66:5002/query/fashion etc..


## I have used the ansible to run both the haproxy and flask app 

### Haproxy ip address configured in the hosts file located dgflask-app/haproxy-dg and site.yml contain the roles & variable file for different environment. The parameter (- environments/{{ env }}/var.yml) defined in site.yml allow to use the same playbook in different environment such as test, stage, prod 

##### Make sure you change the ip address for haproxy (hosts file) ( change ipaddress: 192.168.56.109 with your environment and for backend server var.yml file each for test,stage ,prox ex - name: test-server, ip: 192.168.56.109, name: stage-server, ip: 192.168.56.110, name: prod-server, ip: 192.168.56.112



###  I Used Jenkins to deploy the haproxy and application in different environment

#### Choose any one of the three environment from choice parameter and build the job

###  Jenkins has three stages 1) Pull source code 2) Change the permission of docker.sh file to be executable , docker.sh trigger the playbook to deploy haproxy & flask app based on environment we select from choice parameter and set the variable accordingly

### Jenkins will install necessary packages like docker ,haproxy  build the app container and expose it on port based on jenkins build number thus allow us to run multiple version of docker container . But we can access the latest version of application on haproxy ip address at port 5002 for test, 5003 for stage & 5004 for prod



