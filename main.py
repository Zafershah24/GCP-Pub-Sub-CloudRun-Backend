import base64
import os
import json
from flask import Flask, request, jsonify
import emailsender
import base64
os.environ.setdefault("GCLOUD_PROJECT", "df-szafersa-s")




app = Flask(__name__)
# [END run_pubsub_server_setup]
# [END cloudrun_pubsub_server_setup]


# [START cloudrun_pubsub_handler]
# [START run_pubsub_handler]
@app.route("/", methods=["POST"])
def index():
    # data = request.get_data()
    # data=data.decode("utf-8")
    # # print(type(data))
    # data=json.loads(data)
    data=request.get_json()
    # Decoding Base64 pub sub message
    pubsub_message = data["message"]
    if isinstance(pubsub_message, dict) and "data" in pubsub_message:
        data = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()
    print(data)
    print(type(data))
    #converting to Dictionary/JSON
    data = json.loads(data)
    print(type(data))
    
    # prj_id=str(prj_id)
    mss=data['message']
    recipients=data['receivers']
    print(type(recipients))
    # query = f"""SELECT DISTINCT cdsid FROM `df-szafersa-s.event_db.denormal` where project_id={prj_id};"""
    # print(prj_id)
    # print(mss)
    # query_job = client.query(query)
    # a=[]
    # for row in query_job:
    #     a.append(str(row[0]))
        
    emailsender.recipients_list_sender(recipients,mss)

    return jsonify(mss,recipients)


# [END run_pubsub_handler]
# [END cloudrun_pubsub_handler]
@app.route('/pst',methods=['POST'])
def pst_api():
    '''
    post endpoint test
    '''
    data=""

    data = request.get_json()
    messge=data['message']
    return jsonify({'output':'Successfully delivered ! : '+ messge})

if __name__ == "__main__":
    PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080

    # This is used when running locally. Gunicorn is used to run the
    # application on Cloud Run. See entrypoint in Dockerfile.
    app.run(host="127.0.0.1", port=PORT, debug=True)
