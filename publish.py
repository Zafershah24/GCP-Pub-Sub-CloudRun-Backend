from google.cloud import bigquery
from google.cloud import pubsub_v1
import json
topic_id="pubsub2DF"
project_id = "df-szafersa-s"
 
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)
code = "We Says Thanks!"
message="hello"
html = """\


<html>
  <head></head>
  <body>
    <p>Thank you for being a loyal customer.<br>
       Here is your unique code to unlock exclusive content:<br>
       <br><br><h1>{code}</h1><br>
       <br><h1>{message}</h1><br>
      
    </p>
  </body>
</html>
""".format(code=code,message=message)
# var="test"
# message="hello"+var
print(html)
json_data={
        'event_ID':"testDB1",
        'event_msg':html,
        'event_source':"testDB1",
        'event_subject':"Dynamic"
        }
json_data1 = json.dumps(json_data)
data=json_data1.encode('utf-8')
print(data)
res=publisher.publish(topic_path,data)
print(f'The published message is {res.result()}')