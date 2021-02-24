import requests
import json


def getCreds():
    creds = dict()
    creds['access_token'] = 'EAAGAaW9nKqABAJjjhzSx0wQDIZCWiZCQPGdUeq8Exsn7QqX2QQ6z0ZBWDQJVsg3Odz9kb9XlKoBwiJjow1bp991vG3noKtd9ZAwYmduAQ3HhDh4jS2ZCD02Na425Ap5EfvLuPyzfK2ZCTJAS5WETjJqCq2wcB2hagEQz4Hi3mBLDg0h4r3qELeLP8HE9GpzRSZAGqjlx1ZC9RQZDZD'

    creds['client_id'] = '422665305664160'
    creds['client_secret'] = '1715db1c383efc3d4a974f8655464e0f'
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v9.0'
    creds['endpoint_base'] = creds['graph_domain'] + \
        creds['graph_version'] + '/'
    creds['debug'] = 'no'
    creds['page_id'] = '106824740747187'
    creds['instagram_account_id'] = '17841403084310383'
    creds['ig_username'] = 'ilyassstri'

    return creds


def makeApiCall(url, endpointParams, debug='no'):
    data = requests.get(url, endpointParams)

    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)

    if('yes' == debug):
        displayApiCallData(response)

        return response


def displayApiCallData(response):
    print("\nURL: ")
    print(response['url'])
    print("\nEndpoint Params: ")
    print(response['endpoint_params_pretty'])
    print("\nResponse: ")
    print(response['json_data_pretty'])
