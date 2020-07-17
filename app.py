#!/usr/bin/env python3

from aws_cdk import core

from twitter_trends.twitter_trends_stack import TwitterTrendsStack


app = core.App()
TwitterTrendsStack(app, "twitter-trends")

app.synth()
