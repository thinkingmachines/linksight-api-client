# -*- coding: utf-8 -*-

"""Settings for python-dotenv"""

# Import standard library
from pathlib import Path

# Import from package
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(verbose=True)
