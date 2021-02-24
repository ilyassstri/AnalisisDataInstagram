from define import getCreds, makeApiCall


def getUserPages(params):
    """ Get facebook pages for a user

    API Endpoint
        http://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}

    returns:
        object: data from the endpoint
    """

    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + 'me/accounts'

    return makeApiCall(url, endpointParams, params['debug'])


params = getCreds()
params['debug'] = 'yes'
response = getUserPages(params)

print("\n----- FACEBOOK PAGE INFO -----")
print("\nPage Name:")
print(response['json_data']['data'][0]['name'])
print("\nPage Category:")
print(response['json_data']['data'][0]['category'])
print("\nPage Id:")
print(response['json_data']['data'][0]['id'])
