# Component Testing
Component tests are written using the [Gherkin](https://cucumber.io/docs/gherkin/) syntax and implemented using the 
[behave](https://behave.readthedocs.io/en/latest/) library.

### Creating Component Tests

#### Feature Files
Feature files contain the high-level description of a test case described using the Gherkin syntax. The files contain a 
'.feature' extension and are necessarily placed within a directory named 'features'. 

#### Step Files
Step files contain implementations of steps described in feature files. These are placed within a 'features/steps' 
directory.

### Running Component Tests
All tests in a 'features' directory can be run using:
```
behave /path/to/features
```

If only the tests of a single feature file are to be run, this can be done using:
```
behave -i /path/to/features/specific_feature.feature
```
