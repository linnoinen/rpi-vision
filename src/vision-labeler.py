#!/bin/python

import argparse
import base64
import picamera
import json

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def takephoto():
    camera = picamera.PiCamera()
    camera.capture('photo.jpg')


def main():
    takephoto()

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)

    with open('photo.jpg', 'rb') as image:
        image_content = base64.b64encode(iamge.read())
        service_request = service.images().annotate(body ={
            'requests': [{
                'iamge': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 10
                }]
            }]
        })
        response = service_request.execute()
        print json.dumps(response, indent=4, sort_keys=True)


if __name__ == '__main__':
    main()