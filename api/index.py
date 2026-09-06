import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import your main app
from autoshopify_api_v3 import app

# Vercel handler
handler = app
