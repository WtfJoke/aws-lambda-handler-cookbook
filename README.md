# AWS Lambda Cookbook - Elevate your handler's code

This repository is designed to be a starting point for a new business service in the platform.
In order to create a new repository from this template follow these steps -
What makes an AWS Lambda handler resilient, traceable and easy to maintain? How do you write such a code?

This repository provides a working, open source based, AWS Lambda handler skeleton Python code.
This handler embodies Serverless best practices and has all the bells and whistles for a proper production ready handler.
It will cover issues such as logging, tracing, input validation, features flags, dynamic configuration, and how to safely use environment variables.
While the code examples are written in Python, the principles are valid to any supported AWS Lambda handler programming language.

Most of the code examples here are taken from the excellent AWS Lambda Powertools repository.
I've written several of the utilities which are mentioned in this blog series and donated 2 of them, the parser and feature flags to AWS Lambda Powertools.

This repository is the complementary code examples of my blog series "AWS Lambda Cookbook - Elevate your handler's code"

First post:


## Getting started
```shell script
pipenv install --dev
make pr
```

### Unit tests
Unit tests can be found under the `tests` folder.
You can run the tests by using the following command:
```shell script
pytest -v
```


To calculate test code coverage us the command:
```shell script
pytest --cov
```
