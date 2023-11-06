from aws_cdk import (
    # Duration,
    Stack,
    aws_secretsmanager as secrets
    # aws_sqs as sqs,
)
from constructs import Construct

class ConfigStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repo_secret = secrets.Secret(
            self,"github-token",
            secret_name="github-token"
        )
