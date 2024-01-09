# Unit Testing
Unit testing is performed using the [unittest](https://docs.python.org/3/library/unittest.html) library.

### Creating Unit Tests
Using PyCharm, a unit test file can be easily created by right-clicking on the directory where you want the file to be 
placed, and going to New > Python File > Python unit test. This should automatically create a skeleton file - ensure 
that while renaming the test function, it continues to start with `test_` - the test will otherwise not be picked up by 
the unit test framework. 

Alternatively, the unit test file can be created from scratch with the following points in mind:
1. Ensure that you `import unittest`
1. Ensure that `unittest.TestCase` is passed as a parameter to the test class
1. Ensure that test functions always start with the phrase `test_`

### Running Unit Tests
With PyCharm, simply right-click the unit test file and select 'Run Python tests in ...'. 

Alternatively, it can be run from the terminal by executing:
```
python -m unittest /path/to/file.py`
```

### Generating Coverage Reports
Coverage reports can be generated using the [coverage.py](https://coverage.readthedocs.io/en/7.4.0/) tool. To execute a 
unit test with coverage measurement enabled, replace `python` with `coverage` while running it:
```
coverage -m unittest /path/to/file.py
```
To then view the coverage report, simply run:
```
coverage report
```
Special include/exclude rules for coverage can be configured in the pyproject.toml file. The coverage.py documentation 
describes these in further detail, along with a variety of options for generating reports.
