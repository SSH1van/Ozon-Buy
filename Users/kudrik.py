import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import start
start("User Data Kudrik", 1000, 5, True)