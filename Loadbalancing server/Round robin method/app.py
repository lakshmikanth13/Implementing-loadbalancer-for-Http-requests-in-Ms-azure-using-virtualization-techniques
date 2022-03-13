from flask import Flask, request
import requests
import roundrobin

app = Flask(__name__)

#change the ip address in the below lines according to your machines.
ipAddressWebServer1 = "137.116.240.190:8080"
ipAddressWebServer2 = "137.116.245.199:8080"

@app.route('/')
def round_robin():
    round_robin = roundrobin.basic([0,1])
    return str(round_robin)

def output():
    a=round_robin()
    result=loadbalance()
    return result

def loadbalance():
    global a
    if a =="0":
        loadresult=requests.get("http://" + ipAddressWebServer1 + "/")
    else :
        loadresult=requests.get("http://"+ ipAddressWebServer2 + "/")
    return str(loadresult.content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)

