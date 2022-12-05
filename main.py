from flask import Flask, render_template, request,redirect,url_for
import logging
import http.client
import requests

logger = logging.getLogger(__name__)

languages= dict()
languages['es'] = 2
languages['en']=3

# API_ENDPOINT = "https://luisitopalma.ip-zone.com/ccm/admin/api/version/2/&type=json"
API_ENDPOINT ="https://marketing@luisitopalma.com/api/v1"


app = Flask(__name__)
def subscribe_user_to_newsletter(name,email):
    conn = http.client.HTTPSConnection("luisitopalma.ipzmarketing.com")

    # payload = "{\"replace_groups\":true,\"restore_if_deleted\":true,\"status\":\"active\",\"email\":\"user@example.com\",\"name\":\"string\",\"address\":\"string\",\"city\":\"string\",\"state\":\"string\",\"country\":\"string\",\"birthday\":\"2022-12-05\",\"website\":\"string\",\"locale\":\"en\",\"time_zone\":\"Africa/Abidjan\",\"group_ids\":[1]}"
    # payload="{\"replace_groups\":true,\"restore_if_deleted\":true,\"status\":\"active\",\"email\":\"prueba@test.com\",\"name\":\"prueba\" }"

    payload = "{\"replace_groups\":true,\"restore_if_deleted\":true,\"status\":\"active\",\"email\": \""+ str(email) +"\",\"name\": \""+ str(name) + "\"}"
    
    
    print('\n')
    print('Este es el payload que se envia')
    print('\n')
    print(payload)
    print('\n')

    headers = {
        'content-type': "application/json",
        'x-auth-token': "vz3hhVaNRHM8xh3KdwDPEm7xpe2gLWicjqVKxmk_"
        }

    conn.request("POST", "/api/v1/subscribers/sync", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    return redirect(url_for('success',name=name))
    
@app.route('/success', methods=['POST'])
def success():
    name = request.form['name']
    email = request.form['email']
    subscribe_user_to_newsletter(name,email)
    return render_template('success.html', name=name)

@app.route('/', methods=['POST','GET'])
def index():
    # subscribe_user_to_newsletter()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
