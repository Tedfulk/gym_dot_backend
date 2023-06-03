# Steps to run scripts
1. Get in a virtualenv
2. Make sure sure scripts are written in Pipfile
  - i.e. [scripts]
          - bootstrap = "./scripts/bootstrap__spiffy"
          - format = "./scripts/format__spiffy"
3. chmod +x scripts/bootstrap__spiffy or have #!/usr/bin/env python as the first line in the bootstrap__spiffy script
4. Run `pipenv run bootstrap` from root of the repo
5. You should now be able to run any other script from any directory inside the project. Run `pipenv run format` to test it out.  
6. Don't forget to `pipenv install isort black --dev`
