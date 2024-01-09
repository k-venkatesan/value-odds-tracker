# Continuous Integration
Continuous Integration (CI) is implemented using [GitHub Actions](https://docs.github.com/en/actions). A workflow has 
been set up for this project that triggers automated checks for every push to the repository:

### Automated Checks
- **code-format-check:** The codebase is scanned using the formatting tool described in [Code Style](code-style.md) - 
this job only checks for conformance to the tool's standard and does not make any modifications - if the check fails, 
following the instructions in the [Code Style](code-style.md) document to reformat the code appropriately should fix it
- **unit-tests:** All unit tests in the project are executed with code coverage enabled - see 
[Unit Testing](unit-testing.md) for more details
- **component-tests:** All component tests in the project are executed with code coverage enabled - see
[Component Testing](component-testing.md) for more details

### Known Issues
- **Duplicate code:** GitHub Actions does not support a straightforward approach to reuse steps/configurations defined 
in YAML workflow files. See [this open issue](https://github.com/actions/starter-workflows/issues/245) for example. 
Until this is resolved, it is accepted that the YAML file will contain multiple jobs with duplicate code.
- **HTML coverage reports:** GitHub Actions does not support viewing build artifacts on the site itself - they can only 
be downloaded as zip file. See [this open issue](https://github.com/actions/upload-artifact/issues/14) for example. 
Until this is resolved, it is accepted that HTML code coverage reports are not generated in the workflow since they are 
less useful when they cannot be directly viewed on GitHub.
