# Code Style

For uniformity in code style, adhere to the [PEP-8](https://peps.python.org/pep-0008/) style guide. This establishes 
standards for concerns such as naming conventions and use of blank lines. The former is an example of a concern that 
the developer needs to make a conscious decision on, while the latter can be easily enforced through the use of a 
formatting tool. The choice of tool for this project is [black](https://black.readthedocs.io/en/stable/). To 
automatically format all files using black, simply run this in the root of the repository:
``````
black .
``````
Note that this only formats Python files.
