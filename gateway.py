from flask import Flask
import flask
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/server1/getdata', methods=['GET'])
def get_data():
    url = 'http://localhost:8091/gateway/getdata'
    response = requests.request('GET', url)
    return response.text


@app.route('/server2/getdata', methods=['GET', 'POST'])
def get_data2():
    if flask.request.method == 'GET':
        url = 'http://localhost:8092/siswa/get_data_siswa'
        response = requests.request('GET', url)
        return response.text
    else:
        url = 'http://localhost:8092/siswa/insert_data_siswa'
        response = requests.request('POST', url)
        return response.text


if __name__ == '__main__':
    app.run(debug=True, port=8090)
