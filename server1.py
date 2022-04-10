
from flask import Flask
import requests
import http.client

app = Flask(__name__)


@app.route('/gateway/getdata', methods=['GET'])
def get_task():
    conn = http.client.HTTPConnection("api.rajaongkir.com")
    payload = "origin=501&destination=114&weight=1700&courier=jne"
    headers = {
        'key': "fd889414f746f5f8ca41b16fcf009837",
        'content-type': "application/x-www-form-urlencoded"
    }
    conn.request("POST", "/starter/cost", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")


if __name__ == '__main__':
    app.run(debug=True, port=8091)
