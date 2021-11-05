import json
import requests
import secrets as secrets

access_token = secrets.access_token


def post_data_to_portal(access_token):

    portal_url = f'https://portal.tiouk.com/api/v1/{access_token}/telemetry'

    data = json.dumps({
    'paul' : 35,
    'ben'  : 38,
                    })
    #Posting the data
    response = requests.post(url=portal_url, data=data)

    #Returns the status code
    print(response.status_code)
    return response.status_code



post_data_to_portal(access_token)
