from flask import Flask
import json
from flask import request
from flask_cors import *
from flask import make_response
import time

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.after_request
def af_request(resp):
    """
    #请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp

@app.route("/emails", methods=["POST"])
def emails_info():
    request_method = request.method
    if request_method == "POST":

       fastName = request.form.get("fastName")
       lastName = request.form.get("lastName")
       domain = request.form.get("domain")
       print(domain)

       nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
       data = json.dumps([
           {
               "date": f'{nowTime}',
               "name": f'{fastName,lastName,domain}',
               "address": 'false'
           }
       ])
       return data
    else:
        data = json.dumps({
            "message": "methodエラー",
            "code": 405
        })
        return data

if __name__ == "__main__":
    app.run(debug=True)