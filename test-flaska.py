# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:04:21 2020

@author: mattw
"""


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()