# -*- coding: utf-8 -*-

"""Settings for python-dotenv"""

# Import standard library
import os

# Import from package
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(verbose=True)
