import base64
import os
import json
from flask import Flask, request, jsonify
import emailsender
import base64
os.environ.setdefault("GCLOUD_PROJECT", "df-szafersa-s")




app = Flask(__name__)



# [START cloudrun_pubsub_handler]
# [START run_pubsub_handler]
@app.route("/", methods=["POST"])
def index():
    data = request.get_data()
    print("get_data: ")
    print(type(data))
    data=data.decode("utf-8")
    print("decode: ")
    print(type(data))
    print(data)
    data=json.loads(data)
    
    # data=request.get_json()
    print("loads:")
    print(type(data))
    
   
    # Decoding Base64 pub sub message
    pubsub_message = data["message"]
    if isinstance(pubsub_message, dict) and "data" in pubsub_message:
        data = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()
    print("decoded:")
    print(data)
    print(type(data))
    # 

    data=json.loads(data)
    print("jsonifieD")
    print(type(data))
    print(data)
    
    #converting to Dictionary/JSON
    # data = json.loads(data)
    # print(type(data))
    
    # prj_id=str(prj_id)
    mss=data["message"]
    recipients=data["receivers"]
    event_subject=data["event_subject"]
    print(type(recipients))

        
    emailsender.recipients_list_sender(recipients,mss,event_subject)

    return jsonify(mss,recipients)




if __name__ == "__main__":
    PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080

   
    app.run(host="127.0.0.1", port=PORT, debug=True)
