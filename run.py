#!/usr/bin/env python 

from app import app
from flask import Flask
name = Flask(__name__)

if __name__ == "__main__":
    app.run(debug = False)
