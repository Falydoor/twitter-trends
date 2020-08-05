import datetime
import json
import os

import boto3
import twitter

s3 = boto3.resource('s3')


def main(event, context):
    # Create Twitter API instance
    api = twitter.Api(consumer_key=os.environ['CONSUMER_KEY'],
                      consumer_secret=os.environ['CONSUMER_SECRET'],
                      access_token_key=os.environ['ACCESS_TOKEN_KEY'],
                      access_token_secret=os.environ['ACCESS_TOKEN_SECRET'])

    # Get top 10 trending topics for a specific location
    trends = api.GetTrendsWoeid(os.environ['OEID'])

    # Format to have a JSON document on each line
    body = '\n'.join(list(map(lambda trend: json.dumps(trend._json), trends)))

    # Save to S3 with a key like "2020-07-23 05:25:08"
    key = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    s3.Bucket(os.environ['BUCKET']).put_object(Key=key, Body=body)

    return {
        'message': 'UPLOAD OK'
    }
