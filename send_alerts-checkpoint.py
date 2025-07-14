import requests

def send_sms(number, message):
    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {
        "authorization": "1ZRhkMsSHVf8cry6ndJ4K5iUPFaT92oumzqpIbDel0LwX7WQgvvYeaq0E1jR2V7oNwbApK56kmM9XWnh",
        "message": message,
        "language": "english",
        "route": "q",
        "numbers": number}

    headers = {
        'cache-control': "no-cache"
    }
    try:
        response = requests.request("GET", url,
                                    headers = headers,
                                    params = querystring)
        
        print("SMS Successfully Sent")
    except:
        print("Oops! Something wrong")