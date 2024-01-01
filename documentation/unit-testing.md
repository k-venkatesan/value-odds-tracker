# Unit Testing
Unit testing is performed using the [unittest](https://docs.python.org/3/library/unittest.html) library.

Some points to keep in mind while writing unit tests:
1. Ensure that you `import unittest`
1. Ensure that `unittest.TestCase` is passed as a parameter to the test class
1. Ensure that test functions always start with the phrase `test` - they will otherwise not be picked up by the unit 
test framework
