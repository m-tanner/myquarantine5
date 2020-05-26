[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# [My Quarantine 5](https://myquarantine5.com) Web App

This is the source code for hosting the back and front end of the Four Track Friday web application.
It uses Python and Flask for the back-end and Jinja2 for the front-end. Data for the app is stored 
in Google Cloud. 
The app is deployed into a Google Kubernetes Engine cluster that I manage. It is deployed via a local Skaffold
pipeline, which you can inspect at `skaffold.yml`. This is all deployed live at [myquarantine5.com](https://myquarantine5.com).

## Setup Instructions
1) Install necessary software tools. For OS X, this is:<br/>
`brew install kubernetes-cli`<br/>
`brew install kustomize`<br/>
`brew install minikube`<br/>
`brew install skaffold`<br/>
`brew tap heroku/brew && brew install heroku`<br/>
`https://cloud.google.com/sdk/docs/quickstart-macos`<br/>
`https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html`
2) Start minikube<br/>
`minikube start --driver=hyperkit`<br/>
3) Clone this repo<br/> 
`git clone <url>`
4) Create a virtual environment for the project<br/>
`virtualenv venv` and activate it `source venv/bin/activate`
5) Install the project's requirements<br/>
`pip install -r requirements.txt`
6) Setup AWS CLI and GCloud CLI on your machine, configure the authentication
7) Setup your `bash_profile`, `bashrc`, or `zshrc`
```$xslt
# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/<user>/Applications/google-cloud-sdk/path.zsh.inc' ]; then . '/Users/<user>/Applications/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/<user>/Applications/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/<user>/Applications/google-cloud-sdk/completion.zsh.inc'; fi

export GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials"

# other exports are necessary...
```
8) To view a Heroku-stored DB's in Intellij follow [this guide](https://www.jetbrains.com/help/datagrip/how-to-connect-to-heroku-postgres.html)
9) To view the Google Cloud compute engine, do something similar

## Run
Simply run the following command in your favorite terminal: `myq5_svc`<br/>
This entry point is provided by the `setup.py`.

## Test
- Pylint: `pylint -j 0 src/ --ignore='' --errors-only` `pylint -j 0 tests/ --ignore='' --errors-only`
- Flake8: `flake8 src/ --max-line-length=120 --per-file-ignores=''` `flake8 tests/ --max-line-length=120 --per-file-ignores=''`
- Black: `black --check src/` `black --check tests/`
- Pytest: `coverage run --source=src/ -m pytest tests/ -s -v --disable-pytest-warnings`
- Coverage Report: `coverage report --omit='' -m --fail-under=1`

## Use Skaffold to Build, Test, and Deploy
1) `kubectl config use-context minikube`
2) `kubectl config set-context --current --namespace=development`
3) `skaffold run --tail` 

    or 

1) `kubectl config use-context gke...`
2) `kubectl config set-context --current --namespace=production`
3) `skaffold run` or `skaffold run --tail`, which can be more helpful when troubleshooting

## Caveat
If you would actually like to run, you'll need to get authentication tokens from me, which must
be on your machine for AWS, Google Cloud, and Heroku to work.
