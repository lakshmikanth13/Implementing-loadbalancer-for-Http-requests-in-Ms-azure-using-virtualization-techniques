
from flask import Flask, request
import requests, sys

app = Flask(__name__)
#change the ip address according to your machine.
ipAddressWebServer2 = "40.113.1.215:8080"
ipAddressWebServer1 = "40.127.181.213:8080"



@app.route('/weight')
def output():
    global loadofserver1, loadofserver2
    result=loadbalance()
#    print ("Load of the server is : ", loadofserver1)
#    print ("Load of the server is : ", loadofserver2)
    return result


def loadbalance():
    global loadofserver1, loadofserver2
    loadofserver1=float(requests.get("http://" + ipAddressWebServer1 + "/load").content)
    loadofserver2=float(requests.get("http://" + ipAddressWebServer2 + "/load").content)


    if loadofserver1<=loadofserver2:
        loadresult=requests.get("http://" + ipAddressWebServer1 + "/")
        print ("Load of the server1 is : ", loadofserver1)
        sys.stdout.flush()
    else :
        loadresult=requests.get("http://"+ ipAddressWebServer2 + "/")
        print ("Load of the server2 is : ", loadofserver2)
        sys.stdout.flush()
    return str(loadresult.content)+("Load of VM8 is: ")+str(loadofserver1)+("   ")+("Load of VM9 is: ")+str(loadofserver2)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)

