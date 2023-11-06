import aws_cdk as cdk
from constructs import Construct
from stacks.backend_stack import ResourceStack

class pipeline_stage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        resource_stack= ResourceStack(self, "Stack")

        