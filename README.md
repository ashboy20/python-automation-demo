# python-automation-demo

## Setup
This project is using `pipenv` as project interpreter, so `pipenv` needs to be installed if you do not have one.

```shell script
pip install pipenv
```

Run this command and all dependencies should be installed this virtual environment:
```shell script
pipenv install
```

`config.json` will decide which platform you are going to execution automation and the desired capabilities for appium driver are located at `/tests/test_my_observatory.py`.

After configuration have been done, run this command with appium server started:
```shell script
pipenv run python -m pytest --html=reports/report.html
```

`report.html` should be saved in `reports` folder, same path from the previous command.

## Introduction for this framework
A mobile automation testing framework based on Appium & pytest. Made the framework to be more organized with Page objects. Used `pytest-bbd` in order to have automation tests run based on Gherkin language.

## TODOs
Since this is just a demo, there are still improvements to be done:
1. Use `pytest.fixture` or even other dependency injection tools to handle Android & Ios page objects and methods better
2. Enhance the reporting: attach and embed the screenshots for the failed test cases etc
3. Extract the steps from the test runner and create a `steps` folder
4. `hooks.py`

etc