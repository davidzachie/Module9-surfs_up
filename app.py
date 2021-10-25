# 9.4.3 Set Up Flask and Create a Route
# Install Flask by running the following in the command line in terminal (in PythonData env): pip install flask


# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'
