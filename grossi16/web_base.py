#!/usr/bin/env python3

from flask import Flask
webapp = Flask("Grossi16")

@webapp.route("/")
def hello():
    return "Hello World!"

def start():
    webapp.run(host='0.0.0.0', port=8080)