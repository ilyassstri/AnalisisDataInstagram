from define import getCreds, makeApiCall


def getUserMedia(params):
    """ Get users media

    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}

    returns:
        object: data from the endpoint
    """

    endpointParams = dict()
    endpointParams['fields'] = 'id, caption, media_type, media_url, permalink, thumbnail_url, timestamp, username'
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + params['instagram_account_id'] + '/media'

    return makeApiCall(url, endpointParams, params['debug'])


def getMediaInsights(params):
    """ Get insights for a specific media id

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{ig-media-id}/insights?metric={metric}
    Returns:
            object: data from the endpoint
    """
    endpointParams = dict()  # parameter to send to the endpoint
    endpointParams['metric'] = params['metric']  # fields to get back
    endpointParams['access_token'] = params['access_token']  # access token

    url = params['endpoint_base'] + \
        params['latest_media_id'] + '/insights'  # endpoint url

    # make the api call
    return makeApiCall(url, endpointParams, params['debug'])


def getUserInsights(params):
    """ Get users media

    API Endpoint:
        https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}

    returns:
        object: data from the endpoint
    """

    endpointParams = dict()
    endpointParams['metric'] = 'follower_count,impressions,profile_views,reach'
    endpointParams['period'] = 'day'
    endpointParams['access_token'] = params['access_token']

    url = params['endpoint_base'] + \
        params['instagram_account_id'] + '/insights'  # endpoint url

    return makeApiCall(url, endpointParams, params['debug'])


params = getCreds()
params['debug'] = 'yes'
response = getUserMedia(params)


print("\n----- LATEST POST -----\n")
print("\tLink to post:")
print("\t" + response['json_data']['data'][0]['permalink'])
print("\n\tPost Caption:")
print("\t" + response['json_data']['data'][0]['caption'])
print("\n\tMedia type:")
print("\t" + response['json_data']['data'][0]['media_type'])
print("\n\tPosted at")
print("\t" + response['json_data']['data'][0]['timestamp'])

params['latest_media_id'] = response['json_data']['data'][0]['id']

if 'VIDEO' == response['json_data']['data'][0]['media_type']:
    params['metric'] = 'engagement, impressions, reach, saved, video_views'
else:
    params['metric'] = 'engagement, impressions, reach, saved'

response = getUserInsights(params)

print("\n----- LATEST POST INSIGHTS -----\n")

for insight in response['json_data']['data']:  # loop over post insights
    # display info
    print("\t" + insight['title'] + " (" + insight['period'] +
          "): " + str(insight['values'][0]['value']))
 # get insights for a user

response = getUserInsights(params)

print("\n---- DAILY USER ACCOUNT INSIGHTS -----\n")

for insight in response['json_data']['data']:
    print("\t" + insight['title'] + " (" + insight['period'] +
          "): " + str(insight['values'][0]['value']))

    for value in insight['values']:
        print("\t\t" + value['end_time'] + ": " + str(value['value']))
