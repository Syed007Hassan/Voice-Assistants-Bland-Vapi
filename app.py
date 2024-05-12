import os
from typing import *
import json
import sys
import time
import subprocess
import traceback
from dotenv import load_dotenv
import requests
import openai
from instruction import INSTRUCTIONS

load_dotenv()


api_key = os.getenv('OPENAI_API_KEY')
client = openai.Client(api_key=api_key)

