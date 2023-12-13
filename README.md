## What have I done?
- I added a dockerfile and a docker-compose file that runs flask-apps and an nginx to send traffic to those multiple flask-app instances.
- I added captures for Sentry.io to capture 'Payment Error' and 'Hacker Warning'. (see sentry.png image)
- I added docker compose file to run logstash, elasticsearch and kibana containers. I redirected the output of the flask-app containers to the logstash.

## Requirements
- Python for 'illegal_item.py' script. (I used 3.12.0 but it shouldn't make much difference.)
- Docker for docker-compose (I used Docker Desktop  4.25.1 for Windows)


##Steps
1. Build and run 5 instances of the containers
```
docker-compose -f ./app/docker-compose.yml up --scale ecommerceapp=5 --detach
```
2. Run logging containers
```
docker-compose -f ./logging/docker-compose.yml up --detach
```
3. Open Flask app
```
http://127.0.0.1:5000/
```
4. Open Elastic
```
http://localhost:5601/
```
5. Check menu>observability>logs

Illegal Item : 

```
python .\illegal_item.py
```



#build and run single container
#docker build --tag docker-flask-app ./app
#docker run -p 5000:5000 docker-flask-app
#docker run --log-driver=gelf --log-opt gelf-address=udp://127.0.0.1:12201 -p 5000:5000 docker-flask-app