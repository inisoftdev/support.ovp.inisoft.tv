import jwt

def create_media_token(service_id, content_access_key):
    payload = {
        'service': {'serviceID': service_id},
        'user': {'userID': ''},
        'content': {
            'contentAccessKey': content_access_key,
            'title': ''
        },
        'drmPolicy': {
            'expireDate': None,
            'playTime': None
        },
        'playPolicy': {
            'sectionRepetition': {
                'startTime': None,
                'endTime': None
            },
            'startAt': None,
            'isAutoPlay': False,
            'enableResumePopup': False,
        },
        'customData': []
    }
    secret_key = "my_secret_key"
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    media_token = token.decode()
    return media_token
