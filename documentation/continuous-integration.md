# Continuous Integration
Continuous Integration (CI) is implemented using [GitHub Actions](https://docs.github.com/en/actions). A workflow has 
been set up for this project that triggers the following automated checks for every push made to the repository:
- code-formatting: The codebase is scanned using the formatting tool described in [Code Style](code-style.md) - this job 
only checks for conformance to the tool's standard and does not make any modifications - if the check fails, follow the
instructions in the [Code Style](code-style.md) document to reformat the code appropriately.