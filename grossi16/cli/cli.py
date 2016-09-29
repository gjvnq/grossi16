#!/usr/bin/env python3

import re
import click
import webbrowser
import netifaces as netifs
import grossi16.web as web

IPV4_REGEX = re.compile("([0-9]{1,3}[.]){3}[0-9]{1,3}")
IPV6_REGEX = re.compile("([0-9]{1,3}[.]){3}[0-9]{1,3}")

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
    default="::",
    help='Address in which to bind the web server. Leave the default if you do not know what you are doing!'
)
@click.option(
    '--code',
    '-c',
    default="1234",
    type=click.IntRange(0, 65535),
    help="Teacher's console password"
)
@click.option(
    '--debug',
    '-d',
    'debug_mode',
    default=False,
    is_flag=True,
    help="If set to true, many optimization will be disabled in order to ease development. It will also automatically reload the code in event of any change. DO NOT USE IN PRODUCTION"
)
@click.option(
    '--open-browser/--no-open-browser',
    'open_browser',
    default=True,
    help="By default, your web browser will be automatically oppend as soon as the server is ready"
)
@click.option(
    '--use-threads/--no-threads',
    'threads_flag',
    default=True,
    help="Default value: True"
)
def main(addr, port, code, debug_mode, threads_flag, open_browser):
    print("Picking best ip address to use")
    user_addr = get_user_addr()
    global OpenBrowser
    OpenBrowser = open_browser

    print("Starting through cli...")

    web.main(
        addr=addr,
        user_addr=user_addr,
        port=port,
        code=code,
        debug_mode=debug_mode,
        threads_flag=threads_flag,
        onStart=startHook
    )

def get_user_addr():
    addr4 = []
    addr6 = []
    for name in netifs.interfaces():
        addr = netifs.ifaddresses(name)
        if netifs.AF_INET:
            addr4.append(addr[AF_INET])
        if netifs.AF_INET6:
            addr6.append(addr[AF_INET6])

    if len(addr4) > 0:
        return addr4
    else:
        return addr6

def startHook():
    if OpenBrowser:
        webbrowser.open("http://"+addr+":"+str(port)+"/welcome")

if __name__ == "__main__":
    main()