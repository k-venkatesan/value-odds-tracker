import os
import sys

# Update sys.path to include components under test
path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
if not path in sys.path:
    sys.path.insert(1, path)
del path
