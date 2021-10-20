# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 16:10:07 2021

@author: Joe Silvan
"""

from flask import Flask, jsonify
from flasgger import Swagger

app2= Flask(__name__)

@app2.route('/')
def ping_app():
    return ("2nd micro service")


if __name__=='__main__':
    app2.run(host='0.0.0.0',port=5001)