- Main resource
    - https://cdkworkshop.com/15-prerequisites/200-account.html
    - https://gitlab.com/guided-explorations/aws/serverless/serverless-framework-aws

- Install Node
    - https://nodejs.org/en/download
- Install AWS CLI
    - https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
    - Maybe use an AWS docker image?
- Install libs:
    - `npm install aws-cdk-lib`
    - `sudo npm install -g aws-cdk typescript jest`
- Should I create a docker image and then have them connect vscode to that instance?
    - https://code.visualstudio.com/docs/devcontainers/attach-container


## What are my thoughts?

- Following the cdk-workshop was super easy
    - https://cdkworkshop.com/15-prerequisites/200-account.html
    - Steps:
        - In AWS:
            - Create deployment user
            - Create AKID/Secrets for user for CLI deployment
        - On local
            - Create deployment user
            - install npm and cdk
            - `aws configure` to load up creds
            - Clone sample repo
            - bootstrap the app
            - deploy the app
        - In gitlab
            - Set various AWS based perm variables
                - https://docs.gitlab.com/ee/ci/cloud_deployment/