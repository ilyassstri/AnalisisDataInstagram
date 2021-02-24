from define import getCreds, makeApiCall


def getInstagramAccount(params):
    """ Get instagram account

        API Endpoint
            http://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}$fields=instagram_business_account

        returns:
            object: data from the endpoint
        """
    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    endpointParams['fields'] = 'instagram_business_account'

    url = params['endpoint_base'] + params['page_id']

    return makeApiCall(url, endpointParams, params['debug'])


params = getCreds()
params['debug'] = 'yes'
response = getInstagramAccount(params)

print("\n----- INSTAGRAM ACCOUNT INFO -----\n")
print("\nPage Id:")
print(response['json_data']['id'])
print("\nInstagram Business Account Id:")
print(response['json_data']['instagram_business_account']['id'])
