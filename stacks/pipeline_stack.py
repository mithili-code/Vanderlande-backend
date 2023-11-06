import aws_cdk as cdk
import yaml
from constructs import Construct
from aws_cdk import(
    Environment,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    pipelines as pipelines,
    aws_codecommit as codecommit,
    aws_codebuild as codebuild
)
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from stacks.pipeline_stage import pipeline_stage
# conf = json.load(open("config/config.json"))
with open("./config/config.yml", "r") as file:
    conf = yaml.load(file, Loader=yaml.BaseLoader)

class PipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # repo = codecommit.Repository.from_repository_name(
        #         self,
        #         "Repo",
        #         repository_name="Repo"
        #     )

        cdk_pipeline =  CodePipeline(self, "Pipeline",
                        pipeline_name="Pipeline",
                        synth=ShellStep("Synth",
                            input=CodePipelineSource.git_hub(conf['RepoName'], conf['branch']),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]
                        )
                        # synth=ShellStep("Synth",
                        #     input=pipelines.CodePipelineSource.code_commit(repo, "dev"),
                        #     commands=["npm install -g aws-cdk",
                        #         "python -m pip install -r requirements.txt",
                        #         "cdk synth"]
                        # )
                    )

        
        cdk_pipeline.add_stage(pipeline_stage(self,"test-",
            env=cdk.Environment(account=conf['account'], region=conf['region'])))

