# Steps to run scripts
1. Get in a virtualenv
2. Make sure sure scripts are written in Pipfile
  - i.e. [scripts]
          - bootstrap = "./scripts/bootstrap__spiffy"
          - format = "./scripts/format__spiffy"
3. chmod +x scripts/bootstrap__spiffy
4. Run `pipenv run bootstrap` from root of the repo
5. Run `pipenv run format` 
6. Don't forget to `pipenv install isort black --dev`
