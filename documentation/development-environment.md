# Development Environment

### Operating System
The development environment has been designed for setup in Linux. While it is expected to be possible to work on this 
project in a Windows or Mac environment, this is currently not being tested.

### Development Language
Python has been selected as the development language for the project primarily due to the availability of libraries to 
fetch and analyse web content.

More specifically, Python 3.12 is being used as it was the latest released version when the project started.

The easiest way to install a specific version of Python is to use the deadsnakes PPA:
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.12
```
This does not replace the existing Python version installed on your system, so to specifically use this version of 
Python, run:
```
python3.12 some_python_file.py
```

### Code Editor
While any code editor can be used for development, the configuration files committed to this repository make PyCharm a 
convenient choice. The free-to-use Community Edition can be downloaded from the 
[JetBrains](https://www.jetbrains.com/pycharm/download/) website.

### Virtual Environment
It is strongly recommended to use a virtual environment for the sake of a consistent development environment across all 
developers contributing to the project. This is especially convenient to ensure that identical versions of libraries and 
tools are available to everyone.

This can be easily setup using PyCharm by navigating to File > Settings > Project > Python Interpreter > 
Add Interpreter > Add Local Interpreter > Virtualenv Environment. Ensure that the base interpreter is Python 3.12 - 
other options can be left untouched.

Alternatively, the virtual environment can also be setup through the terminal as described in the 
[venv documentation](https://docs.python.org/3/library/venv.html).

Once you are inside the virtual environment, all necessary libraries and tools can be installed using:
```
pip install -r requirements.txt
```
