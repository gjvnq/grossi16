#!/usr/bin/env python3

import click
import webbrowser
import grossi16.web as web

@click.command(context_settings={"resilient_parsing": True})
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
@click.option(
    '--debug',
    '-d',
    'debug_mode',
    default=False,
    is_flag=True,
    help="If set to true, many optimization will be disabled in order to ease development. It will also automatically reload the code in event of any change. DO NOT USE IN PRODUCTION"
)
@click.option(
    '--use-threads/--no-threads',
    'threads_flag',
    default=True,
    help="Default value: True"
)
def main(addr, port, code, debug_mode, threads_flag):
    q = Queue()
    t_opener = Thread(target=web_opener, args=(q,))
    t_server = Thread(target=web.main, kwargs={
        "addr"=addr,
        "port"=port,
        "code"=code,
        "debug_mode"=debug_mode,
        "threads_flag"=threads_flag,
        "com_channel"=q
    })
    t_server.start()
    t_opener.start()

def web_opener(q):
    while True:
        data = q.get()
        print(data)
        #webbrowser.open_new_tab(addr+':'+str(port))

if __name__ == "__main__":
    main()