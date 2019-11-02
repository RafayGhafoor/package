import requests
import re
import json
# import os


file_url = 'http://127.0.0.1:8000/media/BRANCH-7895/file-2019-10-26_00.16.40.mkv'
schedule_url = 'http://127.0.0.1:8000/media/BRANCH-7895/schedule.json'

r = requests.get(file_url)
schedule_req = requests.get(schedule_url)


def download(feed_url, filename='temp'):
    r = requests.get(feed_url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=150):
            if chunk:
                f.write(chunk)


if __name__ == '__main__':

    if r.status_code != 200 and schedule_req.status_code != 200:
        raise Exception('test')

    else:
        download(schedule_url, 'schedule.json')
        # print(r.headers)
        # print(schedule_req.headers)
        # print("passed!")
