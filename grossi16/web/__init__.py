#!/usr/bin/env python3

__author__ = "Gabriel Queiroz"
__credits__ = ["Gabriel Queiroz", "Estevão Lobo", "Pedro Ilído"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Gabriel Queiroz"
__email__ = "gabrieljvnq@gmail.com"
__status__ = "Pre-alpha"

import click
import logging
import flask
import tempfile
import pkg_resources

NoCache = True

# WEB PART
FilesCache = {}
webapp = flask.Flask("Grossi16")

def templater(name, **kwargs):
    tempfile_src = pkg_resources.resource_string("grossi16.web", "templates/"+name)
    print(kwargs)
    return flask.render_template_string(
        str(tempfile_src, encoding="utf-8"),
        **kwargs)

def get_mime_from_extension(file):
    ext = file.split(".")[-1]
    if ext == "css":
        return "text/css"
    if ext == "html":
        return "text/html"
    if ext == "js":
        return "application/javascript"
    if ext == "woff2":
        return "application/x-font-woff"
    if ext == "png":
        return "image/png"
    return ""

@webapp.route("/")
def who_are_you():
    return templater("index.html")

@webapp.route("/student")
def student_page():
    o = []
    o.append({"id": 1, "text": "hi"})
    o.append({"id": 2, "text": "hi3"})
    o.append({"id": 3, "text": "hi2"})
    return templater("student.html", options=o, question="hi")

@webapp.route("/teacher")
def teacher_page():
    return templater("teacher.html")

@webapp.route("/ajax/<command>")
def ajax_cmd(command):
    return command

@webapp.errorhandler(404)
def page_not_found(error):
    return templater("404.html"), 404

@webapp.route("/static/<path>")
def static_handler(path):
    if NoCache == True:
        data = pkg_resources.resource_string("grossi16.web", "static/"+path)
        mime = get_mime_from_extension(path)
        return data, 200, {'Content-Type': mime+'; charset=utf-8'}
    elif NoCache == False and path in FilesCache:
        data = FilesCache[path]
        mime = get_mime_from_extension(path)
        return data, 200, {'Content-Type': mime+'; charset=utf-8'}
    else:
        abort(404)

# CLI PART

@click.command()
@click.option(
    '--port',
    '-p',
    default=8080,
    type=click.IntRange(0, 65535),
    help='Port in which the web server will listen to'
)
@click.option(
    '--bind-address',
    'addr',
    '-a',
    default="0.0.0.0",
    help='Address in which to bind the web server. Leave the default if you do not know what you are doing!'
)
@click.option(
    '--code',
    '-c',
    default="1234",
    type=click.IntRange(0, 65535),
    help="Teacher's console password"
)
def main(addr, port, code):
    # Load files in memory
    global FilesCache
    if NoCache == False:
        print("Loading files...")
        for name in pkg_resources.resource_listdir("grossi16.web", "static"):
            print("Loading "+name+"...")
            FilesCache[name] = pkg_resources.resource_string("grossi16.web", "static/"+name)
        print("Files loaded!")

    # Start webserver
    print("Starting webserver")
    webapp.run(host=addr, port=port)

if __name__ == "__main__":
    main()