#!/usr/bin/env python3

from aws_cdk import core
from aws_cdk.core import Tag

from twitter_trends.twitter_trends_stack import TwitterTrendsStack

app = core.App()
stack = TwitterTrendsStack(app, 'twitter-trends')
Tag.add(stack, 'ippon:owner', 'tlebrun')
app.synth()
