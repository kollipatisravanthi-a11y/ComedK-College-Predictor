import sys
import os

# Add project root to path
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.insert(0, path)

from backend.app import app as application
