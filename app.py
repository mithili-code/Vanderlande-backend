#!/usr/bin/env python3
import os
import yaml
import aws_cdk as cdk
from stacks.pipeline_stack import PipelineStack
from stacks.config_stack import ConfigStack
# conf = json.load(open("config/config.json"))
with open("./config/config.yml", "r") as file:
    conf = yaml.load(file, Loader=yaml.BaseLoader)


app = cdk.App()
ConfigStack(app,"ConfigStack",
                env=cdk.Environment(account=conf['account'], region=conf['region']))

PipelineStack(app, "pipelineStack", 
                    env=cdk.Environment(account=conf['account'], region=conf['region']))
app.synth()