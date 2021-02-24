from define import getCreds, makeApiCall
import datetime


def debugAccessToken(params):
    """ Get info on an access token 

    Api Endpoint:
        https://graph.facebook.com/
        debug_token?input_token={input-token}&access_token={valid-access-token} 

    returns:
        object: data from the endpoint

    """

    endpointParams = dict()
    endpointParams['input_token'] = params['access_token']
    endpointParams['access_token'] = params['access_token']

    url = params['graph_domain'] + '/debug_token'

    return makeApiCall(url, endpointParams, params['debug'])


params = getCreds()
params['debug'] = 'yes'
response = debugAccessToken(params)

print("\nData Access Expires at: ")
print(datetime.datetime.fromtimestamp(
    response['json_data']['data']['data_access_expires_at']))

print("\nToken Expires at: ")
print(datetime.datetime.fromtimestamp(
    response['json_data']['data']['expires_at']))
