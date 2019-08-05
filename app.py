from flask import Flask
import json
from flask import request
from flask_cors import *
from flask import make_response
import asyncio
import threading
import time

from get_info import GetInfo
from get_moke_email import main
from judgment import PostApi
from email_search import verify_istrue


app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.after_request
def af_request(resp):
    """
    #请求钩子，request受けた後，headersを挿入。
    :param resp:
    :return:
    """
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp


@app.route("/", methods=["GET"])
def index():
    data = json.dumps({
        "message": "okです",
        "code": 200
    })
    return data


@app.route("/emails", methods=["POST"])
def emails_info():
    request_method = request.method
    if request_method == "POST":
       fastName = request.form.get("fastName")
       lastName = request.form.get("lastName")
       domain = request.form.get("domain")

       fastName = GetInfo.formats(fastName)
       lastName = GetInfo.formats(lastName)

       new_loop = asyncio.new_event_loop()
       asyncio.set_event_loop(new_loop)
       loop = asyncio.get_event_loop()

       task = asyncio.ensure_future(main(fastName, lastName, domain))
       loop.run_until_complete(task)
       mokeEmails = task.result()
       mokeEmails = mokeEmails.split("\n")
       mokeEmails = [x.strip() for x in mokeEmails]
       mokeEmails = [x for x in mokeEmails if x != '']

       email_list = []

       # for email in mokeEmails[:3]:
       #     p = PostApi()
       #     ans = p.send(email)
       #     email_list.append(ans)
       #     time.sleep(5)

       for email in mokeEmails:
           time.sleep(1)
           email_list.append(verify_istrue(email))

       data = json.dumps(email_list)
       return data
    else:
        data = json.dumps({
            "message": "methodエラー",
            "code": 405
        })
        return data

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000,)
    threading.Thread(target=app.run).start()