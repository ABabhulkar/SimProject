# SimProject

### Imp Commands
```pip install -r requirements.txt```

## References
1. Makefile
   - https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#extending-the-app-conclusion
   - https://github.com/flaskbb/flaskbb/blob/master/Makefile

## Temp 
### Reference application with socket communication
This is reference application here we have a main as server and app as client.

### Server side
In this application server starts and open the socket at localhost at 5002 port. Then server waits for client to join with timeout of 11s. Server can handle 2 clients connections at a time. 
Once client is connected a new thread will be started to handle communication with that client where all received msg are printed on console and forwarded to all connected clients.

### Client side
On client side it starts and tries to connect with server. Once connected it will start to send alive msg periodically till 10s and then terminals. While sending msg it checks for received msg and prints them on console.

### How to run
1. Start the main in one terminal with following command
```python3 main.py```
3. Open other terminal and start client 1
```python3 app.py 1```
3. Open new terminal and start client 2
```Python3 app.py 2```