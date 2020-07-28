from aws_cdk import (
    aws_s3 as s3,
    aws_events as events,
    aws_lambda as lambda_,
    aws_events_targets as targets,
    core,
)


class TwitterTrendsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self, 'tlebrun-playground')

        handler = lambda_.Function(self, 'TrendsHandler',
                                   runtime=lambda_.Runtime.PYTHON_3_8,
                                   code=lambda_.Code.asset('resources'),
                                   handler='trends.main',
                                   environment=dict(BUCKET=bucket.bucket_name,
                                                    CONSUMER_KEY='',
                                                    CONSUMER_SECRET='',
                                                    ACCESS_TOKEN_KEY='',
                                                    ACCESS_TOKEN_SECRET='',
                                                    OEID='')
                                   )

        bucket.grant_read_write(handler)

        events.Rule(self, 'RuleHandler',
                    rule_name='Twitter_Trends_15_Minutes_Rule',
                    schedule=events.Schedule.rate(duration=core.Duration.minutes(15)),
                    targets=[targets.LambdaFunction(handler)])
