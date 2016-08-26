#!/usr/bin/env python3

__author__ = "Gabriel Queiroz"
__credits__ = ["Gabriel Queiroz", "Estevão Lobo", "Pedro Ilído"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Gabriel Queiroz"
__email__ = "gabrieljvnq@gmail.com"
__status__ = "Pre-alpha"

from flask import Flask
webapp = Flask("Grossi16")

@webapp.route("/")
def hello():
    return "Hello World!"

def main():
    webapp.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    main()