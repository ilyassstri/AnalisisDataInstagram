from define import getCreds, makeApiCall
import sys


def getHashtagInfo(params):
    """ Get info on a hashtag

    API Endpoint:
            https://graph.facebook.com/{graph-api-version}/ig_hashtag_search?user_id={user-id}&q={hashtag-name}&fields={fields}
    Returns:
            object: data from the endpoint
    """

    endpointParams = dict()  # parameter to send to the endpoint
    # user id making request
    endpointParams['user_id'] = params['instagram_account_id']
    endpointParams['q'] = params['hashtag_name']  # hashtag name
    endpointParams['fields'] = 'id,name'  # fields to get back
    endpointParams['access_token'] = params['access_token']  # access token

    url = params['endpoint_base'] + 'ig_hashtag_search'  # endpoint url

    # make the api call
    return makeApiCall(url, endpointParams, params['debug'])


def getHashtagMedia(params):
    """ Get posts for a hashtag

    API Endpoints:
            https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/top_media?user_id={user-id}&fields={fields}
            https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields}
    Returns:
            object: data from the endpoint
    """

    endpointParams = dict()  # parameter to send to the endpoint
    # user id making request
    endpointParams['user_id'] = params['instagram_account_id']
    # fields to get back
    endpointParams['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink'
    endpointParams['access_token'] = params['access_token']  # access token

    url = params['endpoint_base'] + params['hashtag_id'] + \
        '/' + params['type']  # endpoint url

    # make the api call
    return makeApiCall(url, endpointParams, params['debug'])


def getRecentlySearchedHashtags(params):
    """ Get hashtags a user has recently search for

    API Endpoints:
            https://graph.facebook.com/{graph-api-version}/{ig-user-id}/recently_searched_hashtags?fields={fields}
    Returns:
            object: data from the endpoint
    """

    endpointParams = dict()  # parameter to send to the endpoint
    endpointParams['fields'] = 'id,name'  # fields to get back
    endpointParams['access_token'] = params['access_token']  # access token

    url = params['endpoint_base'] + params['instagram_account_id'] + \
        '/' + 'recently_searched_hashtags'  # endpoint url

    # make the api call
    return makeApiCall(url, endpointParams, params['debug'])


try:  # try and get param from command line
    hashtag = sys.argv[7]  # hashtag to get info on
except:  # default to coding hashtag
    hashtag = 'daylight'  # hashtag to get info on

params = getCreds()  # params for api call
params['debug'] = 'yes'
params['hashtag_name'] = hashtag  # add on the hashtag we want to search for
hashtagInfoResponse = getHashtagInfo(params)  # hit the api for some data!
# store hashtag id
params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']

# section heading
print("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> HASHTAG INFO <<<<<<<<<<<<<<<<<<<<\n")
print("\nHashtag: " + hashtag)  # display hashtag
print("Hashtag ID: " + params['hashtag_id'])  # display hashtag id

# section heading
print("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> HASHTAG TOP MEDIA <<<<<<<<<<<<<<<<<<<<\n")
params['type'] = 'top_media'  # set call to get top media for hashtag
hashtagTopMediaResponse = getHashtagMedia(params)  # hit the api for some data!

for post in hashtagTopMediaResponse['json_data']['data']:  # loop over posts
    print("\n\n---------- POST ----------\n")  # post heading
    print("Link to post:")  # label
    print(post['permalink'])  # link to post
    print("\nPost caption:")  # label
    print(post['caption'])  # post caption
    print("\nMedia type:")  # label
    print(post['media_type'])  # type of media

# section heading
print("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> HASHTAG RECENT MEDIA <<<<<<<<<<<<<<<<<<<<\n")
params['type'] = 'recent_media'  # set call to get recent media for hashtag
hashtagRecentMediaResponse = getHashtagMedia(
    params)  # hit the api for some data!

for post in hashtagRecentMediaResponse['json_data']['data']:  # loop over posts
    print("\n\n---------- POST ----------\n")  # post heading
    print("Link to post:")  # label
    print(post['permalink'])  # link to post
    print("\nPost caption:")  # label
    print(post['caption'])  # post caption
    print("\nMedia type:")  # label
    print(post['media_type'])  # type of media

# section heading
print("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> USERS RECENTLY SEARCHED HASHTAGS <<<<<<<<<<<<<<<<<<<<\n")
getRecentSearchResponse = getRecentlySearchedHashtags(
    params)  # hit the api for some data!

# looop over hashtags
for hashtag in getRecentSearchResponse['json_data']['data']:
    print("\n\n---------- SEARCHED HASHTAG ----------\n")  # searched heading
    print("\nHashtag: " + hashtag['name'])  # display hashtag
    print("Hashtag ID: " + hashtag['id'])  # display hashtag id
