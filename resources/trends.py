import datetime
import json
import os

import boto3
import twitter

s3 = boto3.resource('s3')


def main(event, context):
    api = twitter.Api(consumer_key=os.environ['CONSUMER_KEY'],
                      consumer_secret=os.environ['CONSUMER_SECRET'],
                      access_token_key=os.environ['ACCESS_TOKEN_KEY'],
                      access_token_secret=os.environ['ACCESS_TOKEN_SECRET'])

    trends = api.GetTrendsWoeid(os.environ['OEID'])
    body = '\n'.join(list(map(lambda trend: json.dumps(trend._json), trends)))
    s3.Bucket(os.environ['BUCKET']).put_object(
        Key=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), Body=body)

    return {
        'message': 'UPLOAD OK'
    }
