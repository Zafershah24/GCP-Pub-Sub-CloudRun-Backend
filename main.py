import base64
import os
import json
from flask import Flask, request, jsonify
import emailsender
import base64
os.environ.setdefault("GCLOUD_PROJECT", "df-szafersa-s")
import webex



app = Flask(__name__)



# [START cloudrun_pubsub_handler]
# [START run_pubsub_handler]
@app.route("/", methods=["POST"])
def index():
    data = request.get_data()
    print("get_data: ")
    print(type(data))
    data=data.decode("utf-8")

    data=json.loads(data)
    

    
   
    # Decoding Base64 pub sub message
    pubsub_message = data["message"]
    if isinstance(pubsub_message, dict) and "data" in pubsub_message:
        data = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()
 
    # 

    data=json.loads(data)
 
    

    
    # prj_id=str(prj_id)
    mss=data["message"]
    recipients=data["receivers"]
    event_subject=data["event_subject"]
    print(type(recipients))
    
    for recipient, notification_type in recipients.items():
        if notification_type == "email":
        # perform email action
            try:
                emailsender.recipients_list_sender(recipient,mss,event_subject)
            except:
                print("email sending failed")

        elif notification_type == "webex":
            # perform webex action
            # print(f"Scheduling WebEx meeting with {recipient}")
            try:
                webex.webexpush(recipient,event_subject,mss)
            except:
                print("webex sending failed")
        elif notification_type == "both":
            # perform both actions
            try:
                emailsender.recipients_list_sender(recipient,mss,event_subject)
                webex.webexpush(recipient,event_subject,mss)
            except:
                print("both webex and email sending failed")
        else:
            print("Sending failed xxxxxxxxxxxxxx")


        
    

    

    
    return jsonify(mss,recipients)

if __name__ == "__main__":
    PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080

   
    app.run(host="127.0.0.1", port=PORT, debug=True)
