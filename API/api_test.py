'''
This script allows easy testing of the predictor API.
In the command line, enter the "predictor-api" folder
and type "python api_test.py".
Feel free to test your own urls or any of those listed below.
'''
import requests
import json

if __name__ == '__main__':
    # Use the address below to ping the api deployed on heroku.
    # url = "https://pic-metric-1.herokuapp.com/predictor"
    # Use the address below to ping the api you'be deployed locally.
    # You local address should look something like "127.0.0.1:5000".
    # url = 'http://<YOUR-LOCAL-ADDRESS-HERE>/predictor'
    url = 'https://das-salt-mine.herokuapp.com/predictor'

    # This is a sample image url to send to the predictor api.
    comment = 'I love driving to work. It is fun being stuck in traffic watching my life waste away.'

    # The sample url (photo_url) and a dummy "photo_id"
    # will be sent to the api.
    val = {'saltyComment': comment, 'comment_id': 123456789}
    r_success = requests.post(url, data=json.dumps(val))

    # Print the response code and content of response if
    # the "status_code" is 200.
    print(f'request responded: {r_success}.')
    if r_success.status_code == 200:
        print(f'the content of the response was {r_success.json()}')
    else:
        print(r_success)