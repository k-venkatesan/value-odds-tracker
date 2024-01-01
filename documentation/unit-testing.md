# Unit Testing
Unit testing is performed using the [unittest](https://docs.python.org/3/library/unittest.html) library.

Using PyCharm, a unit test file can be easily created by right-clicking on the directory where you want the file to be 
placed, and going to New > Python File > Python unit test. This should automatically create a skeleton file - ensure 
that while renaming the test function, it continues to start with `test_` - the test will otherwise not be picked up by 
the unit test framework. 

Alternatively, the unit test file can be created from scratch with the following points in mind:
1. Ensure that you `import unittest`
1. Ensure that `unittest.TestCase` is passed as a parameter to the test class
1. Ensure that test functions always start with the phrase `test_`
